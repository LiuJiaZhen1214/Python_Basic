#1.打印10次hello world
#range(10)-->range(0,10),生成一个区间序列[0,10),左闭右开
#for i in range(10): i: 0-9,这10个数
"""
range(...)称为可迭代对象，字符串也属于可迭代对象
可迭代对象中的元素有多少个，循环就执行多少次
只要不在循环内部修改可迭代对象，for循环是不会出现死循环的


"""
from pyexpat.errors import messages

#1.
n = 0
for n in range(1, 11):#n: 1-10
    print(f'这是第{n}次Hello World!')
print(n)#10

#2.使用for()来遍历一个字符串
for ch in 'hello world':
    print(ch)#逐个输出字符串的每个字母

#3.for()循环案例
text = input('请输入要加密的文字：')
secret = ''
for t in text:
    secret += chr(ord(t) + 1)#字符串拼接
print(f'加密后的文字是：{secret}')

message = ''
for s in secret:
    message += chr(ord(s) - 1)
print(f'解密后的文字是：{message}')





