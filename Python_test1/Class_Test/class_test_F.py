# 定义一个天山童姥类 ，类名为TongLao
class TongLao:

    # 构造函数：属性有血量，武力值（通过传入的参数得到）
    def __init__(self, my_hp, my_power):
        self.my_hp = my_hp
        self.my_power = my_power

    # see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，
    # 如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
    def see_people(self, name):
        if name == 'WYZ' or name == '无崖子':
            print('%s？ 师弟！！！！' % name)
        elif name == '李秋水':
            print('%s？ 呸，贱人!' % name)
        else:
            print('%s？ 叛徒！我杀了你!!!' % name)

        # fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
        # 需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
    def fight_zms(self, your_hp, your_power):
        my_hp = self.my_hp / 2 - your_power
        your_hp = your_hp - self.my_power * 10
        if your_hp > my_hp:
            print('哼！你居然赢了，算你走运！')
        elif your_hp < my_hp:
            print('哈哈，我赢了')
        else:
            print('算了，放你一马')



