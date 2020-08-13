# 用类和面向对象的思想，“描述”生活中任意接触到的东西
# （比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。
class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print(f'{self.age}的{self.name}工作相当努力。')

person1 = Human(age='22', name='Lulu')
person1.work()

print('-' * 50)

class Someone:
    name = '类的属性'

    def play(self):
        return '类中方法'

s1 = Someone()
print('这是：', s1.name)
print('这是：', s1.play())

print('-' * 50)

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def disEmployee(self):
        print('Name: ', self.name, 'Salary: ', self.salary)

emp1 = Employee('Vivian', 7000)
emp1.disEmployee()

emp2 = Employee('Lily', 6500)
emp2.disEmployee()

print('-' * 50)

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self, color):
        self.color = color
        print(self.name + f'在{self.color}的地毯上练习坐下.')

# 继承父类所有的属性和方法
class Dog(Animal):
    pass

# 重写父类的方法
class Cat(Animal):
    def sit(self):
        print(f'{self.age}岁的{self.name}在休息')

# 父类的实例化
dog = Animal('狗狗', 3)
dog.sit('蓝色')

cat = Animal(age=2, name='猫咪')
cat.sit('粉色')

# 子类继承后的实例化
jinmao = Dog('小金', 3)
print(jinmao.name)
jinmao.sit('灰色')

# 重写父类方法后的实例化
xiaobai = Cat('小白猫', 2)
xiaobai.sit()


