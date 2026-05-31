"""算术运算符演示"""
print(9+7)
print(9-7)
print(9*7)
print('%f'%(9/7))#除法，1.285714
print(9//7)#取整除法，1
print(9%7)#取余，2
print(9**7)#指数运算，4782969

#加法复合运算符
price = 20
price += 1
print(price)#21
price -= 2
print(price)#19
price *= 2
print(price)#38
price /= 3
print(price)#12.666...
price = int(price)
print(price)#12
price **= 2
print(price)#144

#比较运算符，和C语言中一样
#ord()将字符转换为Unicode编码，chr()将编码转换为字符
print(ord('a'))#97
print(ord('A'))#65
print(ord('我'))#25105
print(chr(97))#a
print(chr(65))#A
print(chr(25105))#我

#布尔类型，boolean: True or False
#boolean是int类型的子类型，底层是用1表示True，0表示False
a = 2>1
b = 5<3
print(type(a),a)
print(type(b),b)
print(type(a+b),a,a+b)
print(type(a-b),a,a-b)
print(type(a*b),a,a*b)
print(7>True)#True
print(8+False)#8
print(type(a+b),a+b)#<class 'int'> 1
'''
bool类型数据运算之后结果是int类型的数字
<class 'bool'> True
<class 'bool'> False
<class 'int'> True 1
<class 'int'> True 1
<class 'int'> True 0
'''
#Python中除0以外的任何数，转为布尔值后都是True
print(bool(300))#True
print(bool(1.56))#True
print(bool(2.78)+3)#4
print(bool(-5))#True
#Python中除了空字符串以外的任何字符串，转为布尔值都是True

#逻辑运算符 与(and) 或(or) 非(not)
print(True and True)#True
print(True or True)#True
print(True or False)#True
print(not True)#False
print(not False)#True
print(7>5 and False)#False

#and具备逻辑短路的能力,直接判断到False,不执行后面的内容
print(False and 5/0)#False
print(False and True)#False




