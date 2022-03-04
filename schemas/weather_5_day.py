"""
    Валидация запроса на 5 дней по апи
"""

import datetime
from typing import List, Optional

from pydantic import BaseModel, validator, Field

# from schemas.custom_enums import WeatherIcons


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
    icon: str


class Clouds_PartItem(BaseModel):
    all: int


class Wind(BaseModel):
    speed: float
    deg: int
    gust: float


class WeatherOneItem(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    dt: int
    main: Main_PartItem
    weather: List[Weather_PartItem]
    clouds: Clouds_PartItem
    wind: Wind
    visibility: int
    dt_txt: datetime.datetime


class WeatherCityCoords(BaseModel):
    lat: float
    lon: float


class WeatherCity(BaseModel):
    id: int
    name: str
    coord: WeatherCityCoords
    country: str
    population: int
    timezone: int
    sunrise: int
    sunset: int


class WeatherFiveDay(BaseModel):
    cod: str
    message: int
    cnt: int = Field(gt=5)
    list: List[WeatherOneItem]
    city: WeatherCity

    @validator('cod')
    def check_status_code(cls, v) -> bool | str:
        """
            Валидация на код 200
        :param v: код
        :return: фолс или сам код
        """
        return int(v) == 200 and v

    @validator('list')
    def check_list_on_need_time(cls, items_weather_list) -> List:
        """
            Отбор нужных данных из апи (погода каждого дня ТОЛЬКО 12:00:00)
        """

        initial_list = tuple(items_weather_list)
        result_list = []

        for one_item in initial_list:
            if datetime.datetime.strptime('12:00:00', '%H:%M:%S').time() == one_item.dt_txt.time():
                result_list.append(one_item)

        return result_list


