"""定义类名"""
#1.定义一个Person类(通常使用: 大驼峰写法)
class Person:
    #说明：当一个函数在定义在类中时，这个函数被称为该类的"方法"
    #初始化方法：给当前正在创建的实例对象添加属性
    # __init__方法收到的参数：当前正在创建的实例对象（self）、其它的自定义参数
    # 当我们以后编写代码去创建Person类实例的时候，Python会自动调用__init__方法
    def __init__(self, name, age, gender):
        #给实例添加属性(语法为:self.属性名 = 值)
        self.name = name
        self.age = age
        self.gender = gender

#2.创建Person类的实例对象
person1 = Person('张三', 18, '男')
person2 = Person('lisa', 20, '女')
#如果直接打印一个实例的话，是看不到一个实例身上的属性的
#print(person1)
#print(person2)
print(person1.name, person1.age, person1.gender)#张三 18 男
print(person2.name, person2.age, person2.gender)#lisa 20 女

#通过 实例.__dict__ 可以查看实例身上所有的属性
print(person1.__dict__)#{'name': '张三', 'age': 18, 'gender': '男'}
print(person2.__dict__)#{'name': 'lisa', 'age': 20, 'gender': '女'}

#实施创建完之后，依然可以通过 实例.属性名 = 值 的方式去给实例追加属性
person1.weight = 75
print(person1.__dict__)#{'name': '张三', 'age': 18, 'gender': '男', 'weight': 75}

#通过type()查看对象类型
print(type(person1))#<class '__main__.Person'>


