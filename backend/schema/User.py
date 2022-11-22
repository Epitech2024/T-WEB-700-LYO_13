import re
from typing import Union
from pydantic import BaseModel, Field, validator
from .Preferences import Preferences
from .Global_Preferences import Global_Preferences


class User(BaseModel):
    username: str = Field(unique=True)
    email: str = Field(unique=True)
    password: str = Field(...)
    role: int = Field(...)
    preferences: Union[Preferences, Global_Preferences, None] = None

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
    