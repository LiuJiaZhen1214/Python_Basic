#0b开头表示二进制
num1 = 0b11001
#0o开头表示八进制
num2 = 0o1034
#0x开头表示十六进制
num3 = 0x1cf

#Python中所有的非十进制数，只是代码层面的编写方式，是给程序员看的
#Python在对上面的numx进行运算、打印操作时，会自动将他们转为十进制数
print(num1, num2, num3)#25 540 463
print(num1+1)#26
print(str(num2))#540
print(str(num3)+str(num2))#463540
print(num3 > 400)#True

#使用bin()将十进制转换为二进制的字符串
result1 = bin(25)
#使用oct()将十进制转换为八进制的字符串
result2 = oct(540)
#使用hex()将十进制转换为十六进制的字符串
result3 = hex(463)
print(result1, result2, result3)#0b11001 0o1034 0x1cf
#返回的结果都是“字符串”
print(type(result1), type(result2), type(result3))#<class 'str'> <class 'str'> <class 'str'>

#其他进制-->十进制数字，使用int(),得到的是数字
#将其他进制的字符串格式转换为十进制数字格式
val1 = int('0b11001',2)
val2 = int('0o1034',8)
#val3 = int('0x1cf',8),错误
val3 = int('0x1cf',16)
print(val1, val2, val3)#25 540 463


