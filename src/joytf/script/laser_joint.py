#!/usr/bin/env python3  
import roslib
import rospy

from sensor_msgs.msg import JointState


trans = (0,0,0)
rot = (0,0,0,1)
def publishtf():
    rospy.init_node("laser_link_tf",anonymous=True)
    pub_laser_link = rospy.Publisher('laser_link', JointState, queue_size=10)
    rate = rospy.Rate(10.00)
    joints = JointState()
    joints.name.append('base_link_to_laser')



    while not rospy.is_shutdown():
        joints.header.stamp = rospy.get_rostime()
        joints.position = [0]
        pub_laser_link.publish(joints)
        rate.sleep()



if __name__ == '__main__':
    try:
        publishtf()
    except rospy.ROSInterruptException:
        pass