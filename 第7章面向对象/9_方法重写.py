"""方法重写"""
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def speak(self, msg):
        print(f'{self.name}说:\"我的年龄是{self.age},我的性别是{self.gender},我的姓名是{self.name},我想说{msg}\"')

#定义一个Student类，继承自Person类
class Student(Person):
    #定义初始化方法
    def __init__(self, name, age, gender, stu_id, grade):
        #调用父类的方法进行初始化
        super().__init__(name, age, gender)
        #初始化子类独有的属性
        self.stu_id = stu_id
        self.grade = grade

    #方法重写：当子类中定义了一个与父类中相同的方法，那么子类中的方法就会"覆盖"父类的方法
    def speak(self, msg):
        #如果任然想要调用父类的speak(),可以使用super()
        super().speak(msg)
        print(f'我是学生，我的学号是{self.stu_id},我正在读{self.grade},我想说:{msg}')


#验证一下：方法重写
#初始化实例对象
s1 = Student('梨花',15,'女',2025201,'初三')
s1.speak('你好，世界')#我是学生，我的学号是2025201,我正在读初三,我想说:你好，世界
"""
梨花说:"我的年龄是15,我的性别是女,我的姓名是梨花,我想说你好，世界"
我是学生，我的学号是2025201,我正在读初三,我想说:你好，世界
"""