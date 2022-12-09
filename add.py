import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase
from PyQt5.QtWidgets import QTableView


class adds(QtWidgets.QMainWindow):

    def signup(self):
        locality = self.lineEdit.text()
        condition = self.lineEdit_2.text()
        temp = self.lineEdit_3.text()
        wet = self.lineEdit_4.text()
        wind = self.lineEdit_5.text()
        humidity = self.lineEdit_6.text()
        day = self.dateEdit.text()
        #conn = QSqlDatabase.addDatabase('QSQLITE')
        #conn = sqlite3.connect('sql.sqlite')
        conn = sqlite3.connect('sql.sqlite')
        conn.execute("CREATE TABLE IF NOT EXISTS signup(locality TEXT,day TEXT,condition TEXT,temp TEXT, wet TEXT, wind TEXT, humidity TEXT)")
        cur = conn.cursor()
        sql = "insert into signup(locality,day,condition,temp,wet,wind,humidity) values(?,?,?,?,?,?,?)"
        data = cur.execute(sql,(locality, day, condition, temp, wet, wind, humidity))
        if data:
            print("Успешно добавлено!")
        conn.commit()
        conn.close()



    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 600, 700))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(195, 165, 174);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 110, 271, 31))
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        #self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 80, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 140, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(160, 170, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 200, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 230, 151, 31))
        self.lineEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        #self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 260, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 290, 151, 31))
        self.lineEdit_3.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        #self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 320, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 350, 151, 31))
        self.lineEdit_4.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        #self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 380, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 410, 151, 31))
        self.lineEdit_5.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        #self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(160, 440, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(160, 470, 151, 31))
        self.lineEdit_6.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        #self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 570, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 222, 230);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.signup)
        # self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_2.setGeometry(QtCore.QRect(210, 620, 131, 31))
        # font = QtGui.QFont()
        # font.setBold(True)
        # font.setWeight(75)
        # self.pushButton_2.setFont(font)
        # self.pushButton_2.setStyleSheet("background-color: rgb(255, 222, 230);")
        # self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add"))
        self.label_2.setText(_translate("MainWindow", "НАСЕЛЁННЫЙ ПУНКТ:"))
        self.label_3.setText(_translate("MainWindow", "ДЕНЬ:"))
        self.label_4.setText(_translate("MainWindow", "СТАТУС:"))
        self.label_5.setText(_translate("MainWindow", "ТЕМПЕРАТУРА:"))
        self.label_6.setText(_translate("MainWindow", "ВЛАЖНОСТЬ ВОЗДУХА:"))
        self.label_7.setText(_translate("MainWindow", "ВЕТЕР:"))
        self.label_8.setText(_translate("MainWindow", "ДАВЛЕНИЕ:"))
        self.pushButton.setText(_translate("MainWindow", "ДОБАВИТЬ"))
        # self.pushButton_2.setText(_translate("MainWindow", "НАЗАД"))







if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = adds()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
