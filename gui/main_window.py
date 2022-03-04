"""
    Стартовая точка запуска графического интерфейса
"""
import os.path
import sys

from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QPushButton, QLayout, QLabel, QHBoxLayout

from general_config import config, logging, CSS, path_join
from gui.gui_widgets.body import Body
from gui.gui_widgets.footer import Footer
from gui.services import files
from widget import Widget


class ExpandedWidget(Widget,
                     Footer,
                     Body):
    """
        Расширение основого окна, работа с виджетами в данном классе
    """
    standart_css: str = 'main.css'

    def __init__(self):
        super().__init__()
        self.initial_operations()

    @logging
    def set_styles(self):
        path_to_css = path_join(CSS, self.standart_css)
        if os.path.exists(path_to_css):
            with open(path_to_css, 'r') as file:
                self.setStyleSheet(file.read())

    @logging
    def initial_operations(self):
        """
            Первоначальные операции после инициализации окна
        :return:
        """
        self.setWindowTitle(config['App Settings']['title'])
        self.setFixedSize(800, 600)
        self.set_styles()

        self.get_need_widgets()
        self.set_handlers()

        self.load_city()
        self.output_api_data()

    @logging
    def get_need_widgets(self):
        """
            Связка элементов UI с элементами Языка программирования
        :return:
        """
        self.button_logs: QPushButton = self.findChild(QPushButton, 'pushButton')
        self.button_config: QPushButton = self.findChild(QPushButton, 'pushButton_2')
        self.label_city: QLabel = self.findChild(QLabel, 'label_2')

        self.layout_with_data_columns: QHBoxLayout = self.findChild(QLayout, 'horizontalLayout')

    @logging
    def set_handlers(self):
        """
            Настройка всех хендлеров на кнопках
        :return:
        """
        self.button_logs.clicked.connect(self.handler_logs_button)
        self.button_config.clicked.connect(self.handler_config_button)


def start_gui():
    app = QApplication([])
    widget = ExpandedWidget()
    widget.show()
    sys.exit(app.exec_())
