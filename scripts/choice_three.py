#! /usr/bin/env python
"""

.. module:: choice_three
    :platform: Unix
    :synopsis: Python code for the robot drive manually with help to not crash walls
.. moduleauthor:: Hussein Hassan  S5165612@studenti.unige.it

Service:
    /robot_coordinates
Subscribes to :
    /map_update_cmd_vel
    /scan
publish to :
    /cmd_vel


This node is used for the user choice number three which is resposible for robot drive maually 
but if it's about to crash the wall the robot stops.

"""
import rospy
import numpy
from geometry_msgs.msg import Twist, Vector3    
from sensor_msgs.msg import LaserScan 

#min distance between the robot and the obstacle
min_dist = 0.5

init = Vector3(0, 0, 0)
assigned = Twist( init, init)


def find_min_dist(ranges):
    """
    This function is used for finding the minimum distance between the robot and the obstical 
    
    args:
        ranges(float):ranges angels of the robot vision 

    return:
        dist_all_directions(list):the nearest obsticales in all directions 
    
    """
    dist_all_directions = [0,0,0]
    #Make direction for each range
    right_range = ranges[0:240]
    front_range = ranges[240:480]
    left_range  = ranges[480:721]
    #compute and store the min dist_all_directions
    dist_all_directions[0] = min(right_range)
    dist_all_directions[1] = min(front_range)
    dist_all_directions[2] = min(left_range)
    return dist_all_directions
        
  

def callback_scan(data):
    """
    This function is used for stop the robot when the robot face an obstical in any direction
    
    args:
        data(float):data which the robot gets from laser scanner 
 
    
    """
    global assigned
    
    pub = rospy.Publisher('cmd_vel',Twist, queue_size=10)
    #Calculate the minimun obstacle distances in the whole directions (right , left and front)
    param_flag = rospy.get_param("/obstical_avoidance_with_keyboard")
    dist_all_directions = find_min_dist(data.ranges)
    if param_flag :
        if dist_all_directions[0] < min_dist :
            if assigned.angular.z < 0 :
                #don't turn right  
                assigned.angular.z = 0    
        if dist_all_directions[1] < min_dist:
            if assigned.linear.x > 0 :
                #dont' go forward to the obstacle
                assigned.linear.x = 0
        if dist_all_directions[2] < min_dist :
            if assigned.angular.z > 0 :
                #don't move left
                assigned.angular.z = 0
    pub.publish(assigned)
    





#copy rmap udate from cmd_vel in the global variable which is modified by the controller 

def callback_map_update(data):
    """
    This function is used for updating the global variable with new controller input
    
    args:
        data(float):data which the robot gets from laser scanner 
 
    
    """
    global assigned
    #update the global variable with new controller input 
    
    assigned = data        
  
    
    
#main 
if __name__=="__main__":
    rospy.init_node('keyboard_interface_node')
    #subscriber to topic map_update_cmd_vel    
    rospy.Subscriber("/map_update_cmd_vel", Twist, callback_map_update)
    #subscriber to topic scan
    rospy.Subscriber("/scan", LaserScan, callback_scan)
    rospy.spin()
