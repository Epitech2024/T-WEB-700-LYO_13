import re
from pydantic import BaseModel, validator

class UserInformations(BaseModel):
    username: str
    email: str
    password: str
    role: int

    class Config:
        orm_mode = True

    @validator("email")
    def email_must_match_regex(value):
        regex = re.compile(r"^\w+@\w+\.[a-z]+")
        if not re.match(regex, value):
            raise ValueError("Input value is not a valid email address.")
        return value