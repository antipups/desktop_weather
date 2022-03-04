import os

from api.weather_5_day import get_weather_on_five_day
from schemas.weather_5_day import WeatherOneItem


def test_amount_items():
    """
        Тест который проверяет кол-во выходных данных после обработки данных из апи
    :return:
    """
    status, weather = get_weather_on_five_day()

    assert status and int(weather.cod) == 200
    assert weather.cnt == 40
    assert len(weather.list) == 5


def test_type_data():
    """
        Проверка на то, все ли данные прошли валидацию и успешно были провалидированы
    :return:
    """
    status, weather = get_weather_on_five_day()

    assert len(weather.list) == 5
    for item in weather.list:
        assert isinstance(item, WeatherOneItem)


def test_exists_picture():
    """
        Проверка на то, все ли картинки достижимы для полученных данных
    :return:
    """
    status, weather = get_weather_on_five_day()
    images = tuple(os.listdir('../static/icons/'))

    assert len(weather.list) == 5
    for item in weather.list:
        assert isinstance(item, WeatherOneItem)
        assert item.weather
        assert item.weather[-1].icon + '.png' in images