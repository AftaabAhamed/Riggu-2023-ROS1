#!/usr/bin/env python3  
import roslib
import rospy

import tf


trans = (0,0,0)
rot = (0,0,0,1)
def publishtf():
    rospy.init_node("laser_base_tf",anonymous=True)
    rate = rospy.Rate(10.00)
    br = tf.TransformBroadcaster()
    li = tf.TransformListener()


    while not rospy.is_shutdown():
        
        # (trans,rot) = li.lookupTransform("tf/odom","tf/map",rospy.Time(0))
        br.sendTransform(trans,rot,rospy.Time(0),"laser","base_link")
        rate.sleep()



if __name__ == '__main__':
    try:
        publishtf()
    except rospy.ROSInterruptException:
        pass