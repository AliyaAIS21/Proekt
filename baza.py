from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import sys
from PyQt5 import QtCore, QtWidgets, QtCore, QtGui
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableView, QApplication


class base(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fon3 = QtWidgets.QLabel(self.centralwidget)
        self.fon3.setGeometry(QtCore.QRect(0, 0, 600, 700))
        self.fon3.setStyleSheet("background-color: rgb(146, 204, 137);")
        self.fon3.setText("")
        self.fon3.setObjectName("fon3")
        #self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        #self.btn7.setGeometry(QtCore.QRect(50, 620, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        #self.btn7.setFont(font)
        #self.btn7.setStyleSheet("background-color: rgb(225, 255, 220);")
        #self.btn7.setObjectName("btn7")
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(230, 620, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn8.setFont(font)
        self.btn8.setStyleSheet("background-color: rgb(225, 255, 220);")
        self.btn8.setObjectName("btn8")
        #self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton_3.setGeometry(QtCore.QRect(410, 620, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        #self.pushButton_3.setFont(font)
        #self.pushButton_3.setStyleSheet("background-color: rgb(225, 255, 220);")
        #self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.btn8.clicked.connect(self.perehod3)
        #self.pushButton_3.clicked.connect(self.delete_record)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "БАЗА НАСЕЛЁННЫХ ПУНКТОВ"))
        #self.btn7.setText(_translate("MainWindow", "НАЗАД"))
        self.btn8.setText(_translate("MainWindow", "ДОБАВИТЬ "))
        #self.pushButton_3.setText(_translate("MainWindow", "УДАЛИТЬ"))



    def perehod3(self):
        self.okno=adder()
        self.okno.show()

    #def udalit(rowid):
        #def delete_sqlite_record(dev_id):
        #try:
            #sqlite_connection = sqlite3.connect('sql.sqlite')
            #cursor = sqlite_connection.cursor()
            #print("Подключен к SQLite")
            #sql_delete_query = """DELETE from signup where rowid = ? """
            #cursor.execute(sql_delete_query, (rowid, ))
            #sqlite_connection.commit()
            #print("Запись успешно удалена")
            #cursor.close()



        #except sqlite3.Error as error:
            #print("Ошибка при работе с SQLite", error)
        #finally:
            #if sqlite_connection:
                #sqlite_connection.close()
                #print("Соединение с SQLite закрыто")

    #delete_sqlite_record(5)

    def delete_record(self):
        try:
            sqlite_connection = sqlite3.connect('sql.sqlite')
            cursor = sqlite_connection.cursor()
            print("Подключен к SQLite")

            sql_delete_query = ("""DELETE from signup where locality = ?""", ()).fetchall()
            cursor.execute(sql_delete_query)
            sqlite_connection.commit()
            print("Запись успешно удалена")
            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")


class adder(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        import add
        self.win = add.adds()
        self.win.setupUi(self)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = base()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
