"""
    Описание работы с локальными файлами
"""
import subprocess
import sys


def open_file(filename: str):
    """
        Открытие файла через систему
    :param filename: название файла
    :return:
    """
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, filename])
