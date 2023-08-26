import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow
import image
import sqlite3




class WelcomeScreen(QMainWindow):
    def __init__(self):
        super(WelcomeScreen,self).__init__()
        loadUi("riggu_home.ui",self)
        self.doc_btn.clicked.connect(self.goto_doc)


    def goto_doc(self):
        wlcm = doc_wlcm()
        widget.addWidget(wlcm)
        widget.setCurrentIndex(widget.currentIndex()+1)



class doc_wlcm(QMainWindow):
    def __init__(self):
        super(doc_wlcm, self).__init__()
        loadUi("doc_wlcm.ui",self)
        self.gb_btn1.clicked.connect(self.goto_home)
        self.signin_btn1.clicked.connect(self.goto_docsignin)
        self.signup_btn1.clicked.connect(self.goto_docsignup)

    def goto_home(self):
        home = WelcomeScreen()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_docsignin(self):
        signin = docsignin()
        widget.addWidget(signin)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_docsignup(self):
        signup = docsignup()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex()+1)

class docsignup(QMainWindow):
    def __init__(self):
        super(docsignup,self).__init__()
        loadUi("doc_signup.ui",self)
        self.gb_btn3.clicked.connect(self.goto_docwlcm)
        self.pswrd_txt.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cnf_pswrd_txt_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.submit_btn2.clicked.connect(self.signup_func)

    def signup_func(self):
        user = self.username_txt.text()
        pswrd = self.pswrd_txt.text()
        cnf_pswrd = self.cnf_pswrd_txt_2.text()

        if len(user)==0 or len(pswrd)==0 or len(cnf_pswrd)==0:
            self.error.setText("!! Please Enter All Fields !!")

        elif (pswrd != cnf_pswrd):
            self.error.setText("!! PLease Enter The Correct Password !!")
    

    def goto_docwlcm(self):
        wlcm = doc_wlcm()
        widget.addWidget(wlcm)
        widget.setCurrentIndex(widget.currentIndex()+1)
        

    


class docsignin(QMainWindow):
    def __init__(self):
        super(docsignin,self).__init__()
        loadUi("doc_login.ui",self)
        self.gb_btn2.clicked.connect(self.goto_docwlcm)
        self.pswrd_txt.setEchoMode(QtWidgets.QLineEdit.Password)
        self.submit_btn1.clicked.connect(self.login_func)

    def login_func(self):
        user = self.username_txt.text()
        pswrd = self.pswrd_txt.text()

        if len(user)==0 or len(pswrd)==0:
            self.error.setText("!! Please Enter All Fields !!")

    def goto_docwlcm(self):
        wlcm = doc_wlcm()
        widget.addWidget(wlcm)
        widget.setCurrentIndex(widget.currentIndex()+1)

        




#main

app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1280)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")