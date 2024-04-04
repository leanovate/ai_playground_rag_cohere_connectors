from pydantic_settings import BaseSettings
from pydantic import BaseModel


class Settings(BaseSettings):

    confluence_user: str
    confluence_api_token: str
    confluence_product_url: str
    confluence_connector_api_key: str
    confluence_search_limit: int = 8
    items_per_user: int = 50

    class Config:
        case_sensitive = False


class Query(BaseModel):
    query: str
