# -*- coding:utf-8 -*-
# __author = 'c08762'

"""输入1个数，输出不大于该数的所有质数"""

from math import sqrt


def is_prime(n):
    """This function return a number is a prime or not"""
    assert n >= 2
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def get_num():
    """This function get a integer greater than 1 from input"""
    while True:
        try:
            num = int(input('Pls enter a integer greater than 1:\n'))
        except ValueError:
            print("NOT a number, try again:\n")
            continue
        if num <= 1:
            print('NOT greater than 1, try again:\n')
            continue
        return num


def put_prime(numb):
    for x in range(2, numb+1):
        if is_prime(x):
            print(x, end=',')

if __name__ == '__main__':
    put_prime(get_num())
