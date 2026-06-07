"""静态方法"""
from datetime import datetime
class Person:
    #类的初始化方法
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    #静态方法
    #使用@staticmethod装饰过的方法，就叫：静态方法，它保存在类身上
    #静态方法只是单纯地定义在类中，它不会收到：self、cls参数，它收到的参数都是自定义参数
    #由于静态方法没有收到:self、cls参数，所以其内部不会访问任何：类和实例相关的内容
    #静态方法通常用于定义：与类相关的工具方法
    @staticmethod
    def is_adult(year):
        current_year = datetime.now().year
        age = current_year - year
        #返回结果(成年：True,未成年：False)
        return age >= 18

    @staticmethod
    def mask_idcard(idcard):
        return idcard[:6]+'********'+idcard[-4:]

#验证一下：静态方法是否保存在类身上
print(Person.__dict__)

#静态方法需要通过类去调用
res = Person.is_adult(1983)
print(res)#True
res1 = Person.mask_idcard('123456789123456789')
print(res1)#123456********6789

#注意：通过实例对象也能调用静态方法，但非常不推荐
