# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glavnaya.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fon = QtWidgets.QLabel(self.centralwidget)
        self.fon.setGeometry(QtCore.QRect(0, 0, 600, 700))
        self.fon.setStyleSheet("background-color: rgb(170, 172, 255);")
        self.fon.setText("")
        self.fon.setObjectName("fon")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(230, 460, 141, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn2.setFont(font)
        self.btn2.setStyleSheet("background-color: rgb(219, 215, 255);\n"
"")
        self.btn2.setObjectName("btn2")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(230, 390, 141, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn1.setFont(font)
        self.btn1.setStyleSheet("background-color: rgb(219, 215, 255);\n"
"")
        self.btn1.setObjectName("btn1")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главное меню"))
        self.btn2.setText(_translate("MainWindow", "БАЗА НАС.ПУНКТОВ"))
        self.btn1.setText(_translate("MainWindow", "ПРОГНОЗ ПОГОДЫ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())