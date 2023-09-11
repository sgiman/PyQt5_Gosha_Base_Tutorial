# -*- coding: utf-8 -*-
# **********************************************************
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

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(0, 0, 300, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)

        # LABEL
        self.label_result.setFont(font)
        font = QtGui.QFont()
        self.label_result.setStyleSheet("background-color: rgb(111, 111, 111);\n" "color: rgb(255, 255, 255);\n" "")
        self.label_result.setObjectName("label_result")

        # BUTTON "0"
        self.btn_zero = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zero.setGeometry(QtCore.QRect(0, 320, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_zero.setFont(font)
        self.btn_zero.setStyleSheet("background-color: rgb(255, 170, 0);\n" "")
        self.btn_zero.setObjectName("btn_zero")

        # BUTTON "1"
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 230, 80, 90))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color: rgb(255, 170, 0);\n" "")
        self.btn_1.setObjectName("btn_1")

        # BUTTON "2"
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(80, 230, 80, 90))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color: rgb(255, 170, 0);\n" "")
        self.btn_2.setObjectName("btn_2")

        # BUTTON "3"
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(160, 230, 80, 90))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color: rgb(255, 170, 0);\n" "")
        self.btn_3.setObjectName("btn_3")

        # BUTTON "4"
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 140, 80, 90))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color: rgb(255, 170, 0);\n" "")
        self.btn_4.setObjectName("btn_4")

        # BUTTON "5"
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(80, 140, 80, 90))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color: rgb(255, 170, 0);\n" "")
        self.btn_5.setObjectName("btn_5")

        # BUTTON "6"
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(160, 140, 80, 90))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color: rgb(255, 170, 0);\n" "")
        self.btn_6.setObjectName("btn_6")

        # BUTTON "7"
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 50, 80, 90))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("background-color: rgb(255, 170, 0);\n" "")
        self.btn_7.setObjectName("btn_7")

        # BUTTON "8"
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(80, 50, 80, 90))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color: rgb(255, 170, 0);\n" "")
        self.btn_8.setObjectName("btn_8")

        # BUTTON "9"
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(160, 50, 80, 90))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color: rgb(255, 170, 0);\n" "")
        self.btn_9.setObjectName("btn_9")

        # BUTTON "="
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equal.setGeometry(QtCore.QRect(80, 320, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet("background-color: rgb(255, 112, 16);")
        self.btn_equal.setObjectName("btn_equal")

        # BUTTON "CLEAR" ("C")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(160, 320, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_clear.setObjectName("btn_clear")

        # BUTTON "+"
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(240, 50, 60, 90))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("background-color: rgb(255, 170, 0);\n" "")
        self.btn_plus.setObjectName("btn_plus")

        # BUTTON "-"
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(240, 140, 60, 90))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet("background-color: rgb(255, 170, 0);\n" "")
        self.btn_minus.setObjectName("btn_minus")

        # BUTTON "*"
        self.btn_mult = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mult.setGeometry(QtCore.QRect(240, 230, 60, 90))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_mult.setFont(font)
        self.btn_mult.setStyleSheet("background-color: rgb(255, 170, 0);\n" "")
        self.btn_mult.setObjectName("btn_mult")

        # BUTTON "/"
        self.btn_divide = QtWidgets.QPushButton(self.centralwidget)
        self.btn_divide.setGeometry(QtCore.QRect(240, 320, 60, 80))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_divide.setFont(font)
        self.btn_divide.setStyleSheet("background-color: rgb(255, 170, 0);\n" "")
        self.btn_divide.setObjectName("btn_divide")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()    # добавленный метод для обработчика событий

        self.is_equal = False   # флаг операции

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор "))
        self.label_result.setText(_translate("MainWindow", "0"))
        self.btn_zero.setText(_translate("MainWindow", "0"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_mult.setText(_translate("MainWindow", "*"))
        self.btn_divide.setText(_translate("MainWindow", "/"))
        self.btn_clear.setText(_translate("MainWindow", "C"))

    # Обработчик событий (нажатие кнопок)
    def add_functions(self):
        self.btn_zero.clicked.connect(lambda: self.write_number(self.btn_zero.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.btn_plus.clicked.connect(lambda: self.write_number(self.btn_plus.text()))
        self.btn_minus.clicked.connect(lambda: self.write_number(self.btn_minus.text()))
        self.btn_mult.clicked.connect(lambda: self.write_number(self.btn_mult.text()))
        self.btn_divide.clicked.connect(lambda: self.write_number(self.btn_divide.text()))

        self.btn_equal.clicked.connect(self.results)
        self.btn_clear.clicked.connect(self.clear)

    # OUTPUT
    def write_number(self, number):
        if self.label_result.text() == "0" or self.is_equal:                # игнорировать
            self.label_result.setText(number)                               # только число или операнд
            self.is_equal = False                                           # сброс операции
        else:
            self.label_result.setText(self.label_result.text() + number)    # добавить цифру/операнд
        #print(number)

    # CLEAR
    def clear(self):
        self.label_result.setText("")
        self.is_equal = False

    # RESULT
    def results(self):
        if not self.is_equal and self.label_result.text() != "":
            res = eval(self.label_result.text())
            self.label_result.setText("Результат: " + str(res))
            self.is_equal = True                                            # операция выполнена
        else:
            error = QMessageBox()                                           # всплывающее окно
            error.setWindowTitle("Ошибка")                                  # заголовок
            error.setText("Сейчас это действие выполнить нельзя")           # текст
            error.setIcon(QMessageBox.Warning)                              # иконка

            error.setStandardButtons(QMessageBox.Reset | QMessageBox.Cancel | QMessageBox.Ok)   # кнопки
            error.setDefaultButton(QMessageBox.Ok)                          # подсвеченная кнопка по умолчанию

            error.setInformativeText("Два раза действие не выполнить")      # INFO
            error.setDetailedText("Детали")                                 # детально

            error.buttonClicked.connect(self.popup_action)                  # buttons for POPUP actions

            error.exec_()                                                   # выполнить

    # OK, RESET
    def popup_action(self, btn):
        if btn.text() == "Ok":
            print("Print OK")
        elif btn.text() == "Reset":
            self.label_result.setText("")
            self.is_equal = False


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
