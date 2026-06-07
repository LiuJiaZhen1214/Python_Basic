"""
列表：python中最常见的数据容器，可以容纳多种数据类型
特点：有序、可变、允许有重复元素，支持增删查改
列表就像多功能购物袋：有固定顺序、可以随时往里加 / 减 / 换东西、能装重复物品、什么类型的东西都能放。
列表名 = [元素1, 元素2, 元素3]
"""
#1.基础定义与索引取值（购物清单）
shopping = ['apple','milk','cola','bread']
#从0开始取值，取第一个元素
print(shopping[0])
print(shopping[2])

#2.修改列表元素（可变特性）
scores = [45,80,100]
scores[1] = 56
print(scores)#[45, 56, 100]

#3.添加元素（append 尾部添加）,只能在末尾添加单个元素
scores.append(80)
print(scores)#[45, 56, 100, 80]
shopping.append(120)
print(shopping)#['apple', 'milk', 'cola', 'bread', 120]

#4.极简数据案例 - 列表切片（截取部分数据）
nums = [1,3,56,8,9,7]
#切片：[起始索引:结束索引]，左闭右开
res = nums[1:4]
res1 = nums[3]
res2 = nums[2:5]
print(res)#[3, 56, 8]
print(res1)#8, 不是切片，只是一个元素
print(res2)#[56, 8, 9]

#5.len()获取列表长度
print(len(nums))#6
#索引分为正索引和负索引，正~从0开始，负~从-1开始。
#如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
print(shopping[-1])#获取最后一个元素，120

#用索引-1获得倒数第一个元素，那么也可以获得倒数第2/3个元素
print(shopping[-2])#bread
print(shopping[-3])#cola

#6.使用索引，把元素插入到指定位置
classmates = ['Mike', 'Jack', 'Lisa']
classmates.insert(1,'Liu')
print(classmates)#['Mike', 'Liu', 'Jack', 'Lisa']

#7.用pop()，删除list末尾元素
classmates.pop()
print(classmates)#['Mike', 'Liu', 'Jack']
#pop(i),删除指定位置元素
classmates.insert(2,'MJ')
print(classmates)#['Mike', 'Liu', 'MJ', 'Jack']
classmates.pop(3)
print(classmates)#['Mike', 'Liu', 'MJ']

#8.list元素也可以是另一个list
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))#4
#获取s[2]这个list中的元素
print(s[2])#['asp', 'php']
print(s[2][1])#php



