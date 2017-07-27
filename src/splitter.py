#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from lab_ros_speech_to_text.msg import Speech

class splitter:


    def callback(self,speech):

        if speech.is_final:
            self.complete_pub.publish(speech.text)

        else:
            self.partial_pub.publish(speech.text)
    def __init__(self):
        rospy.init_node('speech_splitter')
        self.complete_pub = rospy.Publisher('speech/complete', String, queue_size=10)
        self.partial_pub = rospy.Publisher('speech/partial', String, queue_size=10)
        sub = rospy.Subscriber('stt', Speech, self.callback)

        rospy.spin()

if __name__ == '__main__':
    splitter()
