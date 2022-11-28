from pydantic import BaseModel


class Global_Preferences(BaseModel):
    n_crypto: int = None
    k_articles: int = None
    list_crypto: set[str] = None
    list_sources: set[str] = None

    class Config:
        orm_mode = True