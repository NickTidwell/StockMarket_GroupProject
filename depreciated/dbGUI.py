from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtGui import QPainter, QTextDocument
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QTextDocument
from PyQt5.QtCore import QRect, Qt, QRectF
import sys
import dbConn
import mainGUI
from PyQt5 import QtGui

class loginWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setup()
        returnCon = dbConn.connect

    def setup(self):
        self.setGeometry(10, 10, 600, 600)
        self.setFixedSize(600,600)
        bg = QtWidgets.QLabel(self)
        bg.setGeometry(0,0,600,600)
        pic = QtGui.QPixmap("bg.jpg")
        pic.scaled(200,200,aspectRatioMode=1, transformMode=1)
        bg.setPixmap(pic)


        self.setWindowTitle("Login")
        self.textbox = QtWidgets.QLineEdit(self)
        self.textbox.move(165, 150)
        self.textbox.setEchoMode(2)
        self.textbox.resize(280, 40)
        self.continueBtn = QtWidgets.QPushButton("Enter", self)
        self.continueBtn.setGeometry(205,200, 200,60)
        self.continueBtn.clicked.connect(self.cont)
        self.show()

    def returnConnection(self):
        print(self.returnCon)
        #return self.returnCon



    def errorPop(self):
        msg = QtWidgets.QMessageBox()
        msg.setText("Invalid DB - Try again.")
        msg.setInformativeText( "Check your input." + "\nClick Cancel To Exit")
        msg.setWindowTitle("Error: Invalid DB")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msg.setGeometry(190, 190, 100, 100)
        ret = msg.exec_()
        if ret == 4194304:
            QtWidgets.QApplication.quit()

    def cont(self,parent):
        input = self.textbox.text()
        if input == "":
            return
        connect = dbConn.connect(input)
        if connect != 0:
            #print(connect)
            self.returnCon = connect
            self.returnConnection()
            self.hide()
        else:
            self.errorPop()

def paintEvent(self,event):
    qp = QPainter(self)
    qp.begin()
    qp.drawText(90,90,"HELLO CLEVELAND")
    qp.end()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = loginWindow()
    app.exec_()



