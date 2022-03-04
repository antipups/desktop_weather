"""
    Описывание виджета футера (нижней панели в программе)
"""
from PySide6.QtWidgets import QLabel
from loguru import logger

from general_config import config, logging
from gui.services import files


class Footer:

    @logging
    def handler_logs_button(self):
        """
            Обработка лог кнопки, вывод текстового файла с логами через средства ОС
        :return:
        """
        files.open_file(filename=config['Filenames']['logs'])

    @logging
    def handler_config_button(self):
        """
            Обработка конфиг кнопки, вывод текстового файла с логами через средства ОС
        :return:
        """
        files.open_file(filename=config['Filenames']['config'])

    @logging
    def load_city(self):
        """
            Загрузка города в GUI из конфига
        :return:
        """
        self.label_city.setText(config['Weather Api Settings']['primary_city'])
