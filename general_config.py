"""
    Общий конфиг, тут хранятся токены, и прочее, то, что не должно быть на гите
"""

import functools
import os
import sys
from configparser import ConfigParser
from loguru import logger
from os.path import join as path_join


def check_supported_version():
    return sys.version_info.major == 3 and sys.version_info.minor >= 10


def create_virtualenv():
    """
        Создание виртуальной среды для запуска всего кода
    :return:
    """
    try:
        import loguru

    except ModuleNotFoundError:

        if check_supported_version():
            separator = '\n' + '=' * 100 + '\n'
            print(separator + '\nVenv not setup, creating venv...\n' + separator)

            try:
                os.system('python3.10 -m venv venv')
            except Exception as e:
                raise Exception(f'Не удалось создать виртуальное окружение, ошибка - {e}')

            activate_this = 'venv/Scripts/activate_this.py'
            with open(activate_this) as f:
                code = compile(f.read(), activate_this, 'exec')
                exec(code, dict(__file__=activate_this))

            print(separator + '\nInstall requirements...\n' + separator)

            try:
                os.system('pip install -r requirements.txt')
            except Exception as e:
                raise Exception(f'Не удалось установить зависимости, ошибка - {e}')

            from loguru import logger
            print('\n\n')
            logger.success('Установка и настройка venv успешно завершена.')

        else:
            raise Exception('Ошибка версии Python, необходима версия более 3.10 !')


create_virtualenv()


def load_config() -> ConfigParser:
    """
        Загрузка конфига
    :return:
    """

    try:
        config_name = 'config.ini'

        if config_name not in os.listdir():
            config_name = os.path.join('..', config_name)

        config = ConfigParser()
        config.read(config_name)

    except Exception as e:
        logger.exception(e)
        quit(1)

    else:
        return config


def prepare_logger():
    """
        Подготовка логгера
    :return:
    """
    logger.remove()                             # удаление изначальных настроек

    logger.add(sys.stderr, level='SUCCESS')     # перегрузка вывода в консоль
    # 25 - уровень success info - 20 error - 40

    logger_init_data = {'rotation': None,
                        'compression': None}

    logger_config = config['Logger']

    if 'rotation' in logger_config:
        logger_init_data['rotation'] = logger_config['rotation']

    if 'compression' in logger_config:
        logger_init_data['compression'] = logger_config['compression']

    logger.add(config['Filenames']['logs'],     # перегрузка вывода в файл
               **logger_config)


config = load_config()
prepare_logger()


def logging(function=None, entry=True, exit=False, level="DEBUG"):
    """
        Реализация собственного декоратора для логирования
    :param function: декорируемая функция
    :param entry: логировать входные данные
    :param exit: логировать выходные данные
    :param level: уровень логирования входа и выхода
    :return:
    """
    if function is None:
        return functools.partial(logging,
                                 entry=entry,
                                 exit=exit,
                                 level=level)

    @functools.wraps(function)
    def wrapper(*args, **kwargs):

        function_name = function.__name__
        logger_ = logger.opt(depth=1)

        if entry:
            logger_.log(level, "Entering '{}' (args={}, kwargs={})", function_name, args, kwargs)

        try:
            result = function(*args, **kwargs)

        except Exception as e:
            logger.exception(e)
            return

        if exit:
            logger_.log(level, "Exiting '{}' (result={})", function_name, result)

        return result

    return wrapper


STATIC = 'static'
ICONS = path_join(STATIC, 'icons')
CSS = path_join(STATIC, 'css')
