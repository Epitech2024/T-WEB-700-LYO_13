from typing import List
from pydantic import BaseModel, Field


class Preferences(BaseModel):
    selected_crypto: set[str] = None
    article_keywords: set[str] = None

    class Config:
        orm_mode=True