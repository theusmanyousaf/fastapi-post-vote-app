from pydantic import BaseModel, EmailStr, field_validator
from datetime import datetime

# Request [from user to us]
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

    class config:
        orm_mode = True

class PostCreate(PostBase):
    pass

class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Response [from us to user]
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class config:
        orm_mode = True

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int

class Vote(BaseModel):
    post_id: int
    dir: int

    @field_validator('dir')
    def check_dir(cls, value):
        if value not in (0, 1):
            raise ValueError('dir must be either 0 or 1')
        return value
