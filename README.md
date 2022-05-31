# Research track2_assignmet_1
This assignment cosists of three parts: 
  1) Research track1_3rd assignment documentation using sphinx.
  2) Robot drive and plot using jupyter.
  3) Research track1_1st assignment statistical analysis.
## 1- Research track1_3rd assignment documentation using sphinx:
  You can find sphinx documentation in this link ([Sphinx documentation](https://husseinfd97.github.io/RT2_assignmet_1/)).
## 2- Robot drive and plot using jupyter:
  **Introduction**\
    This assignment is aimed to use the last assignmet of research track 1 which you can find here([last_assignment](https://github.com/husseinfd97/RT_assignment3.git/)) and control it with GUI then plot the laser scanner sensor output , the position of the robot and histogram of the reached targets with three modes:\
    1) Autonumous driving mode.\
    2) Manual driving mode.\
    3) Manual driving mode with assistance.
    
  **How to run the project**  \
  First , run the launch file simulation_gmapping and move_base

```
roslaunch final_assignment simulation_gmapping.launch
```
```
roslaunch final_assignment move_base.launch
```

Then run the project launch file
```
roslaunch assignment3 main_launcher.launch
```
    
Finally,open the jupyter file
```
User_interface.ipynb
```
    
  **Note**:
To make the scripts excutable in the direction of scripts. 


**How it works** \ 
Once you run the required launch files then the jupyter file and run all cells the main minu appears which has two choices ( case 1:autonomous **or** case2: drive keyboard) then if you choose (autonomous mode)  it waits for the user's input of x , y coordinates and then you should press (start the case) button to use move the robot autonumously to your desired coordinates once it arrived the target the histogram graph shows the reached targets and the coordinates and laser scanner plots will be updates automatically. 
Another mode can be chosen by the user is the manual drive with assitance or without , once you press drive keyboard button 

## 3- Research track1_1st assignment sstatistical analysis:
  
  
[Statestics_RT2.xlsx](https://github.com/husseinfd97/RT2_assignmet_1/files/8804885/Statestics_RT2.xlsx)  \

[RT2_statistics_report.pdf](https://github.com/husseinfd97/RT2_assignmet_1/files/8804891/RT2_statistics_report.pdf)


   

      
