﻿# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uishop.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WindowShop(object):
    def setupUi(self, WindowShop):
        WindowShop.setObjectName("WindowShop")
        WindowShop.resize(203, 357)
        self.groupBox = QtWidgets.QGroupBox(WindowShop)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 211, 361))
        self.groupBox.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.groupBox.setObjectName("groupBox")
        self.cost_4 = QtWidgets.QLabel(self.groupBox)
        self.cost_4.setGeometry(QtCore.QRect(130, 140, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.cost_4.setFont(font)
        self.cost_4.setObjectName("cost_4")
        self.cost_3 = QtWidgets.QLabel(self.groupBox)
        self.cost_3.setGeometry(QtCore.QRect(130, 100, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.cost_3.setFont(font)
        self.cost_3.setObjectName("cost_3")
        self.cost_1 = QtWidgets.QLabel(self.groupBox)
        self.cost_1.setGeometry(QtCore.QRect(130, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.cost_1.setFont(font)
        self.cost_1.setObjectName("cost_1")
        self.cost_2 = QtWidgets.QLabel(self.groupBox)
        self.cost_2.setGeometry(QtCore.QRect(130, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.cost_2.setFont(font)
        self.cost_2.setObjectName("cost_2")
        self.cost_8 = QtWidgets.QLabel(self.groupBox)
        self.cost_8.setGeometry(QtCore.QRect(130, 320, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.cost_8.setFont(font)
        self.cost_8.setObjectName("label_9")
        self.cost_5 = QtWidgets.QLabel(self.groupBox)
        self.cost_5.setGeometry(QtCore.QRect(130, 200, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.cost_5.setFont(font)
        self.cost_5.setObjectName("cost_5")
        self.cost_7 = QtWidgets.QLabel(self.groupBox)
        self.cost_7.setGeometry(QtCore.QRect(130, 280, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.cost_7.setFont(font)
        self.cost_7.setObjectName("cost_7")
        self.cost_6 = QtWidgets.QLabel(self.groupBox)
        self.cost_6.setGeometry(QtCore.QRect(130, 240, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.cost_6.setFont(font)
        self.cost_6.setObjectName("cost_6")
        self.clickboost_2 = QtWidgets.QPushButton(WindowShop)
        self.clickboost_2.setGeometry(QtCore.QRect(10, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.clickboost_2.setFont(font)
        self.clickboost_2.setObjectName("clickboost_2")
        self.clickboost_3 = QtWidgets.QPushButton(WindowShop)
        self.clickboost_3.setGeometry(QtCore.QRect(10, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.clickboost_3.setFont(font)
        self.clickboost_3.setObjectName("clickboost_3")
        self.clickboost_4 = QtWidgets.QPushButton(WindowShop)
        self.clickboost_4.setGeometry(QtCore.QRect(10, 140, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.clickboost_4.setFont(font)
        self.clickboost_4.setObjectName("clickboost_4")
        self.autoclick_1 = QtWidgets.QPushButton(WindowShop)
        self.autoclick_1.setGeometry(QtCore.QRect(10, 200, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.autoclick_1.setFont(font)
        self.autoclick_1.setObjectName("autoclick_1")
        self.autoclick_2 = QtWidgets.QPushButton(WindowShop)
        self.autoclick_2.setGeometry(QtCore.QRect(10, 240, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.autoclick_2.setFont(font)
        self.autoclick_2.setObjectName("autoclick_2")
        self.autoclick_3 = QtWidgets.QPushButton(WindowShop)
        self.autoclick_3.setGeometry(QtCore.QRect(10, 280, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.autoclick_3.setFont(font)
        self.autoclick_3.setObjectName("autoclick_3")
        self.autoclick_4 = QtWidgets.QPushButton(WindowShop)
        self.autoclick_4.setGeometry(QtCore.QRect(10, 320, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.autoclick_4.setFont(font)
        self.autoclick_4.setObjectName("autoclick_4")
        self.clickboost_1 = QtWidgets.QPushButton(WindowShop)
        self.clickboost_1.setGeometry(QtCore.QRect(10, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.clickboost_1.setFont(font)
        self.clickboost_1.setObjectName("clickboost_1")

        self.retranslateUi(WindowShop)
        QtCore.QMetaObject.connectSlotsByName(WindowShop)

    def retranslateUi(self, WindowShop):
        _translate = QtCore.QCoreApplication.translate
        WindowShop.setWindowTitle(_translate("WindowShop", "Shop"))
        self.groupBox.setTitle(_translate("WindowShop", "магазин"))
        self.cost_4.setText(_translate("WindowShop", "25"))
        self.cost_3.setText(_translate("WindowShop", "5"))
        self.cost_1.setText(_translate("WindowShop", "0,01"))
        self.cost_2.setText(_translate("WindowShop", "0,1"))
        self.cost_8.setText(_translate("WindowShop", "20"))
        self.cost_5.setText(_translate("WindowShop", "0,1"))
        self.cost_7.setText(_translate("WindowShop", "5"))
        self.cost_6.setText(_translate("WindowShop", "1"))
        self.clickboost_2.setText(_translate("WindowShop", "Клик +"))
        self.clickboost_3.setText(_translate("WindowShop", "Супер клик"))
        self.clickboost_4.setText(_translate("WindowShop", "Кликер"))
        self.autoclick_1.setText(_translate("WindowShop", "Автоклик"))
        self.autoclick_2.setText(_translate("WindowShop", "Авоклик +"))
        self.autoclick_3.setText(_translate("WindowShop", "Супер автоклик"))
        self.autoclick_4.setText(_translate("WindowShop", "Автокликер"))
        self.clickboost_1.setText(_translate("WindowShop", "Клик"))
