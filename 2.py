import random
money = 100
num1 = random.randint(0, 100)
print(num1)
while money > 0:
    money -= 10
    num2 = int(input('���������Ĳ²⣺'))
    if num2 > num1:
        print('�´��ˣ��ٽ�����')
    elif num2 < num1:
        print('��С�ˣ��ٽ�����')
    else:
        print('��ϲ��')
        break