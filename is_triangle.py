# -*- coding:utf-8 -*-
# __author = 'c08762'

"""输入3个数，判断能否组成三角形"""

def is_positive(numb):
    """输入合法性检查，必须输入正数，不支持科学计数法"""
    try:
        float(numb)
    except:
        return False
    else:
        if float(numb) <= 0:
            return False
        else:
            return True


def is_pythagoras(a, b, c):
    """直角三角形判断"""
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else:
        return False

num_1 = input("Pls enter the 1st number:\n")
while not is_positive(num_1):
    num_1 = input("That's not a valid number, try again:\n")

num_2 = input("Pls enter the 2nd number:\n")
while not is_positive(num_2):
    num_2 = input("That's not a valid number, try again:\n")

num_3 = input("Pls enter the 3rd number:\n")
while not is_positive(num_3):
    num_3 = input("That's not a valid number, try again:\n")

# 将输入的字符串转换为数字，并用copy进行计算
num1 = float(num_1)
num2 = float(num_2)
num3 = float(num_3)

if num1 + num2 > num3 and num2 + num3 > num1 and num1 + num3 > num2:
    if num1 == num2 == num3:
        print("{}\n{}\n{}\n可以组成等边三角形" .format( num_1,num_2,num_3))
    elif num1 == num2 or num1 == num3 or num2 == num3:
        if is_pythagoras(num1,num2,num3):
            print("{}\n{}\n{}\n可以组成等腰直角三角形".format(num_1, num_2, num_3))
        else:
            print("{}\n{}\n{}\n可以组成等腰三角形".format(num_1, num_2, num_3))
    elif is_pythagoras(num1,num2,num3):
        print("{}\n{}\n{}\n可以组成直角三角形".format(num_1, num_2, num_3))
    else:
        print("{}\n{}\n{}\n可以组成普通三角形".format(num_1, num_2, num_3))
else:
    print("{}\n{}\n{}\n不能组成三角形".format(num_1, num_2, num_3))
