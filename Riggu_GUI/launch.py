import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow, QMessageBox
import image
import sqlite3
import cv2
import os
import numpy as np
from deepface import DeepFace
import sqlite3
from PIL import Image

#// WELCOME SCREEN CLASS (RIGGU HOME WINDOW //

class WelcomeScreen(QMainWindow):
    def __init__(self):
        super(WelcomeScreen,self).__init__()
        loadUi("riggu_home.ui",self)
        self.doc_btn.clicked.connect(self.goto_doc)


    def goto_doc(self):
        wlcm = doc_wlcm()
        widget.addWidget(wlcm)
        widget.setCurrentIndex(widget.currentIndex()+1)


#// DOCTOR WELCOME CLASS (HERE YOU GET THE SIGNUP AND SIGNIN OPTIONS) //


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

#// DOCTOR SIGNUP PAGE ( HERE YOU GET THE SIGNUP INFORMATION) //


class docsignup(QMainWindow):
    def __init__(self):
        super(docsignup,self).__init__()
        loadUi("doc_signup.ui",self)
        self.gb_btn3.clicked.connect(self.goto_docwlcm)
        self.pswrd_txt.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cnf_pswrd_txt_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.submit_btn2.clicked.connect(self.signup_func)
        self.face_btn2.clicked.connect(self.add_face)

# // ADDING FACE DATA OF A DOCTOR // 


    def add_face(self):
        user = self.username_txt.text()
        pswrd = self.pswrd_txt.text()
        cnf_pswrd = self.cnf_pswrd_txt_2.text()
        if ((len(user)!=0 and len(pswrd)!=0 and len(cnf_pswrd)!=0) and (pswrd == cnf_pswrd)):
           
            doctor_directory = os.path.join("doc_images", user)
            os.makedirs(doctor_directory,exist_ok=True)

            cam = cv2.VideoCapture(0)
            image_counter = 0
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

            while (image_counter<1):
                ret,frame = cam.read()
                if not ret:
                    break

                gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

                if len(faces)>0:
                    image_path = os.path.join(doctor_directory, f"face_{image_counter}.jpg")
                    cv2.imwrite(image_path,frame)
                    image_counter+=1

                    # Draw a bounding box around the detected face
                    for (x, y, w, h) in faces:
                        cv2.rectangle(frame, (x, y), (x + w, y + h), ( 255, 0, 0), 2)


                cv2.imshow("Captured Image", frame)
                cv2.waitKey(500)
            cam.release()
            cv2.destroyAllWindows()

            self.add_doctor_data(user, pswrd, image_path)

        else:
            if len(user)==0 or len(pswrd)==0 or len(cnf_pswrd)==0:
                self.error.setText("!! Please Enter All Fields !!")

            elif (pswrd != cnf_pswrd):
                self.error.setText("!! PLease Enter The Correct Password !!")



    def signup_func(self):
        user = self.username_txt.text()
        pswrd = self.pswrd_txt.text()
        cnf_pswrd = self.cnf_pswrd_txt_2.text()

        if len(user)==0 or len(pswrd)==0 or len(cnf_pswrd)==0:
            self.error.setText("!! Please Enter All Fields !!")

        elif (pswrd != cnf_pswrd):
            self.error.setText("!! PLease Enter The Correct Password !!")

        else:
            self.conn = sqlite3.connect("riggu_hms.db")
            self.create_table()
            


    def create_table(self):

        # CREATING A TABLE TO STORE DOCTOR'S SIGNUP DATA

        query = """
        CREATE TABLE IF NOT  EXISTS doctors (
        username TEXT,
        password TEXT,
        image_path TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

        try:
            self.conn.execute(query)
            self.conn.commit()
            print("Table 'doctors' created successfully.")
        except sqlite3.Error as e:
            print("Error creating table:", e)

    # NOW ADD DOCTORS DATA TO A DATABASE NAMED "riggu_hms" IN TABLE NAMED "doctors"

    def add_doctor_data(self, username, password,image_path):
        
        #ADD DATA
        
        try:
            query = "INSERT INTO doctors (username, password, image_path) VALUES (?,?,?)"
            # with open(embeddings_path, "rb") as f:
                # face_embeddings = f.read()

            self.conn = sqlite3.connect("riggu_hms.db")
            self.conn.execute(query,(username, password, image_path))
            self.conn.commit()
            print("Doctors data added successfully!!")

        except sqlite3.Error as e:
            print("Error adding doctors data: ", e)

    def close_connection(self):
        self.conn.close()


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
        self.face_btn1.clicked.connect(self.face_login)

    

    def face_login(self):
        
        #connecting to database
        conn = sqlite3.connect("riggu_hms.db")
        cam = cv2.VideoCapture(0)
        login_directory = os.path.join("login_images")
        image_counter = 0
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        while (image_counter<1):
            ret, frame = cam.read()
            if not ret:
                break
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            if len(faces)>0:
                login_image_path = os.path.join(login_directory, f"face_{image_counter}.jpg")
                cv2.imwrite(login_image_path,frame)
                image_counter+=1

                 # Draw a bounding box around the detected face
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), ( 255, 0, 0), 2)


            cv2.imshow("Face ID Login", frame)
            cv2.waitKey(500)
        cam.release()
        cv2.destroyAllWindows()

        # computed_embeddings = self.compute_and_save_embeddings(login_directory)

        cursor = conn.cursor()
        cursor.execute("SELECT username, image_path FROM doctors")
        user_records = cursor.fetchall()

        similarity_threshold = 0.8

        authenticated_user = None

        for username, stored_image_path in user_records:
            stored_image = stored_image_path
            img1 = login_image_path
            img2 = stored_image

            similarity_score = DeepFace.verify(img1, img2, enforce_detection=False)["verified"]

            if (similarity_score > similarity_threshold):
                authenticated_user = username
                

        conn.close()

        if authenticated_user:
            print(f"User {authenticated_user} is authenticated.")
            # Allow access to the user's account
        else:
            print("Access denied.")
            # Deny access


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