import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
from matplotlib.patches import Rectangle

# 显式创建坐标轴
fig, ax = plt.subplots()

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
    + ax.transData                    # 结合数据坐标系
)

# 应用变换并添加到图形
rect.set_transform(transform)
ax.add_patch(rect)  # 使用 ax 添加矩形

# 设置坐标轴范围和比例
ax.set_xlim(0, 4)
ax.set_ylim(0, 6)
ax.set_aspect('equal')
ax.grid(True)
plt.show()