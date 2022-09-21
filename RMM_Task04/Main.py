#!/usr/bin/env python3
# coding=utf-8

import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)  # загрузка формы в py-скрипт

        self.setWindowTitle('Работа с визуальными табличными данными в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)

    def fill_random_numbers(self):
        """
        заполняем таблицу случайными числами
        :return:
        """
        row = 0
        col = 0

        # заполняем таблицу случайными числами
        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                random_num = randint(-101, 101)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                item = self.tableWidget.item(row, col).text()
                col += 1
            row += 1
            col = 0

        # находим максимальное число и его координаты
        # [0] - максимальное число, [1] - строка максимума, [2] - столбец максимума
        list_information_max_num = find_max(self.tableWidget)

        if not list_information_max_num:
            self.label_error.setText('Введены неправильные данные!')
        else:
            # выводим на кэран информацию о расположении максимального числа
            self.label_max_el.setText(
                'Максимальный элемент: ' + str(list_information_max_num[0]) + ' [' +
                str(list_information_max_num[1]) + ';' + str(list_information_max_num[2]) + ']')

    def solve(self):
        list_information_max_num = find_max(self.tableWidget)
        list_information_min_nim = find_min(self.tableWidget)
        negativeNumber = countNegative(self.tableWidget)
        maxRow = int(list_information_max_num.__getitem__(1))
        maxCol = int(list_information_max_num.__getitem__(2))
        minRow = int(list_information_min_nim.__getitem__(1))
        minCol = int(list_information_min_nim.__getitem__(2))
        valueMax = int(list_information_max_num.__getitem__(0))
        valueMin = int(list_information_min_nim.__getitem__(0))


        self.tableWidget.setItem(maxRow, maxCol, QTableWidgetItem(str(valueMax+negativeNumber)))
        self.tableWidget.setItem(minRow, minCol, QTableWidgetItem(str(valueMin+negativeNumber)))


        self.label_error.setText('')


def find_max(table_widget):
    """
    находим максимальное число из таблицы и его координаты
    :param table_widget: таблица
    :return: [max_num, row_max_number, col_max_number], если выкинуто исключение,
            то None
    """

    row_max_number = 0  # номер строки, в котором находится максимальне число
    col_max_number = 0  # номер столбца, в котором находится максимальне число
    max_num = int(table_widget.item(row_max_number, col_max_number).text())  # Максимальное значение

    row = 0
    col = 0

    try:
        while row < table_widget.rowCount():
            while col < table_widget.columnCount():
                number = int(table_widget.item(row, col).text())
                if number > max_num:
                    max_num = number
                    row_max_number = row
                    col_max_number = col
                col += 1
            row += 1
            col = 0
        return [max_num, row_max_number, col_max_number]
    except Exception:
        return None
def find_min(table_widget):
    """
    находим максимальное число из таблицы и его координаты
    :param table_widget: таблица
    :return: [max_num, row_max_number, col_max_number], если выкинуто исключение,
            то None
    """

    row_min_number = 0  # номер строки, в котором находится максимальне число
    col_min_number = 0  # номер столбца, в котором находится максимальне число
    min_num = int(table_widget.item(row_min_number, col_min_number).text())  # Максимальное значение

    row = 0
    col = 0

    try:
        while row < table_widget.rowCount():
            while col < table_widget.columnCount():
                number = int(table_widget.item(row, col).text())
                if number < min_num:
                    min_num = number
                    row_min_number = row
                    col_min_number = col
                col += 1
            row += 1
            col = 0
        return [min_num, row_min_number, col_min_number]
    except Exception:
        return None
def countNegative(table_widget):

    row = 0
    col = 0
    NegativeCount = 0
    while row < table_widget.rowCount():
        while col < table_widget.columnCount():
            number = float(table_widget.item(row, col).text())
            if number < 0:
                NegativeCount=NegativeCount+1
            col+=1
        row+=1
        col=0
    return NegativeCount






def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
