"""使用嵌套循环，打印九九乘法表"""
#1.前置知识
print('你好')
print('尚硅谷')
#分行打印
"""
你好
尚硅谷
相当于：
print('你好', end='\n')
print('尚硅谷', end='\n'))
"""
print('你好', end='!')
print('尚硅谷', end='@\n')
"""
你好!尚硅谷@
"""
print('你好', end='')
print('尚硅谷', end='\n')
"""你好尚硅谷"""

#1.使用for()循环打印9*9乘法表
for row in range(1,10):#row: 1-9
    for col in range(1,row+1):#col: 1-row
        print(f'{col}*{row}={row*col}', end=' ')
    print()

