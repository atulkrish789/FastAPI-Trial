import datetime

from pydantic import BaseModel

from data.Language import LanguageEnum
from data.genre import GenreEnum


class MovieBaseModel(BaseModel):
    name:str
    genre: GenreEnum
    release_date:datetime.date
    rating:float
    language:LanguageEnum
