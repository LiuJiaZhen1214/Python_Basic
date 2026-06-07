"""
字典：用来存放一组『键值对』数据，可通过『键(key)』对『值(value)』进行：增、删、改、查操作。
字典就像一个带标签的收纳盒，你贴上标签（键），然后放进东西（值） 。
"""
# 字典中的key不能重复，若出现重复，则后写的会覆盖之前写的
d1 = {'张三': 72, '李四': 60, '王五': 85, '张三': 99}
print(d1)#{'张三': 99, '李四': 60, '王五': 85}
# 定义空字典
d1 = {}
d2 = dict()
print(type(d1), d1)
print(type(d2), d2)

# 字典中的key必须是不可变类型(元组、字符串、数字)，但value可以是任意类型
# 通俗理解：只有不可变的东西，才能作为key
d1 = {250: 72, '李四': 60, '王五': 85}
d2 = {('抽烟', '喝酒'): 72, '李四': 60, '王五': 85}
print(d1)
print(d2)
# 错误示例：将列表作为key，是不行的
# d2 = {['抽烟', '喝酒']: 72, '李四': 60, '王五': 85}

#字典是可以嵌套的，以student_dict为例
student_dict = {
    2026001:{
        '姓名' : '张三',
        '年龄' : 18,
        '成绩' : 98
    },
2026002:{
        '姓名' : '李四',
        '年龄' : 19,
        '成绩' : 95
    },
2026003:{
        '姓名' : '溜溜',
        '年龄' : 20,
        '成绩' : 99
    }
}
print(student_dict)

#字典的增删改查
#新增语法：字典[key] = 值
# 新增一个元素
d1 = {'张三': 72, '李四': 60, '王五': 85}
d1['赵六'] = 100
print(d1)#{'张三': 72, '李四': 60, '王五': 85, '赵六': 100}

#删除元素
# 删除
d1 = {'张三': 72, '李四': 60, '王五': 85, '赵六':92}

# 删除指定key所对应的那组键值对
del d1['张三']
print(d1)

# 删除指定key所对应的那组键值对，并返回这个key所对应的值
result = d1.pop('王五')
print(d1)#{'李四': 60, '赵六': 92}
print(result)#85

# pop方法可以设置默认值
# 默认值可以保证：当要删除的key不存在的情况下，程序不会报错，并且返回这个默认值
result = d1.pop('奥特曼', '删除失败！')
print(d1)
print(result)

# 清空字典
d1.clear()
print(d1)

d1 = {'张三': 72, '李四': 60, '王五': 85}

# 修改的写法，与新增的写法一样，若字典中有对应的key，就是修改；若没有，就是新增
d1['张三'] = 97
print(d1)#{'张三': 97, '李四': 60, '王五': 85}
#批量修改
d1.update({'李四':80, '王五':87})
print(d1)#{'张三': 97, '李四': 80, '王五': 87}

# 查询
d1 = {'张三': 72, '李四': 60, '王五': 85}
# 直接取值，若键（key）不存在，会报错
result = d1['张三']
# 安全取值，若键（key）不存在，会返回默认值（若没有设置默认值，则会返回None）
result = d1.get('奥特曼', '抱歉，key不存在！')
print(result)#抱歉，key不存在！

# keys方法：用于获取字典中所有的键
d1 = {'张三': 72, '李四': 60, '王五': 85}

# keys方法的返回值不是list，而是一种叫做dict_keys的类型
result = d1.keys()
print(result)
print(type(result))

# dict_keys和列表类似，可以被遍历，但要注意的是：它不能通过下标访问元素
for item in result:
    print(item)
#print(result[0]),'dict_keys' object is not subscriptable,该object不支持下标访问

# 借助内置的list函数，可以将dict_keys转换成list
l1 = list(result)
print(l1)
print(type(l1))

# values方法：获取字典中所有的值
d1 = {'张三': 72, '李四': 60, '王五': 85}
# values方法的返回值类型是：dict_values，它的特点和dict_keys一样
result = d1.values()
print(result)
print(type(result))

# items方法：获取字典中所有的键值对（每组键值对以元组的形式呈现）
d1 = {'张三': 72, '李四': 60, '王五': 85}

# items方法返回的类型是：dict_items，它的特点也和dict_keys一样
result = d1.items()
print(result)
print(type(result))

#字典的循环
# 字典不能使用while循环遍历，但可以使用for循环遍历
d1 = {'张三': 72, '李四': 60, '王五': 85}

for key in d1:
    print(f'{key}的成绩是{d1[key]}')

for key in d1.keys():
    print(f'{key}的成绩是{d1[key]}')

for item in d1:
    print(item)
"""
张三
李四
王五
"""



