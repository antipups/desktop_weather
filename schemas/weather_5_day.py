import datetime
from typing import List

from pydantic import BaseModel, validator, Field

from schemas.custom_enums import WeatherIcons


class Main_PartItem(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    sea_level: int
    grnd_level: int
    humidity: int
    temp_kf: float


class Weather_PartItem(BaseModel):
    id: int
    main: str
    description: str
    icon: WeatherIcons


class Clouds_PartItem(BaseModel):
    all: int


class Wind(BaseModel):
    speed: float
    deg: int
    gust: float


class Sys:
    pod: str


class WeatherOneItem(BaseModel):
    dt: int
    main: Main_PartItem
    weather: List[Weather_PartItem]
    clouds: Clouds_PartItem
    wind: Wind
    visibility: int
    pop: int
    sys: Sys
    dt_text: datetime.datetime


class WeatherFiveDay(BaseModel):
    cod: str
    message: int
    cnt: int = Field(gt=5)
    list: List[WeatherOneItem]

    @validator('cod')
    def check_status_code(self, v):
        return int(v) == 200 and v
