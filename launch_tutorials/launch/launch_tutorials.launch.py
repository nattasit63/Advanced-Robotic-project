
from launch import LaunchDescription
from launch.actions import ExecuteProcess
import os
import time
import random


def listNodeAvailable():
    stringnodeList=os.popen('ros2 node list').read()
    listt= stringnodeList.split("\n")
    listt=listt[0:len(listt)-1]
    listt=list(dict.fromkeys(listt))
    return listt
def IsNodeAvaiable(Nodename):
    listAva=listNodeAvailable()
    for i in range(0,len(listAva)):
        if(listAva[i]==Nodename):
            return 1 
    return 0
def WaitNodeAvaiable(Nodename,timeout):
    timestamp=time.time()
    while True:
        if(IsNodeAvaiable(Nodename)):
            return 1
        elif(time.time()-timestamp >= timeout):
            return 0

def RunNode(pkgName,Nodename):
    try:
        os.popen("ros2 run "+pkgName+" "+Nodename)
    except:
        #run fail
        return 0 
    return 1 

def generate_launch_description():
    Alltaskdone=False
    state=0
    while not Alltaskdone:
        if(state==0):
            RunNode("turtlesim","turtlesim_node")
            state=1
        elif(state==1):
            flag=WaitNodeAvaiable("/turtlesim",10)
            if(flag == 1 ):
                state=2
            else:
                state=0 #reopen node
        elif(state==2):
            RunNode("launch_tutorials","viapointservice_node")
            state=3
        elif(state==3):
            flag=WaitNodeAvaiable("/goVp_service",10)
            if(flag == 1 ):
                state=4
            else:
                state=2 #try run node again
        elif(state==4):
            os.popen("ros2 service call /GotoVp interfaces_tutorials/srv/Govp \"{x: "+str(1+random.uniform(0, 1)*8.5) + ",y: " +str(1+random.uniform(0, 1)*8.5) +"}\"")
            
            state=5
        elif(state==5): 
            timestamp=time.time()
            while 1:
                if(time.time()-timestamp>=5):#wait 5 s
                    break
                print(time.time()-timestamp)
            state=6
        elif(state==6):
            flag=IsNodeAvaiable("/goVp_service")
            if(flag==0):
                print('Turtle Win')
                break
            else:
                print('Turtle Lose')
                os.system('ros2 service call /kill turtlesim/srv/Kill "{name: turtle1}"')
                os.popen('ros2 service call /spawn turtlesim/srv/Spawn "{x: 5.4445, y: 5.4445, theta: 0.2, name: '"turtle1"'}"')
                print('New turtle born')
                state=2
       
    spawn_turtle_condition= ExecuteProcess( cmd=[['ros2 service call /spawn turtlesim/srv/Spawn "{x: 2, y: 2, theta: 0.2, name: '"turtleWin"'}"',]] , shell=True)
    return LaunchDescription([spawn_turtle_condition] )


