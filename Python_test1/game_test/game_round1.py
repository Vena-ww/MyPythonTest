# 回合制游戏----单轮

def game():
    my_hp = 1000
    my_power = 200
    your_hp = 1000
    your_power = 199
    my_hp = my_hp - your_power
    your_hp = your_hp - my_power

    # 三目运算符
    # print("我赢了") if my_hp > your_hp else print("你赢了")

    if my_hp > your_hp:
        print("我赢了")
    else:
        print("你赢了")


game()
