"""数据类型转换"""
#使用str()将指定数据转换为字符串
result1 = str(18)
result2 = str(75.6)
result3 = str(1.8e3)
result4 = str(12_000)

print(type(result1),result1)
print(type(result2),result2)
print(type(result3),result3)
print(type(result4),result4)
"""
<class 'str'> 18
<class 'str'> 75.6
<class 'str'> 1800.0
<class 'str'> 12000
"""
#使用int()将指定数据转换为整型
result5  = int('18')
result6 = int(75.6)
result7 = int(1.8e3)
result8 = int(' 79 ')
print(result5)#18
print(result6)#75
print(result7)#1800
print(result8)#79
#下面是错误示例
'''
print(int('7 9'))
print(int('你好'))
print(int('79个'))
print(int('15.6'))
'''

#同理，使用float()可以将数据类型转换为浮点型
