from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtGui import QPainter, QTextDocument
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QGridLayout
from PyQt5.QtGui import QPainter, QTextDocument
from PyQt5.QtCore import QRect, Qt, QRectF
from PyQt5.QtWidgets import QLineEdit
import sys
import dbConn
import mainGUI
from PyQt5 import QtGui
from PyQt5.QtWidgets import QPlainTextEdit

import dbGUI
import searchWindow
import dbQuery

class main_window(QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.title = "DB Dashboard"
        self.setGeometry(50, 50, 800, 600)
        self.setFixedSize(800, 600)
        self.test = searchWindow.search_window()
        self.test.setup()
        self.test.hide()
        self.setup()

    def setup(self):
        self.btns = []
        self.query = self.dbEventBtn("Query")
        self.archive = self.dbEventBtn("Archive")
        self.manageTables = self.dbEventBtn("Manage Tables")
        self.b1 = self.dbEventBtn("TBD")
        self.b2 = self.dbEventBtn("TBD")
        self.b3 = self.dbEventBtn("TBD")

        self.btns.append(self.query)
        self.btns.append(self.archive)
        self.btns.append(self.manageTables)
        self.btns.append(self.b1)
        self.btns.append(self.b2)
        self.btns.append(self.b3)

        self.setWindowTitle(self.title)
        self.gridded = QGridLayout()
        c =0

        for i in range(3):
            for x in range(2):
                self.gridded.addWidget(self.btns[c],i,x)
                c = c + 1
        self.setLayout(self.gridded)
        self.query.clicked.connect(self.queryPop)

        self.show()

    class getText(QtWidgets.QLineEdit):
        def __init__(self):
            QtWidgets.QLineEdit.__init__(self)
            #output2 = QPlainTextEdit()
            self.move(165, 150)
            #self.setEchoMode(0)
            self.resize(280, 40)

    class dbEventBtn(QtWidgets.QPushButton):
        def __init__(self,name):
            QtWidgets.QPushButton.__init__(self)
            self.setText(name)
            self.width =20
            self.height=20
            self.name = name

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.drawText(300, 30, "DB Dashboard")

        #rect = QRect(100, 150, 250, 25)
        #painter.drawRect(rect)
        #painter.drawText(rect, Qt.AlignCenter, "Hello World")

    def queryPop(self):
        self.test.show()
        #self.test = searchWindow.search_window()
        #self.test = dbGUI.loginWindow()
        #self.test.setup()
        #self.test.show()
        """
        msg.setInformativeText( "Check your input." + "\nClick Cancel To Exit")
        msg.setWindowTitle("Error: Invalid DB")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msg.setGeometry(190, 190, 100, 100)
        ret = msg.exec_()
        if ret == 4194304:
            QtWidgets.QApplication.quit()
        """

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = main_window()
    app.exec_()
