from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtGui import QPainter, QTextDocument
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QLineEdit
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
        self.textbox.setEchoMode(QLineEdit.Normal)
        self.textbox.resize(280, 40)

        self.textbox2 = QtWidgets.QLineEdit(self)
        self.textbox2.move(605, 270)
        self.textbox2.setEchoMode(QLineEdit.Normal)
        self.textbox2.resize(280, 40)

        self.continueBtn = QtWidgets.QPushButton("Perform Query", self)
        self.continueBtn.setGeometry(205,200, 200,60)
        self.continueBtn.clicked.connect(self.cont)

        self.exportBtn = QtWidgets.QPushButton("Export Query", self)
        self.exportBtn.setGeometry(625, 200, 200, 60)
        self.exportBtn.clicked.connect(self.exportFunc)


        self.output2 = QPlainTextEdit(self)
        self.output2.move(205,260)
        self.output2.setGeometry(150,300,400,200)
        self.output2.setReadOnly(True)
        self.show()

        self.theOutput =[]

        self.input =""

    #def QPlainTextEdit.event(e)

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
        self.input2 = self.textbox2.text()
        if self.output2.blockCount() == 1:
            return
        if self.input2 == "":
            self.errorPop("You must enter a file name!",1)
            return
        ex = export.export()
        ex.runExport(self.theOutput, self.input, self.input2)

    def cont(self):

        self.input = self.textbox.text().lower()
        bool = self.input.find("select")
        if input == "":
           return
        elif bool == -1:
            self.errorPop("ONLY QUERIES PERMITTED",1)
            return
        else:
            que = dbQuery.query()
            returnInput,e = que.query(self.input)
            if returnInput == 0:
                self.errorPop(e)
            else:
                self.output2.clear()
                for x in range(e):
                    self.output2.insertPlainText(returnInput[x] +"\n")
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
