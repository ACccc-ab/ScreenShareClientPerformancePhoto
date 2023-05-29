import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["SimHei"]



import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

# 数据
x_labels = ['非投屏状态运存占用', '投屏状态运存占用', '投屏状态CPU占用', '投屏状态GPU占用', 'BYOM外设开启运存占用', 'BYOM外设开启CPU占用']
x = np.arange(len(x_labels))
width = 0.08

intel_57 = [47, 188.1, 3.6, 18.4, 100, 5.8]
intel_58 = [44, 154.3, 1.7, 14.3, 106.3, 4.7]
amd_57 = [36.5, 102.6, 6.1, 20.5, 63.4, 15.1]
amd_58 = [32.6, 61.2, 2.5, 15, 67, 12.3]
intel_mac_57 = [50.4, 101.2, 48, 8.2, 89.2, 78.6]
intel_mac_58 = [51.4, 92.4, 45.9, 9.4, 94.7, 76.5]
m_mac_57 = [126, 468.4, 69.2, 20.5, 380.5, 76.7]
m_mac_58 = [123.2, 327.3, 66.3, 19.3, 335.7, 76.6]

# 创建子图
fig, ax = plt.subplots(figsize=(12, 6))

# 绘制柱状图
rects1 = ax.bar(x - width, intel_57, width, label='5.7版本【Intel】')
rects2 = ax.bar(x, intel_58, width, label='5.8版本【Intel】')
rects3 = ax.bar(x + width, amd_57, width, label='5.7版本【AMD】')
rects4 = ax.bar(x + 2 * width, amd_58, width, label='5.8版本【AMD】')
rects5 = ax.bar(x + 3 * width, intel_mac_57, width, label='5.7版本【Intel-Mac】')
rects6 = ax.bar(x + 4 * width, intel_mac_58, width, label='5.8版本【Intel-Mac】')
rects7 = ax.bar(x + 5 * width, m_mac_57, width, label='5.7版本【M-Mac】')
rects8 = ax.bar(x + 6 * width, m_mac_58, width, label='5.8版本【M-Mac】')

# 设置柱状图标签
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height), xy=(rect.get_x() + rect.get_width() / 5, height), xytext=(5, 3), textcoords="offset points", ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
autolabel(rects5)
autolabel(rects6)
autolabel(rects7)
autolabel(rects8)

# 设置图表参数
ax.set_xlabel('性能场景指标')
ax.set_ylabel('数值')
ax.set_title('5.7版本和5.8版本不同场景下的优化对比（分组柱状图）')
ax.set_xticks(x + 2 * width)
ax.set_xticklabels(x_labels, rotation=45)
ax.legend()
ax.grid(True)

plt.tight_layout()
plt.show()
