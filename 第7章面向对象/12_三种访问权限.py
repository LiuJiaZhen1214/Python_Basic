"""三种访问权限"""
#定义Person类
class Person:
    #定义初始化方法
    def __init__(self, name, age, idcard):
        self.name = name       #公有属性(Public):当前类中，子类中，类外部，都可以访问
        self._age = age         #受保护的属性(Protected):当前类中，子类中，都可以访问
        self.__idcard = idcard   #私有属性(Private):仅能在当前类中访问
    def speak(self):
        print(f'我叫{self.name},年龄: {self._age}, 身份证号: {self.__idcard}')

class Student(Person):
    def hello(self):
        print(f'我是学生，{self.name}-{self._age}-{self.__idcard}')
#实例化对象
p1 = Person('张三', 20, '147852369987456321')
#验证：在当前类中，可以访问公有、受保护、私有属性
p1.speak()#我叫张三,年龄: 20, 身份证号: 147852369987456321

#验证：子类中，是否可以访问三种权限的属性
s1 = Student('张三', 20, '147852369987456321')
#子类，无法访问私有属性
#s1.hello()#Error: 'Student' object has no attribute '_Student__idcard'

#验证类的外部：是否可访问三大属性
print(p1.name)#正常访问
#在类的外部，如果强制访问【受保护的属性】也能访问到，但十分不推荐
#print(p1._age)#20
#类外部，是否能访问【私有属性】，不能访问到
#print(p1.__idcard)#报错：'Person' object has no attribute '__idcard'

print(p1.__dict__)