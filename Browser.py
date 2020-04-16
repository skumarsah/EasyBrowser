# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Browser.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1112, 826)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditURL = QtWidgets.QLineEdit(Dialog)
        self.lineEditURL.setObjectName("lineEditURL")
        self.gridLayout.addWidget(self.lineEditURL, 0, 1, 1, 5)
        self.pushButtonGo = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonGo.setFont(font)
        self.pushButtonGo.setDefault(True)
        self.pushButtonGo.setObjectName("pushButtonGo")
        self.gridLayout.addWidget(self.pushButtonGo, 0, 6, 1, 1)
        self.pushButtonZoomIn = QtWidgets.QPushButton(Dialog)
        self.pushButtonZoomIn.setObjectName("pushButtonZoomIn")
        self.gridLayout.addWidget(self.pushButtonZoomIn, 1, 1, 1, 1)
        self.pushButtonZoomOut = QtWidgets.QPushButton(Dialog)
        self.pushButtonZoomOut.setObjectName("pushButtonZoomOut")
        self.gridLayout.addWidget(self.pushButtonZoomOut, 1, 2, 1, 1)
        self.pushButtonBack = QtWidgets.QPushButton(Dialog)
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.gridLayout.addWidget(self.pushButtonBack, 1, 3, 1, 1)
        self.pushButtonForward = QtWidgets.QPushButton(Dialog)
        self.pushButtonForward.setObjectName("pushButtonForward")
        self.gridLayout.addWidget(self.pushButtonForward, 1, 4, 1, 1)
        self.pushButtonStop = QtWidgets.QPushButton(Dialog)
        self.pushButtonStop.setObjectName("pushButtonStop")
        self.gridLayout.addWidget(self.pushButtonStop, 1, 5, 1, 1)
        self.pushButtonReload = QtWidgets.QPushButton(Dialog)
        self.pushButtonReload.setObjectName("pushButtonReload")
        self.gridLayout.addWidget(self.pushButtonReload, 1, 6, 1, 1)
        self.widget = QWebEngineView(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.widget.setFont(font)
        self.widget.setStyleSheet("background-color: rgb(200, 194, 193);")
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 2, 0, 1, 7)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter URL"))
        self.pushButtonGo.setText(_translate("Dialog", "GO"))
        self.pushButtonZoomIn.setText(_translate("Dialog", "ZoomIn"))
        self.pushButtonZoomOut.setText(_translate("Dialog", "ZoomOut"))
        self.pushButtonBack.setText(_translate("Dialog", "Back"))
        self.pushButtonForward.setText(_translate("Dialog", "Forward"))
        self.pushButtonStop.setText(_translate("Dialog", "Stop"))
        self.pushButtonReload.setText(_translate("Dialog", "Reload"))

from PyQt5.QtWebEngineWidgets import QWebEngineView
