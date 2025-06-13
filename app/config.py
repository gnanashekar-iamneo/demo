from pydantic_settings import BaseSettings
from pydantic import Field
from typing import List
import os

class Settings(BaseSettings):
    # ==========================
    # DATABASE CONFIGURATION
    # ==========================
    database_url: str = Field(..., env="DATABASE_URL")

    # ==========================
    # JWT CONFIGURATION
    # ==========================
    secret_key: str = Field(..., env="SECRET_KEY")
    algorithm: str = Field(default="HS256", env="ALGORITHM")
    access_token_expire_minutes: int = Field(default=15, env="ACCESS_TOKEN_EXPIRE_MINUTES")

    # ==========================
    # LOGGING
    # ==========================
    log_level: str = Field(default="INFO", env="LOG_LEVEL")
    debug:bool=Field(default=True,env="DEBUG")
    # ==========================
    # FILE UPLOAD SETTINGS
    # ==========================
    upload_dir: str = Field(default="submissions", env="UPLOAD_DIR")
    max_file_size: int = Field(default=10485760, env="MAX_FILE_SIZE")
    #allowed_file_extensions: str = Field(default=".pdf,.doc,.docx,.txt,.zip,.rar", env="ALLOWED_FILE_EXTENSIONS")

    # Computed property -/////////Need to learn
    # @property
    # def allowed_extensions_list(self) -> List[str]:
    #     return [ext.strip() for ext in self.allowed_file_extensions.split(",")]

    # ==========================
    # APP SETTINGS - learn in dep;loument stratergy
    # ==========================
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# use this instace for access env for modlarality 
settings = Settings()


os.makedirs(settings.upload_dir, exist_ok=True)
os.makedirs("logs", exist_ok=True)

#best practice is to use os.path.dirname 