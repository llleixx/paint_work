from util import *


class Element:
    def __init__(self, x, y, width, height, *, port_num: list = [16, 16], port_start_num: list = [1, 17]):
        self.port_num = port_num
        self.port_start_num = port_start_num
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_port_relative_position(self, port_index: int) -> tuple[int, int]:
        port_x = 0
        port_y = 0
        vertical_direction = DOWN
        if port_index >= self.port_start_num[1]:
            vertical_direction = TOP
            port_y = self.height

        interval = self.width / (self.port_num[vertical_direction] + 1)
        port_x = (port_index - self.port_start_num[vertical_direction] + 1) * interval
        return (port_x, port_y)


    def get_port_position(self, port_index: int):
        port_relative_position = self.get_port_relative_position(port_index)
        return (self.x + port_relative_position[0], self.y + port_relative_position[1])
