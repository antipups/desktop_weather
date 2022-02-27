from requests import get
from configparser import ConfigParser
from api.config import Urls, Filenames
from schemas.weather_5_day import WeatherFiveDay


config = ConfigParser()
config.read(Filenames.config_ini)


def get_response():
    """
        Метод получения данных на 5 дней
    :return:
    """

    api_settings = config['Wheater Api Settings']

    try:
        response = get(url=Urls.FiveDayWeather.format(city=api_settings['primary_city'],
                                                      contry=api_settings['primary_country'],
                                                      units=api_settings['units'],
                                                      appid=config['Keys']['AppId']
                                                      ))
        if not response.ok:
            raise Exception('Status not 200')

    except Exception as e:
        return False, e

    else:
        True, response.json()


def get_weather_on_five_day():
    """
        Получение погоды на 5 дней
    :return:
    """
    status, data = get_response()
    if status:
        WeatherFiveDay.parse_obj(data)
