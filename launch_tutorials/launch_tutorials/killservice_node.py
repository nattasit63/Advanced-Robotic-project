import rclpy
from rclpy.node import Node
from turtlesim.srv import Kill

class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('turtle_client_async')
        self.cli = self.create_client(Kill, 'kill')
        while not self.cli.wait_for_service(timeout_sec=10):
            self.get_logger().info('service not available, waiting again...')
        self.req = Kill.Request()

    def send_request(self, name):
        self.req.name=name
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main():
    rclpy.init()

    minimal_client = MinimalClientAsync()
    response = minimal_client.send_request("turtle1")
    minimal_client.destroy_node()
    rclpy.shutdown()
    minimal_client.get_logger().info('Node destroy')


if __name__ == '__main__':
    main()