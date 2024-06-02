#!/usr/bin/env python3
import rospy
import math
from math import pi
from std_msgs.msg import String , Int16MultiArray,Float64
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist


#from _future_ import division
linear_velocity = 0
angular_velocity = 0


leftMotor = 12
rightMotor = 12

class MotorCommand:
    """Holds motor control commands for a differential-drive robot. """
    def _init_(self):
        self.left = 0
        self.right = 0
        

class Controller:
    """Determines motor speeds to accomplish a desired motion.
    """

    def _init_(self):
        # Set the max motor speed to a very large value so that it
        # is, essentially, unbound.
        self.maxMotorSpeed = 1E9 # ticks/s

    def getSpeeds(self, linearSpeed, angularSpeed):
        tickRate = linearSpeed*self.ticksPerMeter
        diffTicks = angularSpeed*self.wheelSeparation*self.ticksPerMeter

        speeds = MotorCommand()
        speeds.left = tickRate - diffTicks
        speeds.right = tickRate + diffTicks

        # Adjust speeds if they exceed the maximum.
        if max(abs(speeds.left), abs(speeds.right)) > self.maxMotorSpeed:
            factor = float(self.maxMotorSpeed / max(abs(speeds.left), abs(speeds.right)))
            speeds.left *= (factor)
            speeds.right *= (factor)


        speeds.left = int(speeds.left)
        speeds.right = int(speeds.right)
        return speeds

    def setWheelSeparation(self, separation):
        self.wheelSeparation = separation

    def setMaxMotorSpeed(self, limit):
        self.maxMotorSpeed = limit

    def setTicksPerMeter(self, ticks):
        self.ticksPerMeter = ticks

cont = Controller()

def callback(data : Twist):
    global linear_velocity
    global angular_velocity
    linear_velocity = data.linear.x
    angular_velocity = data.angular.z


    cont.setMaxMotorSpeed(1.8e4)  #with 60rpm motor
    cont.setTicksPerMeter(609.7) #find no of ticks after robot moves one meter and pass as the parameter 609.6
    cont.setWheelSeparation(0.195) #pass distance between the wheels as param

    speeds = cont.getSpeeds(linear_velocity,angular_velocity)
    global leftMotor
    global rightMotor
    leftMotor = speeds.left
    rightMotor = speeds.right
    
    # rospy.loginfo(str(x)+"  "+str(y))

# def talker():
#     pub = rospy.Publisher('velocity', Int16MultiArray, queue_size=10)
#     rospy.init_node('talker', anonymous=True)
#     rate = rospy.Rate(10) # 10hz
#     while not rospy.is_shutdown():
#         speeds = Int16MultiArray()
#         speeds.data = [leftMotor,rightMotor]
#         rospy.loginfo(speeds)
#         pub.publish(speeds)
#         rate.sleep()

    
def listentalker():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listentalker', anonymous=True)
    rospy.Subscriber('cmd_vel', Twist, callback)

    publ = rospy.Publisher('left_wheel/control_effort', Float64 ,queue_size=10)
    pubr = rospy.Publisher('right_wheel/control_effort', Float64 ,queue_size=10)
    global linear_velocity
    global angular_velocity

    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        speed_left = leftMotor/(20)
        speed_right = rightMotor/20
        vels = Int16MultiArray()

        vels.data = [linear_velocity,angular_velocity]
        msg = f"Speeds={speed_left}/{speed_right}, Vels={vels.data}"
        rospy.loginfo(msg)
        publ.publish(speed_left)
        pubr.publish(speed_right)
        rate.sleep()

    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        listentalker()
    except rospy.ROSInterruptException:
        pass