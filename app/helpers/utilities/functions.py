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

def is_slice_in_list(slice, list):
    len_slice = len(slice) 
    return any(slice == list[i : len_slice + i] for i in range(len(list) - len_slice + 1))

def is_any_slice_element_in_list(slice, list):
    return any(i in list for i in slice)