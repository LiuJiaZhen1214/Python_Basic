"""一、单分支语句"""
#1.if判断为假
age = 15
if age >= 18:
    print('你是成年人')
    print('成年人的世界，虽不容易，却也精彩!')
print('欢迎你来学习Python')

#2.if判断为真，执行语句
if age <= 18:
    print('你是儿童，祝你6.1儿童节快乐')

#3.非0数字和非空字符串在判断时，都是True
if 1 and -1 and 'abc':
    print('判断为真，输出内容')#判断为真，输出内容
if not (1 and 0):
    print('1 and 0 判断为假')#1 and 0 判断为假

#4.输入age,输入的是字符串类型，转换为int型
age = int(input('请输入您的年龄：'))
if age >= 18:
    print('你是成年人，祝你成功')

"""二、双分支语句"""
age = int(input('请输入你的年龄：'))
if age >= 18:
    print('你是成年人')
else:
    print('你是未成年人')
    print('努力学习，报效祖国')

"""三、多分支语句"""
age = int(input('请输入你的年龄：'))
if age <=10:
    print('你是儿童！')
elif age <=18:
    print('你是少年！')
elif age <= 30:
    print('你是青年！')
elif age <=50:
    print('你是中年！')
elif age <=60:
    print('你是中老年！')
else:
    print('你是老年')
