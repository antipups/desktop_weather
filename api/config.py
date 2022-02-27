class Filenames:
    config_ini = 'config.ini'


class Urls:
    FiveDayWeather = 'https://api.openweathermap.org/data/2.5/forecast?' \
                     'q={city},{country}&' \
                     'lang=en&' \
                     'units={units}&' \
                     'appid={app_id}'


a = {
    "cod": "200",
    "message": 0,
    "cnt": 40,
    "list": [
        {
            "dt": 1645963200,
            "main": {
                "temp": 275.19,
                "feels_like": 270.76,
                "temp_min": 275.19,
                "temp_max": 275.74,
                "pressure": 1026,
                "sea_level": 1026,
                "grnd_level": 1002,
                "humidity": 64,
                "temp_kf": -0.55
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "пасмурно",
                    "icon": "04d"
                }
            ],
            "clouds": {
                "all": 100
            },
            "wind": {
                "speed": 5.04,
                "deg": 354,
                "gust": 6.25
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2022-02-27 12:00:00"
        },
        {
            "dt": 1645974000,
            "main": {
                "temp": 275.11,
                "feels_like": 271.27,
                "temp_min": 275.11,
                "temp_max": 275.21,
                "pressure": 1026,
                "sea_level": 1026,
                "grnd_level": 1002,
                "humidity": 62,
                "temp_kf": -0.1
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "пасмурно",
                    "icon": "04d"
                }
            ],
            "clouds": {
                "all": 89
            },
            "wind": {
                "speed": 4,
                "deg": 0,
                "gust": 6.16
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2022-02-27 15:00:00"
        },
        {
            "dt": 1645984800,
            "main": {
                "temp": 274.32,
                "feels_like": 270.38,
                "temp_min": 274.32,
                "temp_max": 274.32,
                "pressure": 1027,
                "sea_level": 1027,
                "grnd_level": 1003,
                "humidity": 63,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "облачно с прояснениями",
                    "icon": "04n"
                }
            ],
            "clouds": {
                "all": 64
            },
            "wind": {
                "speed": 3.89,
                "deg": 9,
                "gust": 5.97
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2022-02-27 18:00:00"
        },
        {
            "dt": 1645995600,
            "main": {
                "temp": 274.47,
                "feels_like": 271.05,
                "temp_min": 274.47,
                "temp_max": 274.47,
                "pressure": 1027,
                "sea_level": 1027,
                "grnd_level": 1003,
                "humidity": 64,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "пасмурно",
                    "icon": "04n"
                }
            ],
            "clouds": {
                "all": 100
            },
            "wind": {
                "speed": 3.23,
                "deg": 15,
                "gust": 4.8
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2022-02-27 21:00:00"
        },
        {
            "dt": 1646006400,
            "main": {
                "temp": 273.74,
                "feels_like": 270.32,
                "temp_min": 273.74,
                "temp_max": 273.74,
                "pressure": 1026,
                "sea_level": 1026,
                "grnd_level": 1002,
                "humidity": 79,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "пасмурно",
                    "icon": "04n"
                }
            ],
            "clouds": {
                "all": 100
            },
            "wind": {
                "speed": 3.05,
                "deg": 9,
                "gust": 4.65
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2022-02-28 00:00:00"
        },
        {
            "dt": 1646017200,
            "main": {
                "temp": 273.12,
                "feels_like": 269.08,
                "temp_min": 273.12,
                "temp_max": 273.12,
                "pressure": 1026,
                "sea_level": 1026,
                "grnd_level": 1002,
                "humidity": 80,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "пасмурно",
                    "icon": "04n"
                }
            ],
            "clouds": {
                "all": 99
            },
            "wind": {
                "speed": 3.65,
                "deg": 6,
                "gust": 5.77
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2022-02-28 03:00:00"
        },
        {
            "dt": 1646028000,
            "main": {
                "temp": 273.01,
                "feels_like": 268.99,
                "temp_min": 273.01,
                "temp_max": 273.01,
                "pressure": 1026,
                "sea_level": 1026,
                "grnd_level": 1002,
                "humidity": 77,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "пасмурно",
                    "icon": "04d"
                }
            ],
            "clouds": {
                "all": 87
            },
            "wind": {
                "speed": 3.59,
                "deg": 21,
                "gust": 5.22
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2022-02-28 06:00:00"
        },
        {
            "dt": 1646038800,
            "main": {
                "temp": 275.49,
                "feels_like": 272.2,
                "temp_min": 275.49,
                "temp_max": 275.49,
                "pressure": 1026,
                "sea_level": 1026,
                "grnd_level": 1002,
                "humidity": 61,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "облачно с прояснениями",
                    "icon": "04d"
                }
            ],
            "clouds": {
                "all": 63
            },
            "wind": {
                "speed": 3.34,
                "deg": 30,
                "gust": 4.26
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2022-02-28 09:00:00"
        },
        {
            "dt": 1646049600,
            "main": {
                "temp": 277.8,
                "feels_like": 274.86,
                "temp_min": 277.8,
                "temp_max": 277.8,
                "pressure": 1024,
                "sea_level": 1024,
                "grnd_level": 1001,
                "humidity": 53,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "переменная облачность",
                    "icon": "03d"
                }
            ],
            "clouds": {
                "all": 45
            },
            "wind": {
                "speed": 3.55,
                "deg": 29,
                "gust": 4.28
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2022-02-28 12:00:00"
        },
        {
            "dt": 1646060400,
            "main": {
                "temp": 276.98,
                "feels_like": 273.63,
                "temp_min": 276.98,
                "temp_max": 276.98,
                "pressure": 1024,
                "sea_level": 1024,
                "grnd_level": 1000,
                "humidity": 58,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "небольшая облачность",
                    "icon": "02d"
                }
            ],
            "clouds": {
                "all": 11
            },
            "wind": {
                "speed": 3.91,
                "deg": 36,
                "gust": 5.1
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2022-02-28 15:00:00"
        },
        {
            "dt": 1646071200,
            "main": {
                "temp": 275.41,
                "feels_like": 272.34,
                "temp_min": 275.41,
                "temp_max": 275.41,
                "pressure": 1025,
                "sea_level": 1025,
                "grnd_level": 1001,
                "humidity": 68,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "переменная облачность",
                    "icon": "03n"
                }
            ],
            "clouds": {
                "all": 29
            },
            "wind": {
                "speed": 3.03,
                "deg": 63,
                "gust": 6.05
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2022-02-28 18:00:00"
        },
        {
            "dt": 1646082000,
            "main": {
                "temp": 274.88,
                "feels_like": 270.91,
                "temp_min": 274.88,
                "temp_max": 274.88,
                "pressure": 1024,
                "sea_level": 1024,
                "grnd_level": 1000,
                "humidity": 68,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "облачно с прояснениями",
                    "icon": "04n"
                }
            ],
            "clouds": {
                "all": 63
            },
            "wind": {
                "speed": 4.12,
                "deg": 64,
                "gust": 6.41
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2022-02-28 21:00:00"
        },
        {
            "dt": 1646092800,
            "main": {
                "temp": 274.65,
                "feels_like": 270.66,
                "temp_min": 274.65,
                "temp_max": 274.65,
                "pressure": 1024,
                "sea_level": 1024,
                "grnd_level": 1000,
                "humidity": 69,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "облачно с прояснениями",
                    "icon": "04n"
                }
            ],
            "clouds": {
                "all": 82
            },
            "wind": {
                "speed": 4.07,
                "deg": 68,
                "gust": 6.4
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2022-03-01 00:00:00"
        },
        {
            "dt": 1646103600,
            "main": {
                "temp": 274.76,
                "feels_like": 270.4,
                "temp_min": 274.76,
                "temp_max": 274.76,
                "pressure": 1023,
                "sea_level": 1023,
                "grnd_level": 999,
                "humidity": 69,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "пасмурно",
                    "icon": "04n"
                }
            ],
            "clouds": {
                "all": 100
            },
            "wind": {
                "speed": 4.72,
                "deg": 68,
                "gust": 7.75
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2022-03-01 03:00:00"
        },
        {
            "dt": 1646114400,
            "main": {
                "temp": 275.18,
                "feels_like": 271.03,
                "temp_min": 275.18,
                "temp_max": 275.18,
                "pressure": 1023,
                "sea_level": 1023,
                "grnd_level": 999,
                "humidity": 72,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "пасмурно",
                    "icon": "04d"
                }
            ],
            "clouds": {
                "all": 100
            },
            "wind": {
                "speed": 4.54,
                "deg": 75,
                "gust": 8.66
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2022-03-01 06:00:00"
        },
        {
            "dt": 1646125200,
            "main": {
                "temp": 278.39,
                "feels_like": 274.68,
                "temp_min": 278.39,
                "temp_max": 278.39,
                "pressure": 1022,
                "sea_level": 1022,
                "grnd_level": 999,
                "humidity": 56,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "облачно с прояснениями",
                    "icon": "04d"
                }
            ],
            "clouds": {
                "all": 54
            },
            "wind": {
                "speed": 5.24,
                "deg": 79,
                "gust": 7
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2022-03-01 09:00:00"
        },
        {
            "dt": 1646136000,
            "main": {
                "temp": 280.24,
                "feels_like": 276.86,
                "temp_min": 280.24,
                "temp_max": 280.24,
                "pressure": 1020,
                "sea_level": 1020,
                "grnd_level": 997,
                "humidity": 55,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "облачно с прояснениями",
                    "icon": "04d"
                }
            ],
            "clouds": {
                "all": 64
            },
            "wind": {
                "speed": 5.59,
                "deg": 80,
                "gust": 7.33
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2022-03-01 12:00:00"
        },
        {
            "dt": 1646146800,
            "main": {
                "temp": 279.61,
                "feels_like": 276.34,
                "temp_min": 279.61,
                "temp_max": 279.61,
                "pressure": 1020,
                "sea_level": 1020,
                "grnd_level": 997,
                "humidity": 64,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "небольшой дождь",
                    "icon": "10d"
                }
            ],
            "clouds": {
                "all": 100
            },
            "wind": {
                "speed": 4.93,
                "deg": 92,
                "gust": 9.3
            },
            "visibility": 10000,
            "pop": 0.3,
            "rain": {
                "3h": 0.1
            },
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2022-03-01 15:00:00"
        },
        {
            "dt": 1646157600,
            "main": {
                "temp": 278.85,
                "feels_like": 275.07,
                "temp_min": 278.85,
                "temp_max": 278.85,
                "pressure": 1020,
                "sea_level": 1020,
                "grnd_level": 997,
                "humidity": 70,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "небольшой дождь",
                    "icon": "10n"
                }
            ],
            "clouds": {
                "all": 100
            },
            "wind": {
                "speed": 5.67,
                "deg": 95,
                "gust": 11.24
            },
            "visibility": 10000,
            "pop": 0.34,
            "rain": {
                "3h": 0.35
            },
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2022-03-01 18:00:00"
        },
        {
            "dt": 1646168400,
            "main": {
                "temp": 277.43,
                "feels_like": 273.31,
                "temp_min": 277.43,
                "temp_max": 277.43,
                "pressure": 1019,
                "sea_level": 1019,
                "grnd_level": 996,
                "humidity": 93,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "небольшой дождь",
                    "icon": "10n"
                }
            ],
            "clouds": {
                "all": 100
            },
            "wind": {
                "speed": 5.6,
                "deg": 109,
                "gust": 11.1
            },
            "visibility": 4715,
            "pop": 0.71,
            "rain": {
                "3h": 1.24
            },
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2022-03-01 21:00:00"
        },
        {
            "dt": 1646179200,
            "main": {
                "temp": 276.85,
                "feels_like": 272.92,
                "temp_min": 276.85,
                "temp_max": 276.85,
                "pressure": 1019,
                "sea_level": 1019,
                "grnd_level": 995,
                "humidity": 95,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "небольшой дождь",
                    "icon": "10n"
                }
            ],
            "clouds": {
                "all": 100
            },
            "wind": {
                "speed": 4.89,
                "deg": 99,
                "gust": 9.93
            },
            "visibility": 181,
            "pop": 1,
            "rain": {
                "3h": 2.54
            },
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2022-03-02 00:00:00"
        },
        {
            "dt": 1646190000,
            "main": {
                "temp": 277.3,
                "feels_like": 273.67,
                "temp_min": 277.3,
                "temp_max": 277.3,
                "pressure": 1019,
                "sea_level": 1019,
                "grnd_level": 995,
                "humidity": 95,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "небольшой дождь",
                    "icon": "10n"
                }
            ],
            "clouds": {
                "all": 100
            },
            "wind": {
                "speed": 4.53,
                "deg": 119,
                "gust": 8.84
            },
            "visibility": 10000,
            "pop": 0.5,
            "rain": {
                "3h": 0.34
            },
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2022-03-02 03:00:00"
        },
        {
            "dt": 1646200800,
            "main": {
                "temp": 277.9,
                "feels_like": 275.31,
                "temp_min": 277.9,
                "temp_max": 277.9,
                "pressure": 1019,
                "sea_level": 1019,
                "grnd_level": 995,
                "humidity": 90,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "пасмурно",
                    "icon": "04d"
                }
            ],
            "clouds": {
                "all": 100
            },
            "wind": {
                "speed": 3.06,
                "deg": 140,
                "gust": 5.5
            },
            "visibility": 10000,
            "pop": 0.38,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2022-03-02 06:00:00"
        },
        {
            "dt": 1646211600,
            "main": {
                "temp": 279.89,
                "feels_like": 277.36,
                "temp_min": 279.89,
                "temp_max": 279.89,
                "pressure": 1018,
                "sea_level": 1018,
                "grnd_level": 994,
                "humidity": 66,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "пасмурно",
                    "icon": "04d"
                }
            ],
            "clouds": {
                "all": 100
            },
            "wind": {
                "speed": 3.62,
                "deg": 152,
                "gust": 5
            },
            "visibility": 10000,
            "pop": 0.06,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2022-03-02 09:00:00"
        },
        {
            "dt": 1646222400,
            "main": {
                "temp": 280.33,
                "feels_like": 277.87,
                "temp_min": 280.33,
                "temp_max": 280.33,
                "pressure": 1016,
                "sea_level": 1016,
                "grnd_level": 993,
                "humidity": 60,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "пасмурно",
                    "icon": "04d"
                }
            ],
            "clouds": {
                "all": 100
            },
            "wind": {
                "speed": 3.66,
                "deg": 159,
                "gust": 5.32
            },
            "visibility": 10000,
            "pop": 0.01,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2022-03-02 12:00:00"
        },
        {
            "dt": 1646233200,
            "main": {
                "temp": 279.68,
                "feels_like": 277.47,
                "temp_min": 279.68,
                "temp_max": 279.68,
                "pressure": 1016,
                "sea_level": 1016,
                "grnd_level": 993,
                "humidity": 69,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "пасмурно",
                    "icon": "04d"
                }
            ],
            "clouds": {
                "all": 100
            },
            "wind": {
                "speed": 3.03,
                "deg": 138,
                "gust": 5.36
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2022-03-02 15:00:00"
        },
        {
            "dt": 1646244000,
            "main": {
                "temp": 278.12,
                "feels_like": 276.42,
                "temp_min": 278.12,
                "temp_max": 278.12,
                "pressure": 1016,
                "sea_level": 1016,
                "grnd_level": 993,
                "humidity": 83,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "пасмурно",
                    "icon": "04n"
                }
            ],
            "clouds": {
                "all": 100
            },
            "wind": {
                "speed": 2.06,
                "deg": 141,
                "gust": 4.08
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2022-03-02 18:00:00"
        },
        {
            "dt": 1646254800,
            "main": {
                "temp": 277.28,
                "feels_like": 275.56,
                "temp_min": 277.28,
                "temp_max": 277.28,
                "pressure": 1015,
                "sea_level": 1015,
                "grnd_level": 992,
                "humidity": 91,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "пасмурно",
                    "icon": "04n"
                }
            ],
            "clouds": {
                "all": 100
            },
            "wind": {
                "speed": 1.95,
                "deg": 147,
                "gust": 3.51
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2022-03-02 21:00:00"
        },
        {
            "dt": 1646265600,
            "main": {
                "temp": 276.8,
                "feels_like": 275.52,
                "temp_min": 276.8,
                "temp_max": 276.8,
                "pressure": 1013,
                "sea_level": 1013,
                "grnd_level": 989,
                "humidity": 93,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "пасмурно",
                    "icon": "04n"
                }
            ],
            "clouds": {
                "all": 100
            },
            "wind": {
                "speed": 1.53,
                "deg": 115,
                "gust": 1.91
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2022-03-03 00:00:00"
        },
        {
            "dt": 1646276400,
            "main": {
                "temp": 276.23,
                "feels_like": 275.05,
                "temp_min": 276.23,
                "temp_max": 276.23,
                "pressure": 1012,
                "sea_level": 1012,
                "grnd_level": 989,
                "humidity": 92,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "пасмурно",
                    "icon": "04n"
                }
            ],
            "clouds": {
                "all": 85
            },
            "wind": {
                "speed": 1.4,
                "deg": 172,
                "gust": 2.76
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2022-03-03 03:00:00"
        },
        {
            "dt": 1646287200,
            "main": {
                "temp": 276.8,
                "feels_like": 276.8,
                "temp_min": 276.8,
                "temp_max": 276.8,
                "pressure": 1011,
                "sea_level": 1011,
                "grnd_level": 988,
                "humidity": 86,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "пасмурно",
                    "icon": "04d"
                }
            ],
            "clouds": {
                "all": 93
            },
            "wind": {
                "speed": 1.04,
                "deg": 244,
                "gust": 1.8
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2022-03-03 06:00:00"
        },
        {
            "dt": 1646298000,
            "main": {
                "temp": 278,
                "feels_like": 275.6,
                "temp_min": 278,
                "temp_max": 278,
                "pressure": 1011,
                "sea_level": 1011,
                "grnd_level": 987,
                "humidity": 76,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "небольшой дождь",
                    "icon": "10d"
                }
            ],
            "clouds": {
                "all": 100
            },
            "wind": {
                "speed": 2.84,
                "deg": 173,
                "gust": 4.26
            },
            "visibility": 10000,
            "pop": 0.4,
            "rain": {
                "3h": 0.14
            },
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2022-03-03 09:00:00"
        },
        {
            "dt": 1646308800,
            "main": {
                "temp": 280.06,
                "feels_like": 278.71,
                "temp_min": 280.06,
                "temp_max": 280.06,
                "pressure": 1008,
                "sea_level": 1008,
                "grnd_level": 985,
                "humidity": 54,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "небольшой дождь",
                    "icon": "10d"
                }
            ],
            "clouds": {
                "all": 100
            },
            "wind": {
                "speed": 2.04,
                "deg": 206,
                "gust": 3.26
            },
            "visibility": 10000,
            "pop": 0.32,
            "rain": {
                "3h": 0.12
            },
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2022-03-03 12:00:00"
        },
        {
            "dt": 1646319600,
            "main": {
                "temp": 279.07,
                "feels_like": 279.07,
                "temp_min": 279.07,
                "temp_max": 279.07,
                "pressure": 1008,
                "sea_level": 1008,
                "grnd_level": 985,
                "humidity": 57,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "пасмурно",
                    "icon": "04d"
                }
            ],
            "clouds": {
                "all": 100
            },
            "wind": {
                "speed": 1.24,
                "deg": 252,
                "gust": 2.05
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2022-03-03 15:00:00"
        },
        {
            "dt": 1646330400,
            "main": {
                "temp": 277.93,
                "feels_like": 277.93,
                "temp_min": 277.93,
                "temp_max": 277.93,
                "pressure": 1008,
                "sea_level": 1008,
                "grnd_level": 985,
                "humidity": 62,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "пасмурно",
                    "icon": "04n"
                }
            ],
            "clouds": {
                "all": 100
            },
            "wind": {
                "speed": 1.29,
                "deg": 297,
                "gust": 1.87
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2022-03-03 18:00:00"
        },
        {
            "dt": 1646341200,
            "main": {
                "temp": 276.9,
                "feels_like": 274.68,
                "temp_min": 276.9,
                "temp_max": 276.9,
                "pressure": 1008,
                "sea_level": 1008,
                "grnd_level": 984,
                "humidity": 67,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "пасмурно",
                    "icon": "04n"
                }
            ],
            "clouds": {
                "all": 100
            },
            "wind": {
                "speed": 2.38,
                "deg": 246,
                "gust": 2.93
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2022-03-03 21:00:00"
        },
        {
            "dt": 1646352000,
            "main": {
                "temp": 275.65,
                "feels_like": 272.83,
                "temp_min": 275.65,
                "temp_max": 275.65,
                "pressure": 1007,
                "sea_level": 1007,
                "grnd_level": 984,
                "humidity": 78,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "пасмурно",
                    "icon": "04n"
                }
            ],
            "clouds": {
                "all": 100
            },
            "wind": {
                "speed": 2.79,
                "deg": 235,
                "gust": 4.08
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2022-03-04 00:00:00"
        },
        {
            "dt": 1646362800,
            "main": {
                "temp": 274.06,
                "feels_like": 271.08,
                "temp_min": 274.06,
                "temp_max": 274.06,
                "pressure": 1006,
                "sea_level": 1006,
                "grnd_level": 983,
                "humidity": 90,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "облачно с прояснениями",
                    "icon": "04n"
                }
            ],
            "clouds": {
                "all": 82
            },
            "wind": {
                "speed": 2.63,
                "deg": 253,
                "gust": 4.54
            },
            "visibility": 9160,
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2022-03-04 03:00:00"
        },
        {
            "dt": 1646373600,
            "main": {
                "temp": 274.25,
                "feels_like": 271.07,
                "temp_min": 274.25,
                "temp_max": 274.25,
                "pressure": 1008,
                "sea_level": 1008,
                "grnd_level": 984,
                "humidity": 90,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 600,
                    "main": "Snow",
                    "description": "небольшой снег",
                    "icon": "13d"
                }
            ],
            "clouds": {
                "all": 87
            },
            "wind": {
                "speed": 2.89,
                "deg": 244,
                "gust": 4.59
            },
            "visibility": 4498,
            "pop": 0.21,
            "snow": {
                "3h": 0.24
            },
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2022-03-04 06:00:00"
        },
        {
            "dt": 1646384400,
            "main": {
                "temp": 276.04,
                "feels_like": 272.77,
                "temp_min": 276.04,
                "temp_max": 276.04,
                "pressure": 1007,
                "sea_level": 1007,
                "grnd_level": 983,
                "humidity": 70,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 600,
                    "main": "Snow",
                    "description": "небольшой снег",
                    "icon": "13d"
                }
            ],
            "clouds": {
                "all": 99
            },
            "wind": {
                "speed": 3.47,
                "deg": 270,
                "gust": 4.67
            },
            "visibility": 8294,
            "pop": 0.26,
            "snow": {
                "3h": 0.2
            },
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2022-03-04 09:00:00"
        }
    ],
    "city": {
        "id": 709717,
        "name": "Донецк",
        "coord": {
            "lat": 48,
            "lon": 37.8
        },
        "country": "UA",
        "population": 1024700,
        "timezone": 7200,
        "sunrise": 1645935265,
        "sunset": 1645974544
    }
}
