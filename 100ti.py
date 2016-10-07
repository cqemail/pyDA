# !/usr/bin/python
# -*- coding:utf8 -*-
# __author__ = c08762

"""编程语言入门经典100题(Python版)"""

import math
import datetime
import time


# 【程序1】题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
def py_001():
    cnt = 0  # count the sum of result
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if i != j and i != k and j != k:
                    print(i * 100 + j * 10 + k)
                    cnt += 1
    print('可以组成互不相同且无重复数字的三位数 %d 个' % cnt)


# 【程序2】题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
def py_002():
    i = int(input('Enter the profit:'))
    arr = [1000000, 600000, 400000, 200000, 100000, 0]
    rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    r = 0
    for idx in range(0, 6):
        if i > arr[idx]:
            r += (i - arr[idx]) * rat[idx]
            print((i - arr[idx]) * rat[idx])
            i = arr[idx]
    print(r)


# 【程序3】题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
def py_003():
    num = 1
    while True:
        if math.sqrt(num + 100) - int(math.sqrt(num + 100)) == 0 and math.sqrt(num + 268) - int(
                math.sqrt(num + 268)) == 0:
            print(num)
            break
        num += 1


# 【程序4】题目：输入某年某月某日，判断这一天是这一年的第几天？
def py_004():
    dtstr = str(input('Enter the datetime:(20151215):'))
    dt = datetime.datetime.strptime(dtstr, "%Y%m%d")
    another_dtstr = dtstr[:4] + '0101'
    another_dt = datetime.datetime.strptime(another_dtstr, "%Y%m%d")
    print(int((dt - another_dt).days) + 1)


if __name__ == '__main__':
    py_004()
