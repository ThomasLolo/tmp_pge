#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import math
import numpy as np


def showImage(img):
    cv2.imshow('image', img)
    cv2.waitKey(1)




def process_image(msg):
    try:
        # convert sensor_msgs/Image to OpenCV Image
        bridge = CvBridge()
        orig = bridge.imgmsg_to_cv2(msg, "bgr8")
        drawImg = orig

    except Exception as err:
        print(err)

    showImage(drawImg)

def start_node():
    rospy.init_node('main_detect')
    rospy.loginfo('main_detect node started')

    rospy.Subscriber("/camera/color/image_raw", Image, process_image)
    rospy.spin()

if __name__ == '__main__':
    try:
        start_node()
    except rospy.ROSInterruptException:
        pass