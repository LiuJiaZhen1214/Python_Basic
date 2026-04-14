"""本节介绍python中整型和浮点型数据"""
import sys

#1.整型即不带小数点的数字，可以是正数、负数、0
age = 20
temp = -15
score = 0

#当数字很大时，我们可以使用下划线将数字进行分组，增加可读性
age = 3_000_000
deposit = 999_999_999
print(deposit)

#Python中整数的上限值，取决于执行代码的计算机的内存和处理能力
large_score = 9**999
print(large_score)#数字非常大,正常输出
larger_score = 9**9999
#Exceeds the limit (4300),超出了print()能输出的4300位的范围了，只是不能输出了
#print(larger_score)
sys.set_int_max_str_digits(0)#不再限制位数
print(larger_score)#正常输出

#2.浮点型，带小数点的数字
weight = 80.0
b = 123.456
c = -12.3
print(weight)
print(b)
print(c)

#浮点型的科学计数法
speed_of_sound = 3.8e+2
print(speed_of_sound)#380
print(type(speed_of_sound))
world_population = 7.8e9#7.8乘以10的9次方
print(world_population)
print(type(world_population))

one_ml = 1e-3#'-'不能省略
print(one_ml)#0.001