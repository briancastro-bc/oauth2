from typing import Optional, List, Union

from pydantic import AnyHttpUrl, BaseSettings, validator

"""
    :class Settings - Toma las variables de entorno como propiedades.
"""
class Settings(BaseSettings):
    # PROJECT VARIABLES
    PROJECT_NAME: str
    PROJECT_SECRET_KEY: str
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl]

    # MONGODB VARIABLES
    MONGO_HOST: Optional[str]
    MONGO_PORT: Optional[int]
    MONGO_URI: str

    # VALIDATORS
    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()