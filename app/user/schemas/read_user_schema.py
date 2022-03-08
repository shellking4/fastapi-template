from .user_base_schema import UserBaseSchema

class ReadUserSchema(UserBaseSchema):
    
    class Config:
        orm_mode = True