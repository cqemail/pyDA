# -*- coding:utf-8 -*-
# __author = 'c08762'

"""学习异常处理"""


def ab(x):
    try:
        return int(x)
    # 可以将捕获到的异常，绑定一个异常实例
    except ValueError as err:
        print(type(err))
        print('Catch a Value Error: {}'.format(err))


print(ab(3))

while True:
    try:
        num = int(input('Pls Enter an integer between 0 & 100:\n'))
    except ValueError:
        print("NOT a number, try again:\n")
    else:
        if num > 100 or num < 0:
            print('{} is beyond boundaries, try again:\n'.format(num))
            break
        else:
            print('its')

raise NameError('good')
