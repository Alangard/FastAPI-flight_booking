from pydantic_settings import BaseSettings, SettingsConfigDict


class GlobalSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_NAME: str = "postgres"
    
    api_prefix: str = "/api/v1"
    TG_BOT_TOKEN:str
    TUNNEL_URL:str 

    # static files
    STATIC_HOST: str = "http://localhost:8001"

settings = GlobalSettings()