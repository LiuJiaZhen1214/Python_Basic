"""
本节演示列表常用方法的代码
a.b(), 是一个对象，b()称为a的方法
b(), 此时b()称为一个函数
"""
#1.list.append(元素)，末尾追加一个元素
nums = [10,20,30,40]
nums.append(50)
print(nums)
#2.list.insert(index, 元素)
nums.insert(2,60)
print(nums)#[10, 20, 60, 30, 40, 50]
#3.list.extend(可迭代对象), 将可迭代对象的内容依次取出，追加到列表尾部
nums.extend('Python')
print(nums)
lst1 = [1,2,3]
lst1.extend('你好')
lst1.extend([70,80])
print(lst1)#[1, 2, 3, '你', '好', 70, 80]
lst2 = [10,20,30]
lst2.extend(range(1,4))
print(lst2)#[10, 20, 30, 1, 2, 3]

#4.list.pop(index),删除指定位置的元素，并将元素返回
lst4 = [10,20,30,40]
res = lst4.pop()#默认弹出最后一个元素
print(res)#40
res1 = lst4.pop(1)
print(res1)#20, 删除指定下标的元素，并返回该元素

#5.list.remove(值), 删除列表中第一次出现的指定值
lst5 = [10,20,30,10,40,20]
lst5.remove(10)
print(lst5)#[20, 30, 10, 40, 20]
lst5.remove(20)
print(lst5)#[30, 10, 40, 20]

#6.list.clear(), 清空列表
lst5.clear()
print(lst5)#[]

#7.del list[index], 删除指定位置的元素
print(lst2)#[10, 20, 30, 1, 2, 3]
del lst2[3]
print(lst2)#[10, 20, 30, 2, 3]

#8.查找指定元素在列表中第一次出现的值
print(lst2.index(20))#1
lst2.append(30)
print(lst2.index(30))#2
#print(lst2.index(300))#报错, 300 is not in this list

#9.count(),统计某个元素在列表中出现的次数
print(lst2.count(30))#2

#10.list.reverse(), 翻转列表
print(lst2)#[10, 20, 30, 2, 3, 30]
print(lst2.reverse())#None
print(lst2)#[30, 3, 2, 30, 20, 10]

#11.list.sort(reverse=布尔值), 对列表排序
#list默认升序排序
lst2.sort()
print(lst2)#[2, 3, 10, 20, 30, 30]
lst2.sort(reverse=True)
print(lst2)#[30, 30, 20, 10, 3, 2]
#若列表中的元素：既有数字，又有字符串，那就会报错
"""
nums = [23, 11, 32, 30, 17, '尚硅谷']
nums.sort()
print(nums) # [23, 11, 32, 30, 17, '尚硅谷']
TypeError: '<' not supported between instances of 'str' and 'int'
"""
#若列表中的元素：都是字符串，则按照字符串的 Unicode 编码大小进行排序
msg_list = ['北京', '北硅谷', '北好']
msg_list.sort()
print(msg_list)#['北京', '北好', '北硅谷']
print(ord('京'), ord('好'), ord('硅'))

"""
列表的常见内置函数
这些内置函数，不仅适用于列表，而是适用于所有的数据容器
"""
#1.sorted(数据容器, reverse=布尔值), 对容器进行排序(默认从小到大，不会改变原容器)
#返回值是经过排序后的新容器
nums = [23,11,32,20,17]
res = sorted(nums)
print(nums)#[23, 11, 32, 20, 17],sorted不改变原列表
print(res)#[11, 17, 20, 23, 32]
nums.sort()#调用列表的sort()方法会改变原列表
print(nums)#[11, 17, 20, 23, 32]
'''若列表中的元素既有数字，又有字符串，使用sorted(nums)就会报错
'''

#若list中的元素都是字符串，则按照字符串的Unicode编码进行排序
msg_list1 = ['北','京','欢','迎','你']
print(sorted(msg_list1))#['京', '你', '北', '欢', '迎']
print(ord('京'), ord('你'), ord('北'), ord('欢'), ord('迎'))
#20140 20320 21271 27426 36814

#len(), 返回数据容器的个数
nums = [1,2,3,[9,8,7]]
print(len(nums))#4

#max, 取出最大值
#print(max(nums)), 报错：不能取不同类型
print(max(msg_list1))#京
print(max([9,6,2,4,5,8]))#9
print(min([9,6,2,4,5,8]))#2
msg_list2 = ['北极', '北京', '南京', '重庆']
print(max(msg_list2))#重庆
print(ord('重'))#37325
print(min(msg_list2))#北京
print(ord('北'))#21271

#sum(), 对容器中所有元素求和
print(sum([1,3,5,7,9]))

#2.循环遍历出list的元素
#（1）while循环遍历列表，使用index定义结束条件
score_list = [62, 50, 60, 48, 80, 20, 95]
index = 0
while index < len(score_list):
    print(score_list[index])
    index += 1
#（2）for循环遍历列表
for item in score_list:
    print(item)

#使用for循环遍历列表（通过enumerate函数，同时获取下标（索引值）和元素）
#enumerate 的 start 参数，可以让计数从指定值开始（改变的是循环时的“编号”，不是真正的索引值）
for index, item in enumerate(score_list, start=5):
    print(index, item)
#上面该表的只是输出的序号，没有改变元素的索引值
#下面是获取索引值
for index, item in enumerate(score_list):
    print(index, item)
    """
    0 62
    1 50
    2 60
    3 48
    4 80
    5 20
    6 95
    """


