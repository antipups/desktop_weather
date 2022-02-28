from typing import Tuple
from requests import get
from configparser import ConfigParser
from api.config import Urls, Filenames
from general_config import logging
from schemas.weather_5_day import WeatherFiveDay


config = ConfigParser()
# config.read(Filenames.config_ini)
config.read('../' + Filenames.config_ini)


@logging()
def get_response() -> Tuple[bool, str | dict]:
    """
        Метод получения данных на 5 дней
    :return:
    """

    api_settings = config['Weather Api Settings']

    try:
        response = get(url=Urls.FiveDayWeather.format(city=api_settings['primary_city'],
                                                      country=api_settings['primary_country'],
                                                      units=api_settings['units'],
                                                      app_id=config['Keys']['AppId']
                                                      ))
        if not response.ok:
            raise Exception('Status not 200')

    except Exception as e:
        return False, e.__str__()

    else:
        return True, response.json()


def get_weather_on_five_day():
    """
        Получение погоды на 5 дней
    :return:
    """
    status, data = get_response()
    if status:
        print(WeatherFiveDay.parse_obj(data))


if __name__ == '__main__':
    get_weather_on_five_day()
