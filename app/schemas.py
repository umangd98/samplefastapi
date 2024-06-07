from pydantic import BaseModel, EmailStr, constr

class UserCreate(BaseModel):
    email: EmailStr
    password: constr(min_length=6)

class User(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None

class PostCreate(BaseModel):
    text: constr(max_length=1024)

class Post(BaseModel):
    id: int
    text: str
    owner_id: int

    class Config:
        orm_mode = True
