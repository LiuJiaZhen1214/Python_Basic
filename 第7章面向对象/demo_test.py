"""用于一些例子测试和一些代码的补充"""
info_str = '王五-2003-女'
res = info_str.split('-')
print(res)#['王五', '2003', '女'],得到的是列表
name, year, gender = info_str.split('-')
print(name, year, gender)#王五 2003 女
