"""
参数就是传递给函数的原材料，函数根据你不同的原材料生成或处理不同的内容
如果炒菜这个动作是一个函数，不同的菜就是不同的参数，得到的结果就是不同的菜品
1.位置参数：根据参数不同的位置传对应的参数，按顺序传参数
2.关键字参数：对应名字传参数，传参时写上对应的参数名，不必按照顺序
3.默认参数：定义函数时就提前定义好一些默认值/初始值，你不必传参也可以
4.可变参数：接收任意数量的材料
"""
from tkinter.font import names


#1.位置参数-点餐，按顺序传菜名和价格
def order_food(food, price):
    print(f'点了{food},价格是{price}元')
order_food('牛肉',100)

#2.默认参数-制作饮料
def make_drink(drink, size='中杯'):
    print(f'制作：{drink},{size}')
make_drink('牛奶')
make_drink('可乐','大杯')

#3.关键字参数-填写信息(顺序随意)
def print_profile(name,age):
    print(f'name={name},age={age}')
print_profile(age=23,name='LiuJZ')

#4.可变参数 *args - 接收任意数量的位置参数
#python自动将传入的数据打包成元组，适用于函数处理不确定个数的数据
# 任意数字求和
def sum_nums(*args):
    total = sum(args)
    print(f'total={total}')
sum_nums(1,2,3,4,5)
sum_nums(5,6,7,8,9)

#5.可变参数 **kwargs, 接收任意数量的关键字参数
#python自动将"键=值"打包成一个字典(dict),键值对结构,适用于接收不确定的、带名称的配置信息
def show_info(**kwargs): #接收任意数量的关键字参数(键值对)
    print(kwargs)#{'苹果': 5, '香蕉': 3}
# 调用：传入两个关键字参数 → kwargs={"苹果":5, "香蕉":3}
show_info(苹果=5,香蕉=3)

# 打印args的类型，证明是元组
def test_args(*args):
    print("args的数据：", args)#args的数据： (1, 2, 3)
    print("args的类型：", type(args))  # 输出 <class 'tuple'>

test_args(1,2,3)

# 打印kwargs的类型，证明是字典
def test_kwargs(**kwargs):
    print("kwargs的数据：", kwargs)#kwargs的数据： {'姓名': '张三', '年龄': 22}
    print("kwargs的类型：", type(kwargs)) # 输出 <class 'dict'>

test_kwargs(姓名="张三", 年龄=22)

