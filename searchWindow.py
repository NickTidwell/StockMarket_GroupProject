from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtGui import QPainter, QTextDocument
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QTextDocument
from PyQt5.QtCore import QRect, Qt, QRectF
from PyQt5.QtWidgets import QPlainTextEdit
import sys
import dbConn
import mainGUI
from PyQt5 import QtGui
import dbQuery
import export
import string

class search_window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setup()

    def setup(self):
        self.setGeometry(10, 10, 900, 600)
        self.setFixedSize(900,600)
        self.setWindowTitle("Search")

        self.textbox = QtWidgets.QLineEdit(self)
        self.textbox.move(165, 150)
        self.textbox.setEchoMode(0)
        self.textbox.resize(280, 40)

        self.continueBtn = QtWidgets.QPushButton("Perform Query", self)
        self.continueBtn.setGeometry(205,200, 200,60)
        self.continueBtn.clicked.connect(self.cont)

        self.exportBtn = QtWidgets.QPushButton("Export Query", self)
        self.exportBtn.setGeometry(505, 200, 200, 60)
        self.exportBtn.clicked.connect(self.exportFunc)


        self.output = QPlainTextEdit(self)
        self.output.move(205,260)
        self.output.setGeometry(150,300,400,200)
        self.output.setReadOnly(True)
        self.show()

        self.theOutput =[]

    def errorPop(self,err,msgCode=0):
        msg = QtWidgets.QMessageBox()
        if msgCode ==0:
            msg.setText(str(err)[7:-1])
        else:
            msg.setText(str(err))
        msg.setInformativeText( "Check your input." + "\nClick Cancel To Exit")
        msg.setWindowTitle("Error: Invalid Search String")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msg.setGeometry(190, 190, 200, 100)
        ret = msg.exec_()
        if ret == 4194304:
            QtWidgets.QApplication.quit()

    def exportFunc(self):
        if self.output.blockCount() == 1:
            return
        ex = export.export()
        ex.runExport(self.theOutput)

    def cont(self):
        input = self.textbox.text().lower()
        bool = input.find("select")
        if input == "":
           return
        elif bool == -1:
            self.errorPop("ONLY QUERIES PERMITTED",1)
            return
        else:
            que = dbQuery.query()
            returnInput,e = que.query(input)

            if returnInput == 0:
                self.errorPop(e)
            else:
                self.output.clear()
                for x in range(e):
                    self.output.insertPlainText(returnInput[x] +"\n")
                self.theOutput = returnInput

    def paintEvent(self,event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.qp.drawText(90,90,"Enter in your query")
        self.qp.end()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = search_window()
    app.exec_()
