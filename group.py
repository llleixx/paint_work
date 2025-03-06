from matplotlib import transforms

from element import Element
from util import transform


class Group:
    def __init__(self, x, y, width, height, *, rotate_angle):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotate_angle = rotate_angle
        self.row_num = 3
        self.elements = [[] for _ in range(self.row_num)]
        self.transform = (
            transforms.Affine2D()
            .rotate_deg(rotate_angle)                # 旋转
            .translate(x, y)    # 移回原位置
        )
        
        self.elements[0].append(Element(20, 40, 170, 50, port_num=[16, 16], port_start_num=[1, 17]))
        self.elements[0].append(Element(260, 40, 170, 50, port_num=[16, 16], port_start_num=[1, 17]))

        self.elements[1].append(Element(20, 200, 170, 50, port_num=[16, 16], port_start_num=[1, 17]))
        self.elements[1].append(Element(260, 200, 170, 50, port_num=[16, 16], port_start_num=[1, 17]))

        self.elements[2].append(Element(20, 360, 170, 50, port_num=[16, 16], port_start_num=[1, 17]))
        self.elements[2].append(Element(260, 360, 170, 50, port_num=[16, 16], port_start_num=[1, 17]))
        # self.elements[0].apppend()
    
    def relative_position_to_absolute_position(self, relative_position):
        return transform((self.x, self.y), self.rotate_angle, relative_position)

        
    def get_port_positioin(self, row, col, port_index):
        element = self.elements[row][col]
        port_relative_position = element.get_port_relative_position(port_index)
        return self.relative_position_to_absolute_position(port_relative_position)