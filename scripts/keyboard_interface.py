#! /usr/bin/env python
"""

.. module:: keyboard_interface
    :platform: Unix
    :synopsis: Python code for launching the needed nodes for user control manually
.. moduleauthor:: Hussein Hassan  S5165612@studenti.unige.it

Service:
    /keyboard_interface to start the robot motion autonumously


This node is used for managing the robot with the choice 2 which is making the user 
control the robot manually with assistance or without.
"""

import rospy
from assignment3.srv import keyboard_interface	
import os   #used for write lines on terminal and do them (system )

#get the request (user input) and choose which choice will launch
def handler(req):
    """
    this function is used for choose between the two modes for manual control for the robot
    by getting the choice from services from user_control_node  
    """

    if req.user_input == 2:
    
       print("initializing the teleop keyboard ")
       #launch_file choice 3
       os.system("roslaunch assignment3 choice_two.launch") 
       
    elif req.user_input == 3:
        print("calling teleop twist keyboard with obstacle avoidance control")
        #launch_file choice 3
        os.system("roslaunch assignment3 choice_three.launch")
    else:
        print("wrong input change it please")
    return 0         
   

    
    

#main
if __name__=="__main__":
    rospy.init_node('keyboard_interface')                                      
    a = rospy.Service('keyboard_interface' ,keyboard_interface ,handler)   
    rospy.spin()
