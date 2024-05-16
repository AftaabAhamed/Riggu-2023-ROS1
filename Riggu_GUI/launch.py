import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtCore import QProcess,QPoint, QEasingCurve
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow, QMessageBox,QPushButton,QVBoxLayout,QLabel
from PyQt5.QtGui import QPixmap
import image
import sqlite3
import cv2
import os
import numpy as np
from deepface import DeepFace
import sqlite3
from PIL import Image
import subprocess,time
from riggu_speech import riggu_speech_pv as speech
#// WELCOME SCREEN CLASS (RIGGU HOME WINDOW //

class WelcomeScreen(QMainWindow):
    def __init__(self):
        super(WelcomeScreen,self).__init__()
        loadUi("riggu_home.ui",self)
        self.doc_btn.clicked.connect(self.goto_doc)
        self.admin_btn.clicked.connect(self.goto_admin)
        self.i_mode_btn.clicked.connect(self.goto_imode)


    def goto_doc(self):
        wlcm = doc_wlcm()
        widget.addWidget(wlcm)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def goto_admin(self):
        mode_slct = user_mode_select()
        widget.addWidget(mode_slct)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def goto_imode(self):
        imode = interactive_mode()
        widget.addWidget(imode)
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
           
            doctor_directory = os.path.join("doc_images")
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
                    image_path = os.path.join(doctor_directory, f"{user}_{image_counter}.jpg")
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


#user chooses whether to start mapping or start navigation

class user_mode_select(QMainWindow):
    def __init__(self):
        super(user_mode_select, self).__init__()
        loadUi("user_mode_select.ui",self)
        self.gb_btn_usr.clicked.connect(self.goto_home)
        self.st_map_btn.clicked.connect(self.start_mapping)
        self.nav_btn.clicked.connect(self.start_navigation)

    def start_mapping(self):
        mapping_proc = subprocess.Popen(["roslaunch","joytf","slam.launch"])
        dlg = QMessageBox(self)
        dlg.setWindowTitle("end mapping")
        dlg.setText("Click ok to save map")
        button = dlg.exec()
        if button == QMessageBox.Ok:
            map_save_proc = subprocess.Popen(["rosrun","map_server","map_saver","-f","map"])
            time.sleep(2)
            mapping_proc.terminate()
            map_save_proc.terminate()

    def goto_home(self):
        home = WelcomeScreen()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def start_navigation(self):
        nav = nav_page()
        widget.addWidget(nav)
        widget.setCurrentIndex(widget.currentIndex()+1)

class nav_page(QMainWindow):
    def __init__(self):
        super(nav_page, self).__init__()
        loadUi("nav_page.ui",self)
        widget = self.widget
        layout = self.gdlayout
        self.setCentralWidget(widget)
        self.gb_btn_nav.clicked.connect(self.goto_home)
        self.rviz_proc = QProcess()
        self.nav_proc = QProcess()
        self.rviz_proc.start("rviz")
        pid = self.rviz_proc.pid
        print(f"best pid {pid}")
        wid = self.get_wid(pid)
        print(wid)
     
        self.externalWindow = QtGui.QWindow.fromWinId(wid)
        self.externalWindow.setFlags(QtCore.Qt.FramelessWindowHint)
        self.windowcontainer = self.createWindowContainer(self.externalWindow, widget)
        # self.windowcontainer.resize(500,300)
        layout.addWidget(self.windowcontainer, 0, 0)  
        self.nav_proc.start('roslaunch',['joytf','riggu_nav.launch'])      

        
    def window_id(self,proc_id):
        proc = subprocess.Popen('echo "ibase=16; `wmctrl -l | grep -i rviz | cut -c 3-11 | tr a-z A-Z`" | bc',
                            env=os.environ,
                            stdout=subprocess.PIPE,
                            universal_newlines=True,
                            shell=True)
        out = proc.communicate()[0]

        # print(f"window id{out}")
        return(out)

    def get_wid(self,proc_id,time_out = 1):
        st_time = time.time()
        wid = self.window_id(proc_id)
        while((time.time()-st_time)<time_out):

            wid = self.window_id(proc_id)
            print(wid)
        print(f"window id passed{wid}")
        return int(wid)

    def goto_home(self):
        self.rviz_proc.terminate()
        home = WelcomeScreen()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1)


class interactive_mode(QMainWindow):
    def __init__(self):
        super(interactive_mode, self).__init__()
        loadUi("interactive_mode.ui",self)
        self.gb_btn_im.clicked.connect(self.goto_home)
        self.nav_proc = QProcess()
        # self.speech = QProcess()
        # self.speech.start('python3',['/home/aftaab/Documents/riggu_git/Riggu-2023/riggu_speech/riggu_speech_pv.py'])
        self.rt = speech.riggutalk()
        # self.rt.speak_async("hello i am riggu")
        self.rt.start_listen()
        


        left_pxmp = QPixmap('left_eye.jpg')
        right_pxmp = QPixmap('right_eye.jpg')

        self.label = QLabel(self)

        self.l_eye = QLabel(self)
        self.r_eye = QLabel(self)

        self.l_eye.setPixmap(left_pxmp)
        self.r_eye.setPixmap(right_pxmp)

        self.l_eye.setGeometry(800, 160,0,0)
        self.r_eye.setGeometry(120, 160,0,0)

        self.l_eye.resize(left_pxmp.width(),left_pxmp.height())
        self.r_eye.resize(right_pxmp.width(),right_pxmp.height())

        self.l_eye_anim = QtCore.QPropertyAnimation(self.l_eye, b'pos')
        self.r_eye_anim = QtCore.QPropertyAnimation(self.r_eye, b'pos')

        self.l_eye_pos = (800,160)
        self.r_eye_pos = (120,160)

        # self.look_left()
        # time.sleep(2)
        # self.look_right()
        # self.look_straight()
    
    def look_left(self):
        self.l_eye_anim.setEasingCurve(QEasingCurve.InOutCubic)
        self.r_eye_anim.setEasingCurve(QEasingCurve.InOutCubic)

        x_l,y_l = self.l_eye_pos
        x_r,y_r = self.r_eye_pos

        self.l_eye_anim.setEndValue(QPoint(x_l+50, y_l))
        self.r_eye_anim.setEndValue(QPoint(x_r+100, y_r))

        self.l_eye_anim.setDuration(500)
        self.r_eye_anim.setDuration(500)
        self.l_eye_anim.start()
        self.r_eye_anim.start()
        pass

    def look_right(self):
        self.l_eye_anim.setEasingCurve(QEasingCurve.InOutCubic)
        self.r_eye_anim.setEasingCurve(QEasingCurve.InOutCubic)

        x_l,y_l = self.l_eye_pos
        x_r,y_r = self.r_eye_pos

        self.l_eye_anim.setEndValue(QPoint(x_l-100, y_l))
        self.r_eye_anim.setEndValue(QPoint(x_r-50, y_r))

        self.l_eye_anim.setDuration(500)
        self.r_eye_anim.setDuration(500)
        self.l_eye_anim.start()
        self.r_eye_anim.start()
        pass

    def look_straight(self):
        self.l_eye_anim.setEasingCurve(QEasingCurve.InOutCubic)
        self.r_eye_anim.setEasingCurve(QEasingCurve.InOutCubic)

        x_l,y_l = self.l_eye_pos
        x_r,y_r = self.r_eye_pos

        self.l_eye_anim.setEndValue(QPoint(x_l, y_l))
        self.r_eye_anim.setEndValue(QPoint(x_r, y_r))

        self.l_eye_anim.setDuration(500)
        self.r_eye_anim.setDuration(500)
        self.l_eye_anim.start()
        self.r_eye_anim.start()
        pass
    
    def goto_home(self):
        # self.look_loop()
        self.rt.stop_listen()
        home = WelcomeScreen()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1) 
         
    def look_loop(self):
        self.look_left()
        time.sleep(2)
        self.look_right()


        
















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
