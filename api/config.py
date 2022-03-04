"""
    Конфигурационный файл, хранение констанкт для api модуля
"""

class Filenames:
    config_ini = 'config.ini'


class Urls:
    FiveDayWeather = 'https://api.openweathermap.org/data/2.5/forecast?' \
                     'q={city},{country}&' \
                     'lang=en&' \
                     'units={units}&' \
                     'appid={app_id}'

