"""
    Общий конфиг, тут хранятся токены, и прочее, то, что не должно быть на гите
"""

import functools
from configparser import ConfigParser
from loguru import logger


config = ConfigParser()
config.read('config.ini')
logger.add(config['Filenames']['logs'])


def logging(*, entry=True, exit=True, level="DEBUG"):
    """
        Реализация собственного декоратора для логирования
    :param entry: логировать входные данные
    :param exit: логировать выходные данные
    :param level: уровень логирования входа и выхода
    :return:
    """

    def wrapper(func):
        name = func.__name__

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            logger_ = logger.opt(depth=1)
            if entry:
                logger_.log(level, "Entering '{}' (args={}, kwargs={})", name, args, kwargs)

            result = func(*args, **kwargs)
            if exit:
                logger_.log(level, "Exiting '{}' (result={})", name, result)
            return result

        return wrapped

    return wrapper
