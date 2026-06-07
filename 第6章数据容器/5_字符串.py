"""
字符串（str）：用来存放一组有序的字符数据，但其中的内容不可修改（只能查，不能增删改）
"""
#1.和列表一样，字符串支持下标取元素
msg1 = 'welcome to beijing'
print(msg1[2], msg1[5], msg1[8])#l m t
print(msg1[-1])#g

#字符串中的字符不可修改，不可嵌套
#2.使用字符串.index(字符)，获取『指定字符』在字符串中『第一次』出现的下标
print(msg1.index('e'), msg1.index('o'))#1 4

#3.使用字符串.split(字符)，将字符串按照『指定字符』进行分隔，返回值：列表
#将字符串按照指定字符进行分割，并将分割后的内容放入一个列表
msg2 = '北京#欢迎#你，'
res2 = msg2.split('#')#返回值是一个列表
print(res2)#['北京', '欢迎', '你，']

# replace 方法：将字符串中的某个字符片段，替换成目标字符串（不修改原字符串，返回新字符串）
msg = 'welcome to atguigu'
result = msg.replace('atguigu', '尚硅谷')
print(msg)    # welcome to atguigu
print(result) # welcome to 尚硅谷

# count 方法：统计指定字符，在字符串中出现的次数
msg = 'welcome to atguigu'
result = msg.count('g')
print(result)  # 2

# strip 方法：从某个字符串中删除：指定字符串中的任意字符
# 规则：从字符串两端开始删除，直到遇到第一个不在strip()指定字符串中的字符就停下
msg = '666尚6硅6谷666'
result = msg.strip('6')
print(msg)    # 666尚6硅6谷666
print(result) # 尚6硅6谷
msg = '1234尚12硅34谷4321'
result = msg.strip('1324')
print(msg)     # 1234尚12硅34谷4321
print(result)  # 尚12硅34谷
msg = '34215尚12硅34谷4132'
result = msg.strip('5432')
print(msg)   # 34215尚12硅34谷4132
print(result)# 15尚12硅34谷41
msg = '  尚硅谷  '
result = msg.strip()
print(msg)   #   尚硅谷
print(result)# 尚硅谷

#字符串也可以使用：max、min、len、sorted、sum函数，但实际开发中len函数最常用
msg = 'welcome to beijing'
print(len(msg))#18

#遍历字符串，既可以使用while, 也可以使用for循环
#(1) while循环
index = 0#设置index为循环的结束条件
while index < len(msg):
    print(msg[index])
    index += 1

#(2) for循环遍历
for item in msg:
    print(item)
