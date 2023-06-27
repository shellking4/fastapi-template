from fastapi import APIRouter, Depends, HTTPException, status
from pymysql import IntegrityError
from app.auth.schemas.token_data_schema import TokenDataSchema
from typing import Any
from sqlalchemy.orm import Session
from app.auth.services.auth_service import auth_service
from app.core import database
import requests
import json

from app.user.models.lead_model import Lead


router = APIRouter(prefix="/users")

@router.get("", response_model=TokenDataSchema, status_code=200)
def get_users(*, db: Session = Depends(database.get_db), auth_user = Depends(auth_service.get_current_user)):
    return auth_user

@router.get("/fetch-leads", response_model=Any, status_code=200)
def fetch_leads(*, db: Session = Depends(database.get_db)):
    url = "https://suitecrmdemo.dtbc.eu/service/v4/rest.php"
    headers = { "Content-Type": "application/json" }
    
    auth_rest_data = { 
        "user_auth" : { 
            "user_name": "Demo", 
            "password": "f0258b6685684c113bad94d91b8fa02a"
        }
    }

    querystring = {"method":"login","input_type":"JSON","response_type":"JSON","rest_data": json.dumps(auth_rest_data)}
    response = requests.request("GET", url, headers=headers, params=querystring)
    sessionId = json.loads(response.content)["id"]

    offset = 0
    keep_going = True
    while keep_going:
        fetch_response = fetch_leads_data(db, sessionId, offset)
        total_count = fetch_response["total_count"]
        offset = fetch_response["next_offset"]
        keep_going = (offset < total_count)
        print(keep_going)
    return 1
    


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
    query_response = json.loads(requests.request("GET", url, headers=headers, params=leads_query_string).content)
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
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail=f'An error occured during the insert'
            )
    return {
        "next_offset": next_offset, 
        "total_count": int(total_count)
    }
    
