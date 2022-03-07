from sqlalchemy import MetaData
from passlib.context import CryptContext


crypto_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def combine_metadata(*args):
    all_in_one_metadata = MetaData()
    for metadata in args:
        for t in metadata.tables.values():
            t.tometadata(all_in_one_metadata)
    return all_in_one_metadata

def hash_password(password: str):
    return crypto_context.hash(password)

def verify_hash(plain_password: str, hash: str):
    return crypto_context.verify(plain_password, hash)

