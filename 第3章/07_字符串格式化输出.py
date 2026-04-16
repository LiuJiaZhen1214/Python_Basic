"""字符串的格式化输出"""
name = 'LiuJiaZhen'
age = 22
gender = '男'
weight = 91.5

# 写法一:直接用+连接字符串，但是'+'只能连接字符串类型，不能拼接其他数据类型
#can only concatenate str (not "int") to str
#info1 = '我是' + name + '，我是'+gender + '生' + age
info1 = '我是' + name + '，我是'+gender + '生'
print(info1)

#写法二:使用占位符，格式化输出
info2 = '我是%s，我是%s生，我的体重是%f，年龄是%d'%(name,gender,weight,age)
print(info2)#我是LiuJiaZhen，我是男生，我的体重是91.500000，年龄是22
#占位符可以全部使用%s,按字符串格式输出
info3 = '我是%s，我是%s生，我的体重是%s，年龄是%s'%(name,gender,weight,age)
print(info3)#我是LiuJiaZhen，我是男生，我的体重是91.5，年龄是22
info4 = '我是%s，我是%s生，我的体重是%d，年龄是%f'%(name,gender,weight,age)
#体重用%d占位，输出91
print(info4)#我是LiuJiaZhen，我是男生，我的体重是91，年龄是22.000000

#写法三:使用f-string,在字符串开头加上f,f即format,将嵌入内容直接转成字符串
#官方推荐写法
info5 = f'我是{name}，我今年{age}岁，我的性别是{gender}，我体重是{weight}kg'
print(info5)#我是LiuJiaZhen，我今年22岁，我的性别是男，我体重是91.5kg