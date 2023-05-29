import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["SimHei"] # 字体

versions = ['Intel', 'AMD', 'Intel-Mac', 'M-Mac']
memory_usage_57 = [47, 36.5, 50.4, 126]
memory_usage_58 = [44, 32.6, 51.4, 123.2]


bar_width = 0.3  # 调整柱子的宽度
gap = 0.03  # 调整柱子之间的间隔
index = np.arange(len(versions))

color_57 = 'blue'
color_58 = 'red'

plt.bar(index, memory_usage_57, bar_width + gap, label='5.7版本')
plt.bar(index + bar_width + gap, memory_usage_58, bar_width, label='5.8版本')

# 在柱子上显示数值
for i in range(len(versions)):
    plt.text(index[i], memory_usage_57[i], str(memory_usage_57[i]) + 'MB', ha='center', va='bottom')
    plt.text(index[i] + bar_width + gap, memory_usage_58[i], str(memory_usage_58[i]) + 'MB', ha='center', va='bottom')

plt.xlabel('设备版本')
plt.ylabel('运存占用 (MB)')
plt.title('5.7版本和5.8版本非投屏状态下运存占用对比')
plt.xticks(index + bar_width / 2, versions)
plt.legend()

plt.tight_layout()
plt.show()

