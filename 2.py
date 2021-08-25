import random
money = 100
num1 = random.randint(0, 100)
print(num1)
while money > 0:
    money -= 10
    num2 = int(input('请输入您的猜测：'))
    if num2 > num1:
        print('猜大了，再接再厉')
    elif num2 < num1:
        print('猜小了，再接再厉')
    else:
        print('恭喜您')
        break