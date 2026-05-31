print('请输入你的年龄：')
age = input()#不管输入什么,input获取的都是字符串类型
print(type(age))
print(f"你今年年龄是{age}")
"""
请输入你的年龄：
18
<class 'str'>
你今年年龄是18
"""
#下面的写法更简洁
#直接使用input()接收输入信息
age = input('请输入你的年龄：')
name = input('你的姓名是：')
age = int(age)#转换数据类型
print(f'{name},你今年的年龄是{age}岁')
print(f'{name},你明年的年龄是{age+1}岁')
"""
请输入你的年龄：22
你的姓名是：LiuJiaZhen
LiuJiaZhen,你今年的年龄是22岁
LiuJiaZhen,你明年的年龄是23岁
"""

