#1.使用while打印10次你好呀
n = 1
while n <= 10:
    print(f'第{n}次你好呀！')
    n += 1
print(n)#11

print('*****下面是while()循环的测试案例*****')
#2.while循环案例
print('你现在身处密室，需要正确回答问题之后，才能逃出密室！')
riddle = '你的心上人是谁？'
answer = 'Thunder'
guess = ''

while guess != answer:
    print(riddle)
    guess = input('请输入答案：')
    if guess == answer:
        print('回答正确，逃脱成功！')
    else:
        print('回答错误，逃脱失败！')

