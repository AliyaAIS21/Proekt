import sys
from PyQt5 import QtCore, QtWidgets, QtCore, QtGui
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableView, QApplication



class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('glavnaya.ui', self)
        self.btn1.clicked.connect(self.perehod1)
        self.btn2.clicked.connect(self.perehod2)

    def perehod1(self):
        self.okno2 = prog()
        self.okno2.show()


    def perehod2(self):
        self.okno=base1()
        self.okno.show()

class base1(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        #uic.loadUi('baza.ui', self)
        import baza
        self.win = baza.base()
        self.win.setupUi(self)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('sql.sqlite')
        self.db.open()
        self.view = QTableView(self)
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('signup')
        self.model.select()

        self.view.setModel(self.model)
        self.view.move(10, 10)
        self.view.resize(580, 315)

        self.setGeometry(300, 100, 600, 700)
        self.setWindowTitle('БАЗА')






class prog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        import dfdfd
        self.win = dfdfd.prognoze()
        self.win.setupUi(self)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
