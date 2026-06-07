"""
实现一个成绩统计程序，可以对多名学生的成绩，进行统计和分析。
"""
#学生输入成绩，直到输入"结束"，才停止输入
print('请输入成绩，直到输入"结束"，停止输入：')
scores = []

while True:
    data = input('请输入成绩：')
    if data == '结束':
        break
    else:
        scores.append(int(data))
#如果list中有数据，就开始统计
if scores:
    #统计平均分
    avg = sum(scores)/len(scores)
    #统计合格人数
    pass_num = 0
    #统计优秀人数
    excellent_num = 0
    #遍历列表，开始统计
    for item in scores:
        if item >= 60:
            pass_num += 1
        if item >= 90:
            excellent_num += 1
    #合格率
    pass_rate = pass_num/len(scores)*100
    #优秀率
    excellent_rate = excellent_num/len(scores)*100
    #打印信息
    print(f'总人数：{len(scores)}')
    print(f'通过人数：{pass_num}, 通过率：{pass_rate}%')
    print(f'优秀人数：{excellent_num}, 优秀率：{excellent_rate}%')
    print(f'最高分：{max(scores)}, 最低分：{min(scores)}')
    print(f'平均分：{avg}')
else:
    print('您没有输入任何成绩')


