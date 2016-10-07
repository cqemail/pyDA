# -*- coding:utf-8 -*-
# __author = 'c08762'

"""随机生成[0,100]间的一个数，猜这个数，并会提示大了小了"""

import random


def guess_number():
    rand = random.randint(0, 100)
    # 开启作弊
    # print(rand)
    count = 1
    while True:
        if count > 5:
            print('You have tried {} times!'.format(count - 1))
        if count > 9:
            print('You are so stupid!')
            break
        try:
            num = int(input('Pls enter an integer between 0 & 100:\n'))
        except ValueError:
            print("NOT a number, try again:\n")
            continue
            # 这里使用了continue语句进行下一次循环，跳过下面的数字判断代码
            # 也可将数字判断代码作为try的else语句，而达到continue一样的效果
        if num > 100 or num < 0:
            print('{} is beyond boundaries, try again:\n'.format(num))
            continue
        elif num < rand:
            print('{} is smaller'.format(num))
            count += 1
        elif num > rand:
            print('{} is bigger'.format(num))
            count += 1
        else:
            if count == 1:
                print("""\
       ████████████　　　　　　　
　　　██　　　◥██◤　　██　　　　
　◢███　　　　◥◤　　　██◣
　▊▎██◣　　　　　　　◢█▊ ▊　　　
　▊▎██◤　●　　●　  ◥█▊ ▊
  ▊　██　　　　　　　　　█▊ ▊ 　　
　◥▇██　▊　　　　　 ▊ █▇◤
　　　██　◥▆▄▄▄▆◤　█▊　　　◢▇▇◣
◢██◥◥▆▅▄▂▂▂▄▅▆███◣　▊◢╳█
█╳　　　　　　　　　　　　　　　╳█◥◤◢◤
 █◣　　　⊕　　　　　⊕　　　  ◢█◤ ◢◤　
　　▊　　 　　 █ ◢◤　 　　 ╳▊╳ ◢◤
　　▊　　 　　　　　 　 　　　▊╳◢◤
　　▊　　　 　⊕　⊕　　　　█▇◤　　　
　◢█▇▆▆▆▅▅▅▆▆▆▇█◣　　　　　　　
　▊　▂　▊　　　　　　▊　▂　▊　　　　　　　
　◥▆▆▆◤　　　　　　◥▆▆▆◤""")
                print('Unbelievable!', end=' ')
            elif count <= 3:
                print('Awesome!', end=' ')
            else:
                print('Great!', end=' ')
            print('{} is the right number.'.format(num))
            print('You tried {} times.'.format(count))
            break


guess_number()
print('-'*15+'GAME OVER'+'-'*15)
