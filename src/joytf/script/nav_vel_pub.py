#!/usr/bin/env python3
import rospy
from math import pi
from std_msgs.msg import Int16MultiArray,Float64
from geometry_msgs.msg import Twist

leftMotor = 0
rightMotor = 0

class tf_cmd_vel:
    def __init__(self,width,wheel_radius):
        self.width = width
        self.radius = wheel_radius
    def get_twist(self,cmd_vel):
        self.linx = cmd_vel.linear.x
        self.angx = cmd_vel.angular.z
    def transform(self):
        wl = (1.0*self.linx - (self.angx*self.width/2))/self.radius
        wr = (1.0*self.linx + (self.angx*self.width/2))/self.radius

        left_rate = (wl*300)/(2*pi)
        right_rate = wr*300/(2*pi)
        return((left_rate,right_rate))

        

tf = tf_cmd_vel(0.195,0.0325)

def callback(twist):
    tf.get_twist(twist)
    global leftMotor
    global rightMotor
    (leftMotor,rightMotor) = tf.transform()
class tf_cmd_vel:
    def _init_(self,width,wheel_radius):
        self.width = width
        self.radius = wheel_radius
    def get_twist(self,cmd_vel):
        self.linx = cmd_vel.linear.x
        self.angx = cmd_vel.angular.z
    def transform(self):
        wl = (1.0*self.linx - (self.angx*self.width/2))/self.radius
        wr = (1.0*self.linx + (self.angx*self.width/2))/self.radius

        left_rate = (wl*300)/(2*pi)
        right_rate = (wr*300)/(2*pi)
        return((left_rate,right_rate))

    
def listentalker():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listentalker', anonymous=True)
    rospy.Subscriber('cmd_vel', Twist, callback)

    publ = rospy.Publisher('/setpoint_left', Float64 ,queue_size=10)
    pubr = rospy.Publisher('/setpoint_right', Float64 ,queue_size=10)

    # publ = rospy.Publisher('left_wheel/control_effort', Float64 ,queue_size=10)
    # pubr = rospy.Publisher('right_wheel/control_effort', Float64 ,queue_size=10)
    global rightMotor
    global leftMotor

    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        speed_left = -leftMotor
        speed_right = -rightMotor

        msg = f"Speeds={speed_left}/{speed_right}"
        rospy.loginfo(msg)
        publ.publish(speed_right) #reversed
        pubr.publish(speed_left)
        rate.sleep()

    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        listentalker()
    except rospy.ROSInterruptException:
        pass