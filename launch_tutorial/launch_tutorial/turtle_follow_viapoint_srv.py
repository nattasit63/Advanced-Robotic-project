from launch_service.srv import SetGoal
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
import numpy as np
import math
from geometry_msgs.msg import Twist

class goVp(Node):

    def __init__(self):
        super().__init__('goVp_service')
        self.srv = self.create_service(SetGoal, 'GotoVp', self.toVp)
        self.run = True
        self.k_v = 5.0
        self.k_w = 3.0
        self.dist = 0
        self.subscription = self.create_subscription(Pose,'turtle1/pose',self.pose_callback,10)
        self.subscription
        self.pose = Pose()
        self.original = np.array([5.544445,5.544445])
        self.goal = np.array([5.544445,5.544445])
        self.publisher= self.create_publisher(Twist,'turtle1/cmd_vel',10)
        self.publisher
        self.timeStamp=0
        timer_period = 0.0005
        self.timer = self.create_timer(timer_period,self.timer_callback)
        self.state = 0


    def timer_callback(self):
        self.publish_cmd_vel()

    def pose_callback(self,msg):
        self.pose = msg
        return self.pose
     
    def toVp(self, request, response):
        self.run=1
        self.get_logger().info('Go to (X:'+ str(request.x)+",Y:"+str(request.y)+")")
        
        self.goal[0]=request.x
        self.goal[1]=request.y

        return response
    
    
        
    def control(self):
        msg=Twist()
        dp = self.goal-np.array([self.pose.x,self.pose.y])
        self.dist = np.linalg.norm(dp)
        self.v=0.0
        self.w=0.0
        e = math.atan2(dp[1],dp[0])-self.pose.theta        
        if abs(e)<0.05:
                self.w=0.0
                self.publisher.publish(msg)
                if self.dist <0.1 and self.goal[0]!=5.544445:
                    self.v=0.0
          
                    msg.linear.x = float(self.v)
  
                    self.publisher.publish(msg)
                    # self.state=1
                    print('YESS')
                    print(self.pose.x,self.pose.y)
                    try:
                        self.destroy_service()
                        self.destroy_node()
                    except:
                        exit()
                else:
                    self.v = self.k_v
                    msg.linear.x = float(self.v)
                    self.publisher.publish(msg)
                    
        else:
                self.w = self.k_w*math.atan2(math.sin(e),math.cos(e))
                msg.angular.z = self.w
                self.publisher.publish(msg)

        return self.v,self.w

    
   

        
    def publish_cmd_vel(self):
        self.control()
        msg=Twist()
        msg.linear.x = float(self.v)
        msg.angular.z = float(self.w)
        self.publisher.publish(msg)
  

def main():
    rclpy.init()

    go_Vp = goVp()

    rclpy.spin(go_Vp)

    rclpy.shutdown()


if __name__ == '__main__':
    main()