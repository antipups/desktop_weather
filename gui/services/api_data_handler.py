"""
    Обработка данных полученных из апи для гуи
"""
import datetime
from typing import List

from loguru import logger

from api.weather_5_day import get_weather_on_five_day
from general_config import logging, STATIC, ICONS, path_join
from schemas.weather_5_day import WeatherFiveDay, WeatherOneItem
from pprint import pformat as pretty_print


class OneWeatherDataItem:

    date: datetime.datetime = None
    icon: str
    title: str
    description: str

    def __init__(self, item: WeatherOneItem):
        self.date = item.dt_txt
        weather = item.weather[-1]
        self.icon = self.get_icon_name(icon=weather.icon)
        self.title = weather.main
        self.description = weather.description

    def get_icon_name(self, icon: str) -> str:
        return path_join(ICONS, icon) + '.png'


class DataHandler:
    """
        Класс который создан для обработки данных с апи и загрузки в гуи
    """

    data: WeatherFiveDay = None
    data_to_gui: List[OneWeatherDataItem] = None

    def __init__(self):
        self.handle_data()

    @logging(exit=True)
    def _load_data_from_api(self) -> WeatherFiveDay:
        """
            Получаем данные по api
        :return: объект полученных данных (pydantic схема)
        """

        status, data = get_weather_on_five_day()

        if not status:
            raise Exception(f'Ошибка статуса при данных {data}')

        else:
            return data

    def _handle_each_weather_item(self):
        """
            Обработка каждого полученного объекта по апи (объекта погоды)
        :return:
        """

        self.data_to_gui = []
        for item in self.data.list:
            self.data_to_gui.append(OneWeatherDataItem(item=item))

    def handle_data(self):
        self.data = self._load_data_from_api()
        logger.info(f'\n\nПолучил данные:\n\n{pretty_print(self.data.dict())}\n\n')
        self._handle_each_weather_item()
