"""
概念：多重继承，指的是继承一个类同时继承多个父类，从而拥有多个父类的属性和方法
"""
#定义Person类
class Person:
    #定义初始化方法
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    #定义实例方法
    def speak(self, msg):
        print(f'我叫{self.name},我的年龄是{self.age},我是{self.gender}性,我想说{msg}')

#定义Worker类
class Worker:
    def __init__(self, company):
        self.company = company
    def do_work(self):
        print(f'我在{self.company}做兼职')

#定义Student类,同时继承Person和Worker类
class Student(Person, Worker):
    def __init__(self, name, age, gender, company, stu_id, grade):
        #super().__init__(name, age, gender),这样只能继承Person类的属性
        #正确用法：使用类名，初始化子类
        Person.__init__(self,name, age, gender)
        Worker.__init__(self,company)
        self.stu_id = stu_id
        self.grade = grade
    def study(self):
        print(f'我在努力学习，争取做{self.grade}年级第一名')

#实例化对象
s1 = Student('张三', 20, '女', 'Google', 2025202, '初二')
print(s1.__dict__)
s1.speak('Hello World')
s1.do_work()
s1.study()
"""
我叫张三,我的年龄是20,我是女性,我想说Hello World
我在Google做兼职
我在努力学习，争取做初二年级第一名
"""

#补充：__mro__,用来记录子类属性和方法的继承顺序
#通过实例去查找属性和方法时，会先在实例自身上去查找，如果没有，就按照__mro__记录的顺序去查找
print(Student.__mro__)#(<class '__main__.Student'>, <class '__main__.Person'>, <class '__main__.Worker'>, <class 'object'>)
