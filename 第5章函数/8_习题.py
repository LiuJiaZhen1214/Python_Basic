"""一些习题题目"""
#1.*args的使用
def sum_lst(*args):
    return sum(args)
print(sum_lst(1,3,5,7,9))#25

#2.**kargs的使用,必须得传入键值对数据，每个键不能一样
def print_info(**krags):
    print(krags)
#{'书名': 'C语言程序设计', '书': 'C++', '书1': 'English book'}
print_info(书名='C语言程序设计',书='C++',书1='English book')

#3.返回列表
def ret_lst():
    return [1,2,3,4]
print(ret_lst())

#4.接收列表，返回最大/最小值
def Max_Min(nums):
    return max(nums),min(nums)
max_num, min_num = Max_Min([5,6,9,3,5,1])
print(f'最大值是{max_num},最小值是{min_num}')

#5.判断是否是偶数，返回布尔值
def is_OuShu(num):
    return not num%2
print(is_OuShu(5))
print(is_OuShu(8))

#6.全局变量及其修改
school='重邮'
num=10
def print_global():
    global num
    num = 20
    print(school,num)
print_global()
print(num)#全局变量被修改

#7.计算圆的面积
PI = 3.14
def circle_area(r):
    return PI*r*r
print(circle_area(5))

#8.用 lambda + filter 筛选列表 [11,22,33,44] 中大于 20 的元素
def filter_20(lst):
    return list(filter(lambda x:x>20, lst))
print(filter_20([11,22,33,44]))#[22, 33, 44]

#9.用 lambda + sorted 对列表 [(2,5), (1,3), (3,1)] 按第一个元素排序。
def lst_sort(lst):
    return sorted(lst,key=lambda s:s[0])
print(lst_sort([(2,5), (1,3), (3,1)]))#[(1, 3), (2, 5), (3, 1)]

#10.用 lambda + map 把列表 [1,2,3] 中每个元素加 10。
def map_add_10(lst):
    return list(map(lambda x:x+10, lst))
print(map_add_10([1,2,3]))

#11.用 lambda 定义函数，判断数字是否大于 10。
a = lambda x:x>10#用lambda定义简单函数，不用def
print(a(12))#True

#12.定义嵌套函数，外层函数调用内层函数，内层打印 嵌套函数。
def outer_func():
    def inner_func():
        print('内层嵌套函数')
    #调用内内层的嵌套函数
    inner_func()
outer_func()

#13.外层函数接收数字 10，内层函数返回该数字加 5 的结果
def num_add_10(num):
    def add_10(num):
        num += 5
        return num
    #调用内层函数
    return add_10(num)
print(num_add_10(10))

#14.编写闭包：外层设置倍数 = 3，内层函数实现 “数字 × 倍数” 计算。
#闭包：函数内部定义嵌套函数；内部函数使用外部函数的局部变量；外部函数将内函数作为返回值返回
def mul_3(b=3):#外层定义倍数
    #内层函数
    def cal_3(num):#内层定义数据
        return num*b
    #将内层函数作为返回值返回
    return cal_3
#根据不同倍数生成不同的函数
print(mul_3()(10))#30
print(mul_3(4)(15))#60

#15.编写闭包：外层设置阈值 = 10，内层判断传入数字是否大于阈值。
def outer_fun1(a=10):
    #内层判断是否大于阈值
    def inner_func1(num):
        return num>a
    return inner_func1
is_num_bigger_10 = outer_fun1()
is_num_bigger_20 = outer_fun1(20)
print(is_num_bigger_10(15))
print(is_num_bigger_20(15))

#16.编写装饰器，为函数添加 函数开始 和 函数结束 的打印提示
#定义装饰器
def add_log(func):#修饰原函数func
    def wrapper():
        print('函数开始')
        func()#执行原函数的逻辑
        print('函数结束')
    return wrapper
#修饰目标函数
@add_log
def func_ing():
    print('函数运行中')
func_ing()

#17.装饰器的核心作用就是修饰原目标函数，在原目标函数的基础上增添一些功能

#18.编写装饰器修饰求和函数，自动打印原始参数和最终计算结果。
def add_info(func):
    def wrapper(lst):
        print('原始参数：',lst)
        res = func(lst)
        print('最后结果：',res)
    return wrapper
@add_info
def add_lst(lst):
    return sum(lst)
add_lst([1,2,6,9,5])