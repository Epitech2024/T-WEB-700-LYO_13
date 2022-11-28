from typing import List
from pydantic import BaseModel, Field


class Global_Preferences(BaseModel):
    n_crypto: int = Field()
    k_articles: int = Field()
    list_crypto: set[str] = set()
    list_sources: set[str] = set()
