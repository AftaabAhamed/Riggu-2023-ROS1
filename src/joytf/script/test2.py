#!/usr/bin/env python3
import rospy
import math
from math import pi
from std_msgs.msg import String , Int16MultiArray
from sensor_msgs.msg import Joy


#from _future_ import division

leftMotor = 12
rightMotor = 12




def callback(data):
    angular_velocity = (data[0])
    linear_velocity = (data[1])





    
def listentalker():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('pid', anonymous=True)
    rospy.Subscriber('velocity', Int16MultiArray, callback)

    pub = rospy.Publisher('pwm', Int16MultiArray, queue_size=10)
    
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pwm = Int16MultiArray()
        pwm.data = [leftpwm,rightpwm]
        rospy.loginfo(pwm)
        pub.publish(pwm)
        rate.sleep()

    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        listentalker()
    except rospy.ROSInterruptException:
        pass