"""
Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
举个例子，假设要根据同学的名字查找对应的成绩，如果用list实现，需要两个list：

names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
给定一个名字，要查找对应的成绩，就先要在names中找到对应的位置，再从scores取出对应的成绩，list越长，耗时越长。
如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。用Python写一个dict如下：

字典是无序（3.7 + 有序）、键值对存储、键唯一不可变的数据容器，用 {键:值} 定义，通过键 (key) 取值，值 (value) 可任意修改。
字典的元素是无序的，不能使用索引来获取元素，只能使用key来获取对应元素
"""
#1.定义
d = {'MJ':100, 'Bob':85, 'LM': 84}
print(d['MJ'])#100
print(d, type(d))#{'MJ': 100, 'Bob': 85, 'LM': 84} <class 'dict'>
"""
dict就是第二种实现方式，给定一个名字，比如'Michael'，dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，也就是95这个数字存放的内存地址，直接取出来，所以速度非常快。
而list是从前往后一个一个查找，直到找到对应元素，所以list越长，查找时间越长
"""

#2.把数据放入字典，key和value必须配对
d['Adam'] = 69
print(d['Adam'])#69
print(d)#{'MJ': 100, 'Bob': 85, 'LM': 84, 'Adam': 69}

#3.由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
d['Bob'] = 65
print(d)#{'MJ': 100, 'Bob': 65, 'LM': 84, 'Adam': 69}
d['Bob'] = 95
print(d)#{'MJ': 100, 'Bob': 95, 'LM': 84, 'Adam': 69}

#4.判断key是否存在，使用in方法
print('Thomas' in d)#False
#通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('ABC'))#None
print(d.get('ABC',-1))#-1
print(d.get('MJ'))#100

#5.要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
print(d.pop('LM'), d)#84 {'MJ': 100, 'Bob': 95, 'Adam': 69}
print(d)#{'MJ': 100, 'Bob': 95, 'Adam': 69}

#6.遍历字典(遍历所有键值对)
goods = {'苹果':5, '香蕉':3, '葡萄':4}
for k,v in goods.items():#items() 获取所有键值对；
    print(f'水果:{k}, 价格:{v}')
'''
水果:苹果, 价格:5
水果:香蕉, 价格:3
水果:葡萄, 价格:4
'''
#7.极简数据案例 - 统计字符出现次数
text = 'hello'
count = {}
for c in text:
    count[c] = count.get(c,0)+1
print(count)
'''get(c,0),若存在，返回c对应的value; 若不存在，返回自己设定的0这个值'''

"""
dict的key必须是不可变对象：字符串和整数
在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
>>> key = [1, 2, 3]
>>> d[key] = 'a list'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
"""



