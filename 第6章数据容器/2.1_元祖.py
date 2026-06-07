"""
元组是有序、不可变、允许重复元素的序列数据容器，用 () 定义，一旦创建无法修改（增删改均不支持），仅支持查询操作。
元组就像密封快递盒：有固定顺序、装完东西就封死，不能修改里面的物品，只能查看。
元组和列表的主要区别就是，元组不能改变，只能查看
# 定义
元组名 = (元素1, 元素2, 元素3)
# 单元素元组必须加逗号：(1,)

因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
"""
#1.基础定义与取值（个人固定信息）
info = ('张三', 22, '北京')#当tuple定义时，tuple的元素就定下来了，不能再改变
print(info)
print(info[1])
#定义一个空的tuple
t = ()
print(t, len(t), type(t))#() 0 <class 'tuple'>
#但是如果只定义含有一个元素的tuple，得写成t = (a, )
t_1 = (1, )
print(t_1)#(1,),以免你误解成数学计算意义上的括号

#2.最后来看一个“可变的”tuple：
t_2 = ('a', 'b', ['A', 'B'])
t_2[2][0] = 'X'
t_2[2][1] = 'Y'
print(t_2)#('a', 'b', ['X', 'Y'])
t_2[2].append(3)
print(t_2)#('a', 'b', ['X', 'Y', 3])

#练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Bob:
print(L[2][2])

#元组遍历
color = ('red', 'green', 'black')
for c in color:
    print(c)

#元组解包
# 定义坐标元组
point = (10, 20)
# 解包：直接赋值给多个变量
x, y = point
print(x, y)





