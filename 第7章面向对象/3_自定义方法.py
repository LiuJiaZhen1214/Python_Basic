"""通过自定义方法，给实例添加行为"""
#定义一个Person类
class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.age = age
        self.gender = gender
    #自定义方法：给实例添加行为
    #speak方法收到的参数是：调用speak方法的实例对象(self)、其他参数
    #speak方法只有一份，保存在Person类身上的，所有Person类的实例对象，都可以调用speak方法
    def speak(self, msg):
        print(f'{self.name}说:\"我的年龄是{self.age},我的性别是{self.gender},我的姓名是{self.name},我想说{msg}\"')

#实例化一个对象
p1 = Person('张三', '男', 30)
print(p1)
p1.speak('我爱中国')#张三说:"我的年龄是30,我的性别是男,我的姓名是张三,我想说我爱中国"

p3 = Person('p3', '男', 40)
p4 = Person('p4', '女', 30)
#所有的实例化对象都可以调用类的speak()方法
#当执行p3.speak()时，查找speak方法的过程:1.实例对象自身(p1) =>（如果实例对象没有该方法） 2.实例的"缔造者",类的身上去找方法
#验证一下查找过程
def speak():
    print("123654789oknkjs")
p3.speak = speak
print(Person.__dict__)
p3.speak()#123654789oknkjs
p4.speak('hhhh')#p4说:"我的年龄是30,我的性别是女,我的姓名是p4,我想说hhhh"
