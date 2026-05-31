"""
函数就是把要重复写的代码打包成一个专属的工具，之后要使用同样的代码，就可以直接
调用对应的函数。
def是制作工具，把代码封装起来。函数名()是使用工具，之后使用函数名直接调用该工具
"""
#1.无参数的函数：打招呼
def say_hello():
    print('hello')
    print('你好呀！祝你天天开心')
#直接调用函数
say_hello()

#2.计算数字的平方
def calculate_square(num):
    result = num ** 2
    print(f'{num}的平方是{result}')
#调用函数
num = int(input('输入数字：'))
calculate_square(num)

#3.打印个人信息
def print_profile():
    print('姓名：小明')
    print('学校：重庆邮电大学')
def print_info(name, school):
    print(f'姓名：{name}')
    print(f'学校：{school}')
print_profile()
print_info('LiuJiaZhen', 'CQUPT')

#4.统计列表中元素个数
def count_list(lst):
    print(f'列表长度为{len(lst)}')
count_list([1, 2, 3])
