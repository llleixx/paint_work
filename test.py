import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
from matplotlib.patches import Rectangle

# 定义旋转中心、矩形参数和旋转角度
center_x, center_y = 2, 3  # 中心点坐标
width, height = 4, 2       # 矩形的宽度和高度
angle = 30                 # 旋转角度（度数）

# 计算左下角坐标（基于中心点）
lower_left = (center_x - width/2, center_y - height/2)

# 创建矩形对象（未旋转时的位置）
rect = Rectangle(lower_left, width, height, 
                 linewidth=2, edgecolor='r', facecolor='none')

# 创建组合变换：平移中心到原点 → 旋转 → 平移回原位
transform = (
    transforms.Affine2D()
    .translate(-center_x, -center_y)  # 移动到原点
    .rotate_deg(angle)                # 旋转
    .translate(center_x, center_y)    # 移回原位置
    + plt.gca().transData             # 结合数据坐标系
)

# 应用变换并添加到图形
rect.set_transform(transform)
plt.gca().add_patch(rect)

# 设置坐标轴范围和比例
plt.xlim(0, 4)
plt.ylim(0, 6)
plt.gca().set_aspect('equal')
plt.grid(True)
plt.show()