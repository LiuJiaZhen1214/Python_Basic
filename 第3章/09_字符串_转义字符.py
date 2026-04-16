"""转义字符输出"""
# 字符串中使用转义字符，打印',单引号
print('在python中，可以使用\'打印一个单引号')  # 在python中，可以使用'打印一个单引号

# 使用\",打印一个双引号
print("在python中，可以使用\"打印一个双引号")  # 在python中，可以使用"打印一个双引号

# 使用\n 进行换行
print('注册会员需要以下信息: \n姓名\n年龄\n手机号')
"""
注册会员需要以下信息: 
姓名
年龄
手机号
"""
# 使用\\输出\
print('D:\\nice')
print('D:\nice')  # 未转义，识别为换行符
"""
D:\nice
D:
ice
"""

# 使用\b删除前一个字符
print('helloo\b')#hello

#使用\r使光标回到本行开头，覆盖输出
print('67%\r68%')#68%

#使用\t表示水平制表符，让光标跳转到下一个制表位
print('1234123412341234')
print('ab\tcd')
print('abc\td')
print('abcd\ta')
print('我是\t中文')
"""
1234123412341234
ab	cd
abc	d
abcd	a
我是	中文
"""
#\t常见用法
print('姓名\t性别\t年龄')
print('张三\t男\t18')
print('李四\t男\t20')
print('王五\t女\t30')
