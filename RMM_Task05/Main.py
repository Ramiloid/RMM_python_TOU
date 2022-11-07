#!/usr/bin/env python3
# coding=utf-8

import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi




class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)
        self.processed_data=[]
        self.setWindowTitle('Работа с массивами и файлами в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_upload_data.clicked.connect(self.upload_data_from_file)
        self.btn_process_data.clicked.connect(self.process_data)
        self.btn_save_data.clicked.connect(self.save_data_in_file)
        self.btn_clear.clicked.connect(self.clear)

    def upload_data_from_file(self):
        """
        загружаем данные из файла
        :return: pass
        """
        global path_to_file
        path_to_file = QFileDialog.getOpenFileName(self, 'Открыть файл', '', "Text Files (*.txt)")[0]

        if path_to_file:
            file = open(path_to_file, 'r')

            data = file.read()
            self.processed_data = [[int(i)
                                    for i in line.split()]
                                    for line in data.splitlines()]
            # выводим считанные данные на экран
            self.plainTextEdit.appendPlainText("Полученные данные: \n" + data + "\n")

    def process_data(self):
        if not self.processed_data:
            raise Exception("Oshibka")

        if(self.processed_data[2].count(1) == len(self.processed_data[2])):

            a=max(range(len(self.processed_data)), key=lambda x: self.processed_data[x][0])
            self.processed_data[a][0]*=2

            b=max(range(len(self.processed_data)), key=lambda x: self.processed_data[x][1])
            self.processed_data[b][1]*=3
            print(self.processed_data)
        else:
            print(self.processed_data)

    def save_data_in_file(self):
        """
        сохраняем данные в выбранный нами файл
        :return:
        """

        if path_to_file:
            file = open(path_to_file.split(".")[0] + '-Output.txt', 'w')
            print(self.processed_data)
            lines = [' '.join(str(i) for i in row) for row in self.processed_data]
            print(lines)
            for line in lines:
                file.write(line)
                file.write("\n")
            file.close()

            self.plainTextEdit.appendPlainText("Файл был успешно загружен! \n")
        else:
            self.plainTextEdit.appendPlainText("Для начала загрузите файл!")

    def clear(self):
        self.plainTextEdit.clear()


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
