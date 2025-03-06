import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
from matplotlib.patches import Rectangle

# 显式创建坐标轴
fig, ax = plt.subplots()

# 创建矩形对象（未旋转时的位置）
rect0 = Rectangle((-225, -675), 450, 450, 
                 linewidth=2, edgecolor='r', facecolor='none')

rect1 = Rectangle((675, -225), 450, 450, 
                 linewidth=2, edgecolor='r', facecolor='none')

rect2 = Rectangle((225, 675), 450, 450, 
                 linewidth=2, edgecolor='r', facecolor='none')

rect3 = Rectangle((-675, 225), 450, 450, 
                 linewidth=2, edgecolor='r', facecolor='none')

# 创建组合变换：平移中心到原点 → 旋转 → 平移回原位
transform0 = (
    ax.transData                    # 结合数据坐标系
)


transform1 = (
    transforms.Affine2D()
    .translate(-675, 225)  # 移动到原点
    .rotate_deg(90)                # 旋转
    .translate(675, -225)    # 移回原位置
    + ax.transData                    # 结合数据坐标系
)

transform2 = (
    transforms.Affine2D()
    .translate(-225, -675)  # 移动到原点
    .rotate_deg(180)                # 旋转
    .translate(225, 675)    # 移回原位置
    + ax.transData                    # 结合数据坐标系
)

transform3 = (
    transforms.Affine2D()
    .translate(675, -225)  # 移动到原点
    .rotate_deg(270)                # 旋转
    .translate(-675, 225)    # 移回原位置
    + ax.transData                    # 结合数据坐标系
)
# 应用变换并添加到图形
rect0.set_transform(transform0)
rect1.set_transform(transform1)
rect2.set_transform(transform2)
rect3.set_transform(transform3)
ax.add_patch(rect0)  # 使用 ax 添加矩形
ax.add_patch(rect1)  # 使用 ax 添加矩形
ax.add_patch(rect2)  # 使用 ax 添加矩形
ax.add_patch(rect3)  # 使用 ax 添加矩形

# 设置坐标轴范围和比例
ax.set_xlim(-675, 675)
ax.set_ylim(-675, 675)
ax.set_aspect('equal')
# ax.grid(True)
plt.axis('off')
plt.show()