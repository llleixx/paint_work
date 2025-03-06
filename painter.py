import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
from matplotlib.patches import Rectangle

from group import Group


class Painter:
    def __init__(self, flows = None):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(-675, 675)
        self.ax.set_ylim(-675, 675)
        self.ax.set_aspect('equal')
        plt.axis('off')
        # ax.grid(True)

        self.groups = []

        self.groups.append(Group(-225, -675, 450, 450, rotate_angle=0))
        self.groups.append(Group(675, -225, 450, 450, rotate_angle=90))
        self.groups.append(Group(225, 675, 450, 450, rotate_angle=180))
        self.groups.append(Group(-675, 225, 450, 450, rotate_angle=270))

        for group in self.groups:
            for row_elements in group.elements:
                for element in row_elements:
                    rect = Rectangle((element.x, element.y), element.width, element.height,
                        linewidth=2, edgecolor='r', facecolor='none')
                    
                    rect.set_transform(group.transform + self.ax.transData)
                    self.ax.add_patch(rect)



        if flows is not None:
            self.connect(flows)
    
    def connect(self, flows):
        # TODO: implement this function
        pass

    def show(self):
        plt.show()
    
    def to_picture(self, path):
        plt.savefig(path)

painter = Painter()

painter.show()