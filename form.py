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
from scipy import signal

lineEdit = "path"


class Ui_MainWindow(object):

    def __init__(self):
        self.fileDialog = ""
        self.u = []
        self.x = []
        self.xtotal = []
        self.c = []
        self.T = 0
        self.points = 0
        self.signaux = []
        self.moyenne = []
        self.fft = []
        self.size = 0

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
            count += 1
            tab = a.split()
            self.x += [float(tab[0])]
            self.u += [float(tab[1])]
            a = mytextFile.readline()
        mytextFile.close()
        negative_x = [element * -1 for element in self.x[1:]]
        negative_x.sort()
        self.xtotal = negative_x + self.x
        print("total x ", len(self.xtotal))
        plt.plot(self.x, self.u)
        plt.ylabel('some numbers')
        plt.show()
        #print("absices : ", self.xtotal)
        #print("vitesses : ", self.u)

    def correlation(self):
        self.size = len(self.x)
        #self.c = np.zeros(size*2-1)
        #print("heello", self.size)
        #size = size//640
        """"
        for i in range(0,size): #i = 7
            sum = 0
            for j in range(size): #j = 0
                if size > j - i >= 0:
                    sum += self.u[j] * self.u[j - i]

            self.c[i+size-1] = sum
        """
        self.c = np.correlate(self.u,self.u,'same')

        print(self.c)
        #plt.plot(self.c)
        signal_carre = np.copy(self.c)
        signal_carre[np.where([self.c > 0][0])] = 1
        signal_carre[np.where([self.c < 0][0])] = -1
        diff = np.diff(signal_carre)
        #plt.plot(diff)
        idx = np.where([diff>0][0])

        self.T = self.x[idx[0][2]] - self.x[idx[0][1]]
        self.points = idx[0][2] - idx[0][1]
        #plt.ylabel('some numbers')
        #plt.show()
        #
        """"
        var = 0
        cond = 0
        cond1 = 0
        cond2 = 0
       
        for k in range(size-1, size*2 - 1):
            if self.c[k] < 0 and (var == 0 or var == 2):
                if cond == 0 :
                    cond1 = k - 1
                    cond = 1
                var += 1
                if var == 1:
                    t1 = self.xtotal[k-1]
                if var == 3:
                    t2 = self.xtotal[k-1]
                    cond2 = k-1
                    break
            if self.c[k] > 0 and var == 1:
                var += 1

        self.points = cond2 - cond1 + 1

        self.T = t2 - t1
        """


        print("T : ", self.T)
        print("nb Points : ", self.points)
        #print("absices : ", self.xtotal)
        #print("vitesses : ", self.c)
        self.waves()

    def correlation_2(self):
        self.size = len(self.x)
        # self.c = np.zeros(size*2-1)
        # size = size//640
        """"
        for i in range(0,size): #i = 7
            sum = 0
            for j in range(size): #j = 0
                if size > j - i >= 0:
                    sum += self.u[j] * self.u[j - i]

            self.c[i+size-1] = sum
        """
        self.c = signal.correlate(self.u,self.u)

        print(self.c)
        # plt.plot(self.c)
        signal_carre = np.copy(self.c)
        signal_carre[np.where([self.c > 0][0])] = 1
        signal_carre[np.where([self.c < 0][0])] = -1
        diff = np.diff(signal_carre)
        # plt.plot(diff)
        idx = np.where([diff > 0][0])
        idx_diff = np.diff(idx)
        midx = np.mean(idx_diff)
        print('periode = {}'.format(midx))
        self.T = self.x[int(np.round(midx))]
        #self.T = self.x[idx[0][2]] - self.x[idx[0][1]]
        self.points = int(np.round(midx))
        # plt.ylabel('some numbers')
        # plt.show()
        #
        """"
        var = 0
        cond = 0
        cond1 = 0
        cond2 = 0

        for k in range(size-1, size*2 - 1):
            if self.c[k] < 0 and (var == 0 or var == 2):
                if cond == 0 :
                    cond1 = k - 1
                    cond = 1
                var += 1
                if var == 1:
                    t1 = self.xtotal[k-1]
                if var == 3:
                    t2 = self.xtotal[k-1]
                    cond2 = k-1
                    break
            if self.c[k] > 0 and var == 1:
                var += 1

        self.points = cond2 - cond1 + 1

        self.T = t2 - t1
        """

        print("T : ", self.T)
        print("nb Points : ", self.points)
        # print("absices : ", self.xtotal)
        # print("vitesses : ", self.c)
        self.waves()

    def waves(self):
        k = -1
        ligne = len(self.x) // self.points
        self.signaux = np.zeros((ligne, self.points))
        for i in range(ligne):
            for j in range(self.points):
                k += 1
                self.signaux[i][j] = self.u[k]
        """fig, axs = plt.subplots(3, 2)
        index_s = 0
        for i in range(2):
            for j in range(2):
                index_s += 1
                if i== 1 and j == 1 :
                    axs[i, j].plot(self.x[0:self.points], self.signaux[index_s])
                else :
                    axs[i, j].plot(self.x[0:self.points], self.signaux[403])
        """
        self.moyenne = np.zeros(self.points)
        for i in range(self.points):
            somme = 0
            for j in range(ligne):
                somme += self.signaux[j][i]
            self.moyenne[i] = somme
        #axs[2,0].plot(self.x[0:self.points], self.moyenne)
        #plt.show()
        self.fft = np.fft.fft(self.u)
        fe = 1 / (self.x[1] - self.x[0])
        self.f_tab = np.arange(0, fe, fe/self.size)
        plt.plot(self.f_tab[0:int(self.size/2)], np.abs(self.fft[0:int(self.size/2)]))
        plt.show()
        #print(self.moyenne)



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.upButton.clicked.connect(ui.selectFile)
    ui.pushButton.clicked.connect(ui.correlation_2)

    sys.exit(app.exec_())
