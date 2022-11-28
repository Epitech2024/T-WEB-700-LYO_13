import re
from typing import Union
from pydantic import BaseModel, validator
from .Preferences import Preferences
from .Global_Preferences import Global_Preferences


class User(BaseModel):
    username: str = None
    email: str = None
    password: str = None
    role: int = None
    preferences: Union[Preferences, Global_Preferences, None] = None

    class Config:
        orm_mode=True

    @validator("username")
    def username_must_be_alphanum(value):
        if not value:
            raise ValueError("Valid username should only contain alphanumerical characters.")
        return value

    @validator("email")
    def email_must_match_regex(value):
        regex = re.compile(r"^\w+@\w+\.[a-z]+")
        if not re.match(regex, value):
            raise ValueError("Input value is not a valid email address.")
        return value