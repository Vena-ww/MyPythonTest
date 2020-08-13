from MyPythonTest.Python_test1.Class_Test.class_test_F import TongLao
import random

# 定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。
# 所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
class XuZhu(TongLao):

    def __init__(self):
        super()

    def read(self):
        print('你们不要打了，罪过罪过罪过')


# 实例化类
tonglao = TongLao(1000, random.randint(50, 200))
# 实例调用类方法，使用choice（）随机选择列表中的一个元素作为参数
tonglao.see_people(random.choice(['WYZ', '无崖子', '李秋水', '丁春秋']))
# 传入敌人的血量和武力值
tonglao.fight_zms(1000, random.randint(50, 200))

# 调用子类
xuzhu = XuZhu()
xuzhu.read()
