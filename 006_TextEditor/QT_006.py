# coding=utf-8
# **********************************************************
# QT_005 -  Создание простого текстового редактора
# ----------------------------------------------------------
# Python 3.11
# jetBrain PyCharm 2023.1
# Designer 5.14 (Qt)
# ----------------------------------------------------------
# pip install pyqt5
# pip install pyqt5-tools
# pyuic5 -x app.ui -o app.py
# **********************************************************
# Gosha Dudar, 2023
# Writing sgiman, 2023
#
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog

import sys

class Window(QMainWindow):
    # КОНСТРУКТОР (инициализация)
    def __init__(self):
        super(Window, self).__init__()                  # инициализировать системные параметры
        self.setWindowTitle("Редактор кода")            # заголовок
        self.setGeometry(300, 250, 350, 200)            # геометрия

        self.text_edit = QtWidgets.QTextEdit(self)      # виджет редактора текста
        self.setCentralWidget(self.text_edit)           # растянуть на всё окно по центру
        self.createMenuBar()                            # Cоздать меню

    # MENU
    def createMenuBar(self):
        self.menuBar = QMenuBar(self)       # menubar
        self.setMenuBar(self.menuBar)       # установить menubar

        fileMenu = QMenu("&Файл", self)     # элемент меню "Файл"
        self.menuBar.addMenu(fileMenu)      # добавить элемент меню "Файл"

        #open_file = fileMenu.addMenu("Открыть")
        #save_file = fileMenu.addMenu("Сохранить")
        fileMenu.addAction("Открыть", self.action_clicked)
        fileMenu.addAction("Сохранить", self.action_clicked)

    # ОБРАБОТКА КЛИКОВ
    @QtCore.pyqtSlot()                                          # аннотация для обработки кликов на пункты меню
    def action_clicked(self):
        action = self.sender()                                  # получить информацию от клика на пункт меню
        if action.text() == "Открыть":
            fname = QFileDialog.getOpenFileName(self)[0]        # окрыть только 1-й выбранный файл
            try:
                f = open(fname, 'r')                            # открыть для чтения
                with f:
                    data = f.read()
                    self.text_edit.setText(data)
            except FileNotFoundError:                           # ошибка
                print("No such file")
        elif action.text() == "Сохранить":
            fname = QFileDialog.getSaveFileName(self)[0]
            try:
                f = open(fname, 'w')                            # открыть для записи
                text = self.text_edit.toPlainText()             # введённый текст
                f.write(text)                                   # записать файл
                f.close()                                       # закрыть
            except FileNotFoundError:                           # ошибка
                print("No such file")


# ПРИЛОЖЕНИЕ (редактор текста)
def application():
    app = QApplication(sys.argv)            # передать настройки системы компьютера
    window = Window()                       # создать новое окно из класса Window
    window.show()                           # отобразить окно
    sys.exit(app.exec_())                   # выход

# ЗАПУСК
print("***** PYTHON 3, QT5 *****")
print('Designer 5.14 (Qt)')
if __name__ == "__main__":
    application()

