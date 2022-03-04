"""
    Описание основного пространства в интерфейсе
"""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from loguru import logger

from general_config import logging
from gui.services.api_data_handler import DataHandler


class Body:
    data_handler: DataHandler = None
    layout_with_data_columns: QHBoxLayout

    def include_data_in_gui(self):
        for layout, data_day in zip(self.layout_with_data_columns.children(),
                                    self.data_handler.data_to_gui):

            datetime_widget: QLabel = layout.itemAt(0).wid
            icon_widget: QLabel = layout.itemAt(1).wid
            title_widget: QLabel = layout.itemAt(2).wid
            description_widget: QLabel = layout.itemAt(3).wid

            datetime_widget.setText(data_day.date.strftime('%d-%m-%Y'))
            icon_widget.setPixmap(QPixmap(data_day.icon))
            title_widget.setText(data_day.title)
            description_widget.setText(data_day.description)

    @logging
    def output_api_data(self):
        """
            Получение данных из модуля обработки данных из апи
        :return:
        """
        self.data_handler = DataHandler()
        self.include_data_in_gui()
