"""
    Стартовая точка запуска графического интерфейса
"""

import sys
import os
from PySide6.QtWidgets import QApplication, QPushButton

from general_config import config
from gui.services import files
from widget import Widget


class ExpandedWidget(Widget):
    def __init__(self):
        super().__init__()
        self.get_need_widgets()
        self.set_handlers()

    def get_need_widgets(self):
        """
            Связка элементов UI с элементами Языка программирования
        :return:
        """
        self.button_logs = self.findChild(QPushButton, 'pushButton')

    def set_handlers(self):
        """
            Настройка всех хендлеров на кнопках
        :return:
        """
        self.button_logs.clicked.connect(self.handler_logs_button)

    def handler_logs_button(self):
        """
            Обработка лог кнопки, вывод текстового файла с логами через средства ОС
        :return:
        """
        files.open_file(filename=config['Filenames']['logs'])


def start_gui():
    app = QApplication([])
    widget = ExpandedWidget()
    widget.show()
    sys.exit(app.exec_())
