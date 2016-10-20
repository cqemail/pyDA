# !/usr/bin/python
# -*- coding:utf8 -*-
# __author__ = c08762

"""learn numpy"""

# 基本属性
import numpy as np
# array = np.array([[1,2,3],[4,5,6]])
# print(array)
# print('number of dim(维数):', array.ndim)
# print('shape:', array.shape)
# print('size:', array.size)

# 创建矩阵,可指定矩阵type, 默认为64位
a1 = np.array([2,3,4])
a2 = np.array([[2,3,4],[5,6,7]], dtype=np.int)
# 生成矩阵
a3 = np.zeros((3,4)) # 全0矩阵，参数为shape
a4 = np.ones((5,6), dtype=np.int) # 全1矩阵
a5 = np.empty((2,2))    # 空矩阵，实际为近0值填充
# 生成有序矩阵
a6 = np.arange(10,20) # 生成10-19的一维矩阵(数组)，可指定步长
a7 = np.arange(12).reshape((3,4))   # 指定shape
# 生成线段,包含首尾共n段,段距为(尾-首)/(n-1)
a8 = np.linspace(1,51,6)
a9 = np.linspace(1,51,6).reshape((3,2))
# 生成随机矩阵
a14 = np.random.random_integers(1,20,(3,2))
a15 = np.random.random((2,3))   # 指定shape
# print(a1)
# print(a2.dtype)
# print(a3)
# print(a4)
# print(a5)
# print(a6)
# print(a7)
# print(a8)
# print(a9)
# print(a14)
# print(a15)
# numpy支持的计算
a10 = np.array([10,20,30,40])
a11 = np.arange(4)
# print(a10+a11)  # 加减乘除法对应元素进行相应运算
# print(a10-a11)
# print(a10*a11)
# print(a11/a10)
# print(a10*2)    # 数乘:乘以每个元素
# 对矩阵中的值进行判断，返回bool值
# print(a11,a11<3)
# 矩阵乘法
# a12 = np.array([[1,2,3],[4,5,6]])
# a13 = np.array([[1,2],[3,4],[5,6]])
# print(a12)
# print(a13)
# print(np.dot(a12,a13))    # 与下面的表达式等价
# print(a12.dot(a13))

# print(np.sum(a15))    # 对整个矩阵求和
# print(np.min(a15))   # 求最小值
# print(np.max(a15))   # 求最大值
# print(np.sum(a15,axis=1))   # axis=1 按行求和,求最值
# print(np.min(a15,axis=0))   # axis=0 按列求和,求最值

# print(np.argmin(a15))   # 最小值的索引,从0开始,先行后列
# print(np.argmax(a15))   # 最大值的索引,base 0
# print(np.mean(a15))     # 平均值
# print(a15.mean())       # 平均值
# print(np.average(a15))  # 平均值
# print(np.median(a15))   # 中位数
print(a2)
# print(np.cumsum(a2))     #
# print(np.diff(a2))
# print(np.nonzero(a2))
# print(np.sort(a2))  # 逐行排序
# print(np.transpose(a2))   # 转置
# print(a2.transpose())     # 转置
#print(a2.T)     # 转置
print(np.clip(a2,4,5))      # <min置为min,>max置为max
