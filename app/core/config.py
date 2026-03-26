from pydantic_settings import BaseSettings  


class Settings(BaseSettings):
    app_name: str
    app_version:str

    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str

    @property
    def connection_url(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    class Config:
        env_file = ".env"


settings = Settings()