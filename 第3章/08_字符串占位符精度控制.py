"""占位符精度控制，浮点数四舍五入"""
name = 'LiuJiaZhen'
age = 22
gender = '男'
weight = 91.5
"""
%m.nf
1.m
m控制整体位宽(整数宽度+小数点+小数宽度)
位数不够空格来补，位数小于整体位宽，自动失效
正数是右对齐，负数是左对齐
2.n
n是精度控制，保留n位小数(n默认值是6)，不够0来补，戒断会四舍五入
"""
info4 = '我是%s，我是%s生，我的体重是%f，年龄是%d' % (name, gender, weight, age)
print(info4)  # 我是LiuJiaZhen，我是男生，我的体重是91.500000，年龄是22
info4 = '我是%12s，我是%-5s生，我的体重是%6.3f，年龄是%5.3d' % (name, gender, weight, age)
print(info4)  # 我是  LiuJiaZhen，我是男    生，我的体重是91.500，年龄是  022
info4 = '我是%s，我是%s生，我的体重是%.0f，年龄是%d' % (name, gender, weight, age)
# 四舍五入
print(info4)  # 我是LiuJiaZhen，我是男生，我的体重是92，年龄是22
