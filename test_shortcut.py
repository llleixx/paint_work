import matplotlib.pyplot as plt


def on_scroll(event):
    # 检查是否按下Ctrl键（兼容不同系统的修饰键名称）
    modifiers = event.modifiers if event.modifiers else set()
    if not ({'ctrl', 'control'} & modifiers):  # 检查是否包含ctrl或control
        return
    if event.inaxes is None:
        return
    
    # 确定缩放方向
    scale_factor = 0.9 if event.step > 0 else 1.1
    
    ax = event.inaxes
    x, y = event.xdata, event.ydata
    
    # 计算新的坐标范围（以鼠标位置为中心）
    def adjust_lim(current_lim, cursor_pos, scale):
        new_length = (current_lim[1] - current_lim[0]) * scale
        low = cursor_pos - (cursor_pos - current_lim[0]) * scale
        high = cursor_pos + (current_lim[1] - cursor_pos) * scale
        return (low, high)
    
    ax.set_xlim(adjust_lim(ax.get_xlim(), x, scale_factor))
    ax.set_ylim(adjust_lim(ax.get_ylim(), y, scale_factor))
    ax.figure.canvas.draw_idle()

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 3, 2])
fig.canvas.mpl_connect('scroll_event', on_scroll)
plt.show()