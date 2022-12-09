import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase
from PyQt5.QtWidgets import QTableView, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QCalendarWidget, QLabel, QApplication)
from PyQt5.QtCore import QDate


class prognoze(QtWidgets.QMainWindow):

    def signup(self):
        self.okno2 = inf1()
        self.okno2.show()

        locality = self.vvodc.text()
        #day = self.calendar.selectedDate()
        day = self.dateEdit.text()
        #day = self.vvodd.text()
        conn = sqlite3.connect('sql.sqlite')
        cur = conn.cursor()
        sql = cur.execute(""" insert into res select * from signup  where locality=? and day=?""", (locality, day))
        #conn.execute("CREATE TABLE IF NOT EXISTS signup2(locality TEXT,day TEXT,condition TEXT,temp TEXT, wet TEXT, wind TEXT, humidity TEXT)")
        #sql1 = "insert into signup2(locality,day,condition,temp,wet,wind,humidity) values(?,?,?,?,?,?,?)"
        #data = cur.execute(sql1,sql, (locality, day))
        for elem in sql:
            print(elem)

            #if elem in sql:
                #print("Успешно добавлено!")



        conn.commit()
        conn.close()






    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fon1 = QtWidgets.QLabel(self.centralwidget)
        self.fon1.setGeometry(QtCore.QRect(0, 0, 600, 700))
        self.fon1.setStyleSheet("background-color: rgb(255, 237, 161);")
        self.fon1.setText("")
        self.fon1.setObjectName("fon1")

        self.vvodc = QtWidgets.QLineEdit(self.centralwidget)
        self.vvodc.setGeometry(QtCore.QRect(200, 110, 200, 35))
        self.vvodc.setObjectName("vvodc")

        self.city = QtWidgets.QLabel(self.centralwidget)
        self.city.setGeometry(QtCore.QRect(200, 80, 200, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.city.setFont(font)
        self.city.setObjectName("city")

        self.data = QtWidgets.QLabel(self.centralwidget)
        self.data.setGeometry(QtCore.QRect(200, 190, 200, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.data.setFont(font)
        self.data.setObjectName("data")

        #self.vvodd = QtWidgets.QLineEdit(self.centralwidget)
        #self.vvodd.setGeometry(QtCore.QRect(200, 220, 200, 35))
        #self.vvodd.setObjectName("vvodd")

        #self.calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        #self.calendar.setGeometry(QtCore.QRect(120, 300, 392, 236))
        #self.calendar.setObjectName("calendar")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate.currentDate())

        self.dateEdit.setGeometry(QtCore.QRect(200, 220, 200, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")



        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(80, 600, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.btn3.clicked.connect(self.signup)

        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(350, 600, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.btn4.clicked.connect(self.signup)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ПРОГНОЗ ПОГОДЫ"))
        self.city.setText(_translate("MainWindow", "НАСЕЛЁННЫЙ ПУНКТ:"))
        self.data.setText(_translate("MainWindow", "ДАТА:"))
        self.btn3.setText(_translate("MainWindow", "ЗАПРОС"))
        self.btn4.setText(_translate("MainWindow", "НАЙТИ"))


class inf1(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        import info
        self.win = info.inf()
        self.win.setupUi(self)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('sql.sqlite')
        self.db.open()
        self.view = QTableView(self)
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('res')
        self.model.select()

        self.view.setModel(self.model)
        self.view.move(10, 10)
        self.view.resize(580, 315)

        self.setGeometry(300, 100, 600, 700)
        self.setWindowTitle('БАЗА')



        #self.connection = sqlite3.connect("sql.sqlite")
        #self.textEdit.setPlainText("SELECT * FROM signup")
        #self.select_data()

    #def select_data(self):
        #query = self.textEdit.toPlainText()
        #res = self.connection.cursor().execute(query).fetchall()
        #self.tableWidget.setColumnCount(5)
        #self.tableWidget.setRowCount(0)
        #for i, row in enumerate(res):
            #self.tableWidget.setRowCount(
                #self.tableWidget.rowCount() + 1)
        #for j, elem in enumerate(row):
            #self.tableWidget.setItem(
                #i, j, QTableWidgetItem(str(elem)))
        #def closeEvent(self, event):
            #self.connection.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = prognoze()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
