age = int(input('请输入你的年龄：'))
has_report = input('您是否提交了体检报告？(是/否)：')
level = int(input('请输入你的会员等级(1/2/3)：'))
print('******⬇️程序识别结果如下：⬇️******')
#简化链式比较
if 18 <= age <= 45:
    print('✅️您的年龄可以参加比赛')
    if has_report == '是':
        print('✅️你已经提交报告，可以正式参加比赛！！！')
        if level == 1:
            print(f'您的会员等级是{level}，您的礼物是：纪念T恤')
        elif level == 2:
            print(f'您的会员等级是{level}，您的礼物是：专业跑鞋')
        elif level == 3:
            print(f'您的会员等级是{level}，您的礼物是：运动耳机')
        else:
            print('你的会员等级有误')
    elif has_report == '否':
        print('您未提交报告，不能提交比赛')
    else:
        print('您输入的体检报告有误')
else:
    print('❌️你的年龄不能参加比赛')

