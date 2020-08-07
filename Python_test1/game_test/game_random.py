# -*- coding: utf-8 -*-

import random


# 多轮游戏
def fight():
    my_hp = 1000
    my_power = random.randint(50, 200)
    your_hp = 1000
    your_power = random.randint(50, 200)

    while True:
        my_hp = my_hp - your_power
        your_hp = your_hp - my_power
        print("你的hp:{},我的hp:{}".format(your_hp, my_hp))
        # print(f"我的hp:", my_hp, end='')

        if my_hp <= 0:
            print("我输了")
            break
        elif your_hp <= 0:
            print("你输了")
            break


fight()
