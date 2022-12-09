import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableView, QApplication

class inf(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fon2 = QtWidgets.QLabel(self.centralwidget)
        self.fon2.setGeometry(QtCore.QRect(0, 0, 600, 700))
        self.fon2.setStyleSheet("background-color: rgb(206, 208, 90);")
        self.fon2.setText("")
        self.fon2.setObjectName("fon2")



        #self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        #self.btn5.setGeometry(QtCore.QRect(40, 600, 121, 31))
        #font = QtGui.QFont()
        #font.setPointSize(10)
        #font.setBold(True)
        #font.setWeight(75)
        #self.btn5.setFont(font)
        #self.btn5.setObjectName("btn5")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 570, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "info"))
        #self.btn5.setText(_translate("MainWindow", "НАЗАД"))
        self.pushButton_2.setText(_translate("MainWindow", "ЗАКРЫТЬ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = inf()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
