import re
from typing import Union
from pydantic import BaseModel, validator
from .Preferences import Preferences
from .Global_Preferences import Global_Preferences
from .UserInformations import UserInformations

class User(BaseModel):

    preferences: Preferences | Global_Preferences = None
    informations: UserInformations

    class Config:
        orm_mode=True
