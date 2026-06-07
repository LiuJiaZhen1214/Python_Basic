class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


#定义一个Student类，继承自Person类
class Student(Person):
    #定义初始化方法
    def __init__(self, name, age, gender, stu_id, grade):
        #调用父类的方法进行初始化
        super().__init__(name, age, gender)
        #初始化子类独有的属性
        self.stu_id = stu_id
        self.grade = grade

p1 = Person('张三',18,'男')
s1 = Student('李华', 12, '男', 2022210, '初二')

#方法1：isinstance(instance, Class),作用：判断某个对象是否为指定类或其子类的实例
print(isinstance(s1,Student))#True
print(isinstance(s1, Person))#True
print(isinstance(p1, Person))#True
print(isinstance(p1, Student))#False

#方法2：issubclass(Class1, Class2),作用：判断某个类是否是另一个类的子类
print(issubclass(Student, Person))#True
print(issubclass(Person, Student))#False