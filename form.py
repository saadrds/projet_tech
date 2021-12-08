# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import numpy as np
import matplotlib.pyplot as plt

lineEdit = "path"


class Ui_MainWindow(object):

    def __init__(self):
        self.fileDialog = ""
        self.u = []
        self.x = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 80, 491, 301))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 471, 281))
        self.graphicsView.setObjectName("graphicsView")
        self.upButton = QtWidgets.QPushButton(self.centralwidget)
        self.upButton.setGeometry(QtCore.QRect(40, 40, 101, 31))
        self.upButton.setObjectName("upButton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 390, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.upButton.setText(_translate("MainWindow", "Upload Data"))
        self.pushButton.setText(_translate("MainWindow", "Plot result"))

    def selectFile(self):
        dialog = QFileDialog()
        self.fileDialog = dialog.getOpenFileNames(filter="*.txt")[0][0]
        print(self.fileDialog)
        mytextFile = open(self.fileDialog, "r")
        a = mytextFile.readline()
        a = mytextFile.readline()
        count = 0
        while a:
            count +=1
            tab = a.split()
            self.x += [float(tab[0])]
            self.u += [float(tab[1])]
            a = mytextFile.readline()
        mytextFile.close()
        plt.plot(self.x,self.u)
        plt.ylabel('some numbers')
        plt.show()
        print("absices : ", self.x)
        print("vitesses : ", self.u)








if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.upButton.clicked.connect(ui.selectFile)

    sys.exit(app.exec_())