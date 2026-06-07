"""类的方法"""
from datetime import datetime
class Person:
    #类的属性
    max_age = 120
    planet = '地球'
    #类的初始化方法
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # speak方法只有一份，保存在Person类身上的，所有Person类的实例对象，都可以调用speak方法
    def speak(self, msg):
        print(f'{self.name}说:\"我的年龄是{self.age},我的性别是{self.gender},我的姓名是{self.name},我想说{msg}\"')

    def run(self, distance):
        print(f'{self.name}奔跑了{distance}米')

    #使用@classmethod装饰过的方法，就叫：类方法，类方法保存在身上
    #类方法收到的参数：当前类(cls)，自定义参数
    #因为收到了cls的参数，所以类方法中是可以访问类属性的
    #类方法通常用于实现：与类相关的逻辑，例如：操作类级别的信息、一些工厂方法

    @classmethod#使用该装饰器修饰类方法，归类所有
    def change_planet(cls, value):
        #在类方法内，操作类的属性
        cls.planet = value

    #工厂方法，通过调用类的方法来实例化一个对象
    @classmethod
    def create(cls, info_str):
        #从info_str中获取到有效信息
        name, year, gender = info_str.split('-')
        #获取当前的年份和对象年龄
        current_year = datetime.now().year
        age = current_year - int(year)
        #创建并返回一个实例化对象
        return cls(name,age,gender)

#验证一下：类方法保存在类身上
print(Person.__dict__)
Person.change_planet('月球')
#实例化类对象
p1 = Person('张三', 18, '男')
p2 = Person('李四', 20, '女')

#验证一下：类属性planet已经被修改了
print(p1.planet)#月球
print(p2.planet)#月球

#验证一下：测试一下类方法
p3 = Person.create('李华-2003-女')
p3.speak('你好')#李华说:"我的年龄是23,我的性别是女,我的姓名是李华,我想说你好"

