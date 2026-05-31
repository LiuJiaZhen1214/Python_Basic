"""
一共 3 个关卡 (每个关卡只有一道题)，答对进入下一关，3 关都通过则挑战成功！。
1 答错可重试，每道题都有 3 次回答机会，若 3 次均答错，则挑战失败，游戏自动结束。
2 如果用户输入为空，则提示重新作答，且不浪费回答机会。
3 如果用户输入字母 q，则直接退出游戏。
"""
print('欢迎来到: 答题闯关挑战赛 (输入q可随时退出) \n')

#题目与答案
ques1, ans1 = 'Python中用于输出的函数是？', 'print'
ques2, ans2 = 'Python中用于表示逻辑“并且”的关键字是?', 'and'
ques3, ans3 = 'Python属于编译型还是解释型？', '解释型'

#最多可尝试次数
max_tries = 3
#总关卡数
total_levels = 3
#是否处于可游戏状态
is_playing = True

#根据题目数量开始循环
for level in range(1,total_levels+1):
    print(f'******这是第{level}关******')
    #取出当前关卡所对应的题目和答案
    if level == 1:
        ques, ans = ques1, ans1
    elif level == 2:
        ques, ans = ques2, ans2
    else:
        ques, ans = ques3, ans3
    #若已经尝试的次数<=最大次数，则进入循环
    #记录当前关卡的尝试次数
    tries = 1#第1次
    while tries <= max_tries:
        #向用户提问，获取答案
        user_input = input(ques)
        if user_input == ans:
            print('✅️回答正确\n')
            break
        elif user_input == '':
            print('⚠️您的输入为空，请重新输入！\n')
            tries += 1
            is_playing = False
            continue
        elif user_input == 'q':
            print('👏您已退出游戏\n')
            is_playing = False#用户不再想玩游戏
            break
        else:
            leave = max_tries - tries
            if leave > 0:
                print(f'❌️回答错误，您还有{leave}次机会！\n')
                tries += 1
                continue
            else:
                print(f'😃挑战失败，正确本题答案是{ans},游戏结束')
                is_playing = False
                break
    if not is_playing:
        break
    if is_playing:
        print('恭喜您，您通关了！！！')