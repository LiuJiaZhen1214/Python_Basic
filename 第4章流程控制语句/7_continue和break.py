#1.continue，跳过本次循环的剩余语句，随后进入下一次循环
for day in range(1,5):
    print(f'*****第{day}天*****')
    print('吃饭')
    print('睡觉')
#第2天，不打印任何内容
for day in range(1,5):
    if day == 2:
        continue
    print(f'*****第{day}天*****')
    print('吃饭')
    print('睡觉')

#2.break,立即终止循环，不再执行后续的循环
