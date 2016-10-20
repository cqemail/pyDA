# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = c08762

"""learn matplotlib"""

import numpy as np
import matplotlib.pyplot as plt     # 惯用别名
x = np.linspace(0, 10, 1000)
y = np.sin(x) + 1
z = np.cos(x**2) + 1
plt.rcParams['font.sans-serif'] = ['SimHei']    # 中文支持
plt.rcParams['axes.unicode_minus'] = False      # 解决保存图像时负号'-'显示为方块的问题
plt.figure(figsize=(10, 5))  # 设置图像大小
plt.plot(x, y, label='$\sin x+1$', color='red', linewidth=2)    # 作图，设置标签，线条颜色和大小
plt.plot(x, z, 'b--', label='$\cos x^2+1$')     # 作图，设置标签，线条类型
plt.xlabel('Time(s)')       # x轴名称
plt.ylabel('Volt 值')          # y轴名称
plt.title('A Simple Example')       # 标题
plt.ylim(0, 2.2)    # 显示的y轴范围
plt.legend()        # 显示图例
plt.show()          # 显示作图结果
