"""
1. 函数嵌套
在一个函数的内部定义另一个函数，外层函数称为外函数，内部函数称为内函数；内函数的作用域仅限外函数内部，外部代码无法直接调用内函数。
2. 闭包（Closure）
是函数嵌套的特殊形式，必须同时满足 3 个条件：
① 存在函数嵌套；② 内函数引用了外函数的局部变量；③ 外函数将内函数作为返回值返回；
特性：闭包会延长外函数局部变量的生命周期，外函数执行结束后，其局部变量依然能被内函数访问。
通俗原理
函数嵌套：大盒子里面装小盒子，小盒子只能在大盒子里使用；
闭包：小盒子记住了大盒子里的数据，哪怕大盒子被拿走了，小盒子依然能使用这份数据。
"""
#1.函数嵌套：外函数内部定义一个内函数并调用这个内函数
def outer_hello():
    def inner_hello():
        print('你好，这是嵌套函数')
    inner_hello()
    #内函数只能在外函数内部被调用，外部无法直接执行 inner_hello()；
outer_hello()

#2.嵌套 - 商品折扣的计算
def get_price(price):
    def discount():
        return price*0.8
    return discount()
print(get_price(100))#80.0

#3.标准闭包 - 满足3个条件
def set_factor(n):
    #外函数局部变量是n
    #1.外函数内部定义内函数
    def calc(x):
        #2.内函数引用外函数局部变量n
        return x*n
    #3.将内函数作为对象返回
    return calc
#生成专属计算工具: n=2，可以更改外部函数的局部变量，来生成新的闭包函数
double = set_factor(2)#double现在是calc函数
#调用闭包函数, 延长了外部函数set_factor()的局部变量的使用周期
print(double(5))#10

#4.闭包实现数据缩放
def scale(k):#k是缩放系数
    #外函数：设置缩放系数
    def func(data):
        #内函数：对列表所有函数进行缩放
        return [x*k for x in data]
    #返回内部函数
    return func
#定义专属的缩放函数
scale_k1 = scale(0.36)
scale_k2 = scale(3.5)
#调用闭包函数，处理数据
data = [5,4,3,8,6]
print(scale_k1(data))
print(scale_k2(data))#[17.5, 14.0, 10.5, 28.0, 21.0]




