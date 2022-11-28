from typing import List
from pydantic import BaseModel, Field


class Preferences(BaseModel):
    selected_crypto: set[str] = set()
    article_keywords: set[str] = set()
