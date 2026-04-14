"""
本文件简单介绍变量的一些使用规则
变量，顾名思义是值可以变化的量。变量名是盒子，值是内容。
和其他语言不同，python中，定义一个新变量时，必须马上赋值，否则会报错
标识符命名规则：数字，字母，下划线，不能以数字开头。推荐蛇形写法。
"""
name = 'LiuJiaZhen'
age = 20
print(age)
#weight，NameError: name 'weight' is not defined
#python中，定义一个新变量时，必须马上赋值，否则会报错
weight = 90
weight = 85#警告：已重新声明上方无用法weight
print(name, '现在的体重是', weight)#LiuJiaZhen 现在的体重是 85

#标识符命名规范
UserName = 'LiuJiaZhen'#大驼峰写法
userName = 'LiuJiaZhen'#小驼峰写法
user_name = 'LiuJiaZhen'#蛇形写法，推荐
print(UserName)
print(user_name)