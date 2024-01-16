#!/usr/bin/env python3
import rospy
from tkinter import *
import asyncio 
from threading import Thread



from std_msgs.msg import String

from geometry_msgs.msg import Twist 

from time import sleep


class controller():
    def __init__(self):
        self.pub_ = rospy.Publisher('cmd_vel', Twist)
        rospy.init_node('pidtest', anonymous=True)
        self.msg = Twist()

        self.msg.linear.y = 0
        self.msg.linear.x = 0
        self.msg.angular.z = 0


    def forward(self,vel=0.4,time=3):
        self.msg.linear.x = vel
        sleep(time)
        self.stop()

    def backward(self,vel=0.4,time=3):
        self.msg.linear.x = -vel
        sleep(time)
        self.stop()

    def stop(self):
        self.msg.linear.y = 0
        self.msg.linear.x = 0
        self.msg.angular.z = 0
    def rospublisher(self):
        rate = rospy.Rate(10)
        self.forward
        while not rospy.is_shutdown():
            data = (self.msg.linear.x,self.msg.linear.y)
            rospy.loginfo(data)
            self.pub_.publish(self.msg)
            rate.sleep()
    def gui(self):
        root = Tk()
        root.title("pid test")

        fbutton = Button(root,text="forward", command= self.forward)
        bbutton = Button(root,text="backward", command= self.backward)
        sbutton = Button(root,text="stop", command= self.stop)
        
        fbutton.pack()
        bbutton.pack()
        sbutton.pack()
        root.mainloop()
    
    def start_threads(self):

        gui =  Thread(target = self.gui)
        ros = Thread(target = self.rospublisher)

        gui.start()
        ros.start()


        

  
ct = controller()
if __name__ == '__main__':
    try:
        ct.start_threads()
        
        
    except rospy.ROSInterruptException:
        pass