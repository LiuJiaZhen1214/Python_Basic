"""
python函数可以返回单个数据、多个数据，返回多个数据时，python会自动将结果封装成元组
若函数中未显式编写 return 语句，函数执行完毕后，会默认返回内置常量 None（空值）

# 返回单个值
return 表达式
# 返回多个值（自动封装为元组）
return 表达式1, 表达式2, 表达式3

"""
#1.返回两数之和
def add(a, b):#两个位置参数
    return a + b
res = add(1, 2)
print(f'两数之和{res}')

#2.返回多个值，求商和余数
def div_mod(a, b):
    shang = a // b#//是整除
    yvshu = a % b
    return shang, yvshu#返回到是数据元组
s,y = div_mod(10,6)#利用解包语法，把元组中的两个值分别赋值给变量
temp = div_mod(10,6)
print(temp,type(temp))#(1, 4) <class 'tuple'>
print(f'商是{s},余数是{y}')#商是1,余数是4

#3.返回布尔值，判断数字是否是正数
def is_positive(num):
    return num > 0
print(is_positive(10))#True
print(is_positive(-10))#False

#极简案例，成绩统计(总分+平均分)
def score_analysis(scores):
    total = sum(scores)
    avg = total / len(scores)
    return total, avg
#接收两个返回值
total, avg = score_analysis([1,2,3,4,5])
print(f'总分{total}, 平均分{avg}')#总分15, 平均分3.0
"""
def score_analysis(scores)：你必须主动打包好一个列表或元组传进去。
def score_calculate(*scores)：你可以直接散着传一堆数字进去，Python 会自动帮你打包。
score_analysis([90, 85, 95])  # ✅ 正确
score_analysis((90, 85, 95))  # ✅ 正确,传入参数必须是元组
score_analysis(90, 85, 95)  # ❌ 报错！TypeError: 传了3个参数，但只需要1个
score_calculate(90, 85, 95)   # ✅ 正确！scores 在内部变成了 (90, 85, 95)
"""
