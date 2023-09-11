# coding=utf-8
# **********************************************************
# QT_002 - Библиотека PyQT5. Надписи и кнопки
# QT_004 - Всплывающие окна (QMessageBox)
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

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# КЛАСС WINDOW (наследуется от QMainWindow)
class Window(QMainWindow):
    # КОНСТРУКТОР
    def __init__(self):
        super(Window, self).__init__()  # свойства родительского класса

        # TITLE
        self.setWindowTitle("Простая программа")
        self.setGeometry(300, 250, 350, 200)
        self.new_text = QtWidgets.QLabel(self)

        # LABEL
        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Это базовая надпись")
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        # BUTTON
        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText("Нажми на меня")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)

    # МЕТОД
    def add_label(self):
        self.new_text.setText("Вторая надпись")
        self.new_text.move(100, 50)
        self.new_text.adjustSize()
        print("add")

# MAIN APPLICATION (MAIN)
def application():
    app = QApplication(sys.argv)
    window = Window()       # создать окно из класса Window
    window.show()
    sys.exit(app.exec_())

# START
if __name__ == "__main__":
    application()

# END
print("**** PYTHON 3 ****")
print('Hello World!')
