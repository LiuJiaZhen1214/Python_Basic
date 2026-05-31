#1.使用for()循环，打印一个30天的锻炼计划
# day = 1
# for day in range(1, 31):
#     print(f'*****第{day}天*****')
#     for n in range(4):
#         print(f'第{n+1}组锻炼完成')
#     print(f'第{day}天的训练已完成\n')
# print(f'恭喜你！{day}天的训练计划已完成！！！')

#2.使用while()循环输出为期30天的锻炼计划
day = 1
while day <= 30:
    print(f'*****第{day}天*****')
    group = 1
    while group <= 4:
        print(f'第{group}组锻炼完成！')
        group += 1
    print(f'第{day}天的训练完成\n')
    day += 1
print(f'恭喜你！{day-1}天的训练计划完成！！！')