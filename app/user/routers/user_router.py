from fastapi import APIRouter, BackgroundTasks, Depends
from app.auth.schemas.token_data_schema import TokenDataSchema
from typing import Any
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.auth.services.auth_service import auth_service
from app.core import database
from sqlalchemy import desc, asc
import httpx
import json
from app.user.models.btc_usd_price_price_model import BtcUsdPrice

from app.user.models.lead_model import Lead


router = APIRouter(prefix="/users")


@router.get("", response_model=TokenDataSchema, status_code=200)
def get_users(*, db: Session = Depends(database.get_db), auth_user = Depends(auth_service.get_current_user)):
    return auth_user


@router.get("/fetch-leads", response_model=Any, status_code=200)
def fetch_leads(*, db: Session = Depends(database.get_db), background_tasks: BackgroundTasks):
    background_tasks.add_task(batch_fetch_leads, db)
    return { "message": "job added" }


@router.get("/get-leads", response_model=Any, status_code=200)
def get_leads(*, db: Session = Depends(database.get_db)):
    leads = db.query(Lead).order_by(desc(Lead.created_at)).all()
    return leads


@router.get("/fetch-btc-usd-price", response_model=Any, status_code=200)
def fetch_btc_usd_price(*, db: Session = Depends(database.get_db)):
    binance_api_url = "https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT"
    price_data = httpx.get(binance_api_url).json()
    btc_price_model = BtcUsdPrice(value=price_data["price"])
    db.add(btc_price_model)
    try:
        db.commit()
        db.refresh(btc_price_model)
    except IntegrityError:
        db.rollback()
    return btc_price_model

@router.get("/get-btc-usd-price", response_model=Any, status_code=200)
def get_btc_usd_price(*, db: Session = Depends(database.get_db)):
    btc_usd_prices = db.query(BtcUsdPrice).order_by(desc(BtcUsdPrice.created_at)).all()
    return btc_usd_prices


def fetch_leads_data(db: Session, suite_crm_session_id, offset):
    url = "https://suitecrmdemo.dtbc.eu/service/v4/rest.php"
    headers = { "Content-Type": "application/json" }
    leads_rest_data = {
        "session": suite_crm_session_id,
        "module_name": "Leads",
        "query": "leads.id IS NOT NULL",
        "order_by": "",
        "offset": offset
    }
    leads_query_string = {"method":"get_entry_list","input_type":"JSON","response_type":"JSON","rest_data": json.dumps(leads_rest_data)}
    query_response = httpx.get(url, headers=headers, params=leads_query_string).json()
    next_offset = query_response["next_offset"]
    total_count = query_response["total_count"]
    leads_data = query_response["entry_list"]
    for lead in leads_data:
        item_data = {
            "phone_work": lead["name_value_list"]["phone_work"]["value"],
            "first_name": lead["name_value_list"]["first_name"]["value"],
            "last_name": lead["name_value_list"]["last_name"]["value"]
        }
        new_lead = Lead(**item_data)
        db.add(new_lead)
        try:
            db.commit()
        except IntegrityError as error:
            db.rollback()
            continue
    return {
        "next_offset": next_offset, 
        "total_count": int(total_count)
    }
    
def batch_fetch_leads(db: Session):
    url = "https://suitecrmdemo.dtbc.eu/service/v4/rest.php"
    headers = { "Content-Type": "application/json" }
    
    auth_rest_data = { 
        "user_auth" : { 
            "user_name": "Demo", 
            "password": "f0258b6685684c113bad94d91b8fa02a"
        }
    }
    querystring = {"method":"login","input_type":"JSON","response_type":"JSON","rest_data": json.dumps(auth_rest_data)}
    response = httpx.get(url, headers=headers, params=querystring).json()
    sessionId = response["id"]
    offset = 0
    keep_going = True
    while keep_going:
        fetch_response = fetch_leads_data(db, sessionId, offset)
        total_count = fetch_response["total_count"]
        offset = fetch_response["next_offset"]
        keep_going = (offset < total_count)
    return 1
