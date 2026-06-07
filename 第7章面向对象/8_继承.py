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

#定义一个Student类(子类、派生类)，继承自Person类(父类、超类、基类)
class Student(Person):#Student类继承Person类的所有属性和方法
    #如果该类不再定义新的属性和方法，什么都不写，可以写个pass
    #pass

    #如果想在Student类里面新增属性，需要新建__init__方法
    def __init__(self, name, age, gender, stu_id, grade):
        #方式1
        #通过super语法调用父类的init方法，来实现对继承自父类的属性的初始化的操作
        super().__init__(name,age,gender)
        #方式2（不推荐）
        #Person.__init__(self,name,age,gender)

        #子类新增的独有属性，需要自己手动完成初始化
        self.stu_id = stu_id
        self.grade = grade

    #自定义子类的方法
    def study(self):
        print(f'我叫{self.name},我在努力学习,争取做到{self.grade}年级第一名')

#实例化一个Student类的实例化对象,需要传入Person的属性
stu1 = Student('张三',20,'男', 2025123, '初二')
print(stu1.__dict__)#{'name': '张三', 'age': 20, 'gender': '男'}
print(type(stu1))#<class '__main__.Student'>

#
def speak(data):
    print(f'我是stu1自身的speak方法，我要说{data}')
stu1.speak = speak

#查找speak方法的过程:1.实例自身(s1) => 2.Student类 => 3.Person类
stu1.speak('Hello World')#我是stu1自身的speak方法，我要说Hello World, 调用的是stu1自身的speak方法

#查看stu1新增属性
print(stu1.__dict__)

stu1.study()
