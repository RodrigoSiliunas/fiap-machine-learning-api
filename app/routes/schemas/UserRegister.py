from pydantic import BaseModel


class UserRegister(BaseModel):
    name: str
    username: str
    email: str
    password: str
