import sqlite3
import sys
from PyQt5 import QtCore, QtWidgets, QtCore, QtGui
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableView, QApplication
import connection


class base(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('baza.ui', self)

        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('sql.sqlite')
        db.open()

        view = QTableView(self)
        model = QSqlTableModel(self, db)
        model.setTable('base')
        model.select()

        view.setModel(model)
        view.move(10, 10)
        view.resize(580, 315)

        self.setGeometry(300, 100, 600, 700)
        self.setWindowTitle('Пример работы с QtSql')



    def perehod2(self):
        pass
        # self.okno=base1()
        # self.okno.show()


# class base1(QtWidgets.QMainWindow):
# def __init__(self, parent=None):
# super().__init__(parent, QtCore.Qt.Window)
# import baza
# self.win = baza.base()
# self.win.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = base()
    ex.show()
    sys.exit(app.exec())
