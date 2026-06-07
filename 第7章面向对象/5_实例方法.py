"""实例方法"""
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    #自定义方法：给实例添加行为
    #speak方法收到的参数是：调用speak方法的实例对象(self)、其他参数
    #speak方法只有一份，保存在Person类身上的，所有Person类的实例对象，都可以调用speak方法
    def speak(self, msg):
        print(f'{self.name}说:\"我的年龄是{self.age},我的性别是{self.gender},我的姓名是{self.name},我想说{msg}\"')
    #定义实例方法
    def run(self, distance):
        print(f'{self.name}奔跑了{distance}米！')

#创建Person类的实例对象
p1 = Person('张三', 18, '男')
p2 = Person('李四', 22, '女')

#通过实例调用实例方法
p1.speak('你好')
p1.run(300)

#通过类去调用实例方法(能调用，但不推荐)
Person.run(p2,100)#李四奔跑了100米！
