# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from points import Ui_pointWindow
from login import Ui_loginWindow

class Ui_MainWindow(object):

    def openpoints(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_pointWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def openlogin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_loginWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QPushButton#Logout_Button{\n"
"    background-color: rgb(194, 151, 125);\n"
"    \n"
"    \n"
"    border-left:1px solid rgb(255,76,100);\n"
"    border-right:1px solid rgb(255,76,100);\n"
"    border-bottom:5px solid rgb(255,76,100);\n"
"}\n"
"QPushButton#Logout_Button:hover{\n"
"    background-color:rgb(192,192,192);\n"
"    color:rgb(0,0,0);\n"
"    border-left:1px solid rgb(128,128,128);\n"
"    border-right:1px solid rgb(128,128,128);\n"
"    border-bottom:5px solid rgb(128,128,128);\n"
"}\n"
"QPushButton#Logout_Button:pressed{\n"
"    background-color:rgb(192,192,192);\n"
"    color:rgb(0,0,0);\n"
"    border-left:1px solid rgb(128,128,128);\n"
"    border-right:1px solid rgb(128,128,128);\n"
"    border-top:5px solid rgb(128,128,128);\n"
"}\n"
"QPushButton#ViewPoint_Button{\n"
"    background-color: rgb(153, 184, 152);\n"
"    \n"
"    \n"
"    border-left:1px solid rgb(255,76,100);\n"
"    border-right:1px solid rgb(255,76,100);\n"
"    border-bottom:5px solid rgb(255,76,100);\n"
"}\n"
"QPushButton#ViewPoint_Button:hover{\n"
"    background-color:rgb(192,192,192);\n"
"    color:rgb(0,0,0);\n"
"    border-left:1px solid rgb(128,128,128);\n"
"    border-right:1px solid rgb(128,128,128);\n"
"    border-bottom:5px solid rgb(128,128,128);\n"
"}\n"
"QPushButton#ViewPoint_Button:pressed{\n"
"    background-color:rgb(192,192,192);\n"
"    color:rgb(0,0,0);\n"
"    border-left:1px solid rgb(128,128,128);\n"
"    border-right:1px solid rgb(128,128,128);\n"
"    border-top:5px solid rgb(128,128,128);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 110, 250, 230))
        self.label_2.setStyleSheet("\n"
"background-color: rgb(123, 174, 106);")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setLineWidth(5)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 110, 250, 230))
        self.label_3.setStyleSheet("background-color: rgb(116, 146, 122);")
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setLineWidth(5)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.Student_ID_2 = QtWidgets.QLabel(self.centralwidget)
        self.Student_ID_2.setGeometry(QtCore.QRect(100, 120, 221, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Student_ID_2.setFont(font)
        self.Student_ID_2.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"\n"
"\n"
"border-bottom:2px solid rgba(46,82,101,200);")
        self.Student_ID_2.setObjectName("Student_ID_2")
        self.Logout_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Logout_Button.setGeometry(QtCore.QRect(130, 290, 161, 28))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Logout_Button.setFont(font)
        self.Logout_Button.setObjectName("Logout_Button")
        self.ViewPoint_Button = QtWidgets.QPushButton(self.centralwidget)
        self.ViewPoint_Button.setGeometry(QtCore.QRect(110, 180, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.ViewPoint_Button.setFont(font)
        self.ViewPoint_Button.setObjectName("ViewPoint_Button")
        self.state = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.state.setGeometry(QtCore.QRect(360, 130, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.state.setFont(font)
        self.state.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.state.setStyleSheet("background-color: rgb(153, 184, 152);")
        self.state.setFrameShape(QtWidgets.QFrame.Box)
        self.state.setLineWidth(3)
        self.state.setTabStopWidth(0)
        self.state.setObjectName("state")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(350, 200, 211, 111))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.plainTextEdit.setLineWidth(3)
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.ViewPoint_Button.clicked.connect(self.openpoints)
        self.Logout_Button.clicked.connect(self.openlogin)
        self.Logout_Button.clicked.connect(MainWindow.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Student_ID_2.setText(_translate("MainWindow", "64140301021"))
        self.Logout_Button.setText(_translate("MainWindow", "L o g O u t"))
        self.ViewPoint_Button.setText(_translate("MainWindow", "View Point"))
        self.state.setPlainText(_translate("MainWindow", "Ready"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Congratulations !!!\n"
"You get the points "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
