"""
介绍常量的简单用法
约定俗成，一般用全大写字母的标识符表示常量
常量一旦被赋值，就不希望改变，但是修改不会出问题
"""
age = 20#这里的age，20是变量
AGE = 20#这里的AGE是常量
#可以使用ctrl+shift+u,直接将变量变为常量
NAME = 'LiuJiaZhen'
print(age)
print(NAME)
NAME = 'LiuJia'
print(NAME)#LiuJia,修改常量，并不会出错