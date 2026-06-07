"""
全局变量：定义在函数外部的变量，作用域为整个代码文件，所有函数都可以读取；
局部变量：定义在函数内部的变量，作用域仅限当前函数，函数执行结束后，局部变量会被内存销毁；
语法规则：若需要在函数内部修改全局变量，必须先用 global 关键字声明该变量。

# 全局变量（函数外定义）
变量名 = 值

def 函数名():
    global 全局变量名  # 声明要修改全局变量
    局部变量名 = 值    # 局部变量（函数内定义）
"""
#1.全局变量：在函数外部定义，在整个文件内生效
clas_name = '计科1班'
def show_class():
    print(clas_name)
show_class()#计科1班

#2.局部变量：外部无法访问
def test():
    num = 100
    print('函数内部打印：', num)
test()#函数内部打印： 100
#print(num)#NameError: name 'num' is not defined

#3.在函数内部使用global修改全局变量
count = 0#定义全局变量count用来计数
def add_count():
    global count#告诉 Python：当前操作的是全局变量，而非新建局部变量；
    count += 1
add_count()
print(f'修改后的全局变量{count}')

#4.全局变量+局部变量混合使用
UNIT = 10#全局变量
def calc(x):
    temp = UNIT * x#temp:局部变量，临时计算结果
    return temp
print(calc(10))#100



