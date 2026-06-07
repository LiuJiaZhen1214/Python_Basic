"""
lambda 表达式又称匿名函数，是 Python 提供的轻量化函数语法：
无需 def 关键字、无需定义函数名，仅支持单行表达式，不能编写循环、分支等多行复杂逻辑；
标准语法：lambda 形参列表: 表达式，表达式的运算结果自动作为返回值；
常搭配内置函数 map()、filter()、sorted() 使用，适合临时、简单的逻辑处理。
普通函数是正式、功能完整的工具；lambda 是一次性临时小工具，不用起名，只做简单计算 / 判断，用完即可丢弃，代码更简洁。
# 基础语法
lambda 参数1, 参数2: 运算表达式
"""
#1.两数相乘
mul = lambda x, y: x * y
print(mul(1, 2))

#2.lambda + filter 筛选数据
nums = [1, 2, 3, 4, 5, 6]
#filter(判断函数, 可迭代对象)：保留判断结果为True的函数
#filter(...)：根据 lambda 规则过滤列表；
even_list = list(filter(lambda x: x % 2 == 0, nums))
print('列表中的偶数', even_list)
list_test = [1, 2, 0, '', False, 5, 'xx']
#filter()返回值是一个filter object,需要用list()将元素转换为列表
res = list(filter(None, list_test))#自动过滤掉None or False这些假值元素
print(res)#[1, 2, 5, 'xx']

#3.lambda + sorted 自定义排序
"""
sorted()是数据的排序器
sorted() 的作用是对任意可迭代对象进行排序，并返回一个新的、排好序的列表。它不会修改原来的数据
sorted(iterable, *, key=None, reverse=False)
iterable：需要排序的可迭代对象3。
key（可选）：一个函数，用来指定按什么规则来比较和排序。
reverse（可选）：排序规则。False（默认）表示升序，True 表示降序
"""
nums = [9,3,4,8,6,5,2,7,1]
print(sorted(nums))#默认升序，[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sorted(nums, reverse=True))#降序，[9, 8, 7, 6, 5, 4, 3, 2, 1]
#sorted()不会改变原列表的数据，只是会生成一个新的数据
print(nums)#[9, 3, 4, 8, 6, 5, 2, 7, 1]
#按单词长度排序
words = ["banana", "apple", "cherry"]
print(sorted(words, key=len))#['apple', 'banana', 'cherry']
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]#students是一个字典
#根据学生分数从高到低排序
#[{'name': 'Bob', 'score': 92}, {'name': 'Alice', 'score': 85}, {'name': 'Charlie', 'score': 78}]
print(sorted(students, key=lambda s:s["score"],reverse=True))

# 列表元素：(商品名, 价格)
goods = [("苹果", 5), ("香蕉", 3), ("橙子", 4)]
# 按第二个元素（价格）升序排序
print(sorted(goods, key=lambda x:x[1]))#[('香蕉', 3), ('橙子', 4), ('苹果', 5)]

#4.lambda + map 批量处理元素
# map(处理函数, 可迭代对象)：对每个元素执行相同逻辑
nums = [10,20,30]
double_list = list(map(lambda x:x*2,nums))
print(double_list)#[20, 40, 60]
Square_list = list(map(lambda x:x**2, nums))
print(Square_list)#[100, 400, 900]





