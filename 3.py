'''
    1.׼���㹻�Ľ�Ǯ
    2.׼���յĹ��ﳵ
    3.��Ʒ���㹻����Ʒ
        ��������
    4.��ʼ����
    5.����
    6.��ӡ����С��
    ����ѡ�
        1.�жϣ�if
        2.ѭ����while,for
        3.��������
            �б�
                ����append()
                ɾ����del ����[�Ǳ�]
                �޸ģ�����[�Ǳ�] = ��ֵ
                ��ѯ������[�Ǳ�]
        4.��������:input
        5.��ӡprint
    ���
        �Ƿ������Ʒ��
            ���ڣ�
                Ǯ�Ƿ��㹻��
                    ����
                        ��ӵ��ҵĹ��ﳵ
                        ����ȥ���ӦǮ
                    ������
                        ��ܰ��ʾ������Բ���Ǯ�������������ط���ȥ��
            �����ڣ�
                ��ܰ��ʾ������Ʒ�����ڣ���ϹŪ��

    ����1��
        �Ż�����С���Ĵ�ӡ�������ϲ�ͬ�ࡣ
    ����2��
        10�Ż�е�����Ż�ȯ��9��
        20���ϸ����Ż�ȯ��1��
        15���������Ż�ȯ��2��
        2��4��3��1  0��1 ��е����9���Żݼ�
                   2��3��4��5 �ϸ���1���Żݼ�
                   6��7��8����2���Żݼ�
                   9 лл����
    �������ȡһ�ţ����ս����ʱ��ʹ������Ż�ȯ��
'''
# 0.��ȡ�Żݼۻ
print('��ӭ����!��ϲ����Ϊ��������˶������Գ�ȡһ���Ż�ȯ��')
import random
discounts = random.randint(0, 9)
if 0<=discounts<=1:
    print("��ϲ���鵽һ��9�ۻ�е��������ȯ��")
elif 2<=discounts<=5 :
    print("��ϲ���鵽һ��1���ϸ������ȯ��")
elif 8<discounts<=9 :
    print("���ź������ʹ���ȯֻ��һ���׵ľ��롣")
else:
    print("��ϲ���鵽һ��2��������������ȯ��")

# 1.׼����Ʒ
shop = [
    ["��е����",9000],  # shop[chose][1]
    ["Think pad",4500],
    ["Mac book pro",12000],
    ["ϴ�·�",20],
    ["����",2],
    ["�ϸ���",15],
    ["��������",3.5]
]
# 2.׼���㹻��Ǯ
money = input("�������ʼ��")
money = int(money) # "5" --> 5



# 3.׼���յĹ��ﳵ
mycart = []




# 4.��ʼ���

while True: # ��ѭ��
    # չʾ��Ʒ
    for key ,value in enumerate(shop):
        print(key,value)

    # ����
    chose = input("����������Ҫ����Ʒ��ţ�")
    if chose.isdigit():# "5" --> 5
        chose = int(chose)
        # ��Ʒ�Ƿ����
        if chose  > len(shop): # len()
            print("�Բ�����������Ʒ�����ڣ���ϹŪ��")
        else:
            # ��Ǯ�Ƿ��㹻
            if money < shop[chose][1]:
                print("����Բ���Ǯ�������������ط���ȥ��")
            else:
                mycart.append(shop[chose])
                #�д���ȯ�������ȯ������ȯ�������ϲ������ã�discounts=999
                #��е������9�������
                if 0<=discounts<=1 and shop[chose][0]=='��е����' :
                    money=money - shop[chose][1]*0.9
                    discounts=999
                # �ϸ����1�������
                elif 2<=discounts<=5 and shop[chose][0]=='�ϸ���' :
                    money = money - shop[chose][1] * 0.1
                    discounts=999
                # ����������2�������
                elif 6<=discounts<=8  and shop[chose][0]=='��������' :
                    money = money - shop[chose][1] * 0.2
                    discounts=999
                else:
                    money =  money - shop[chose][1]
                print("��ϲ���ɹ���ӹ��ﳵ!,������ʣ����",money)

    elif chose == 'q' or chose == 'Q':
        print("��ӭ�´ι��٣��ݰ������ϣ�")
        break
    else:
        print("�Բ�������Ƿ������������룡��ϹŪ��")

# ��ӡ����С��
print("���������Ĺ���С�������úã�")
print("----------------- �̳�------------------")
num =0
l=9999999
i=[0]*l    #�����±��б����б�ֵ����ʼ��Ϊ0
while num < len(mycart) :
    j=0
    #�Աȹ��ﳵ���̳���Ʒ�����ﳵ�и���Ʒ����Ʒ��Ӧ���±�+1
    while j<len(shop):
        if mycart[num][0]==shop[j][0]:
            i[j]+=1
        j+=1
    num +=1
# ��ӡ�����嵥����Ӧ�±��б��ӡ��i[]>0����ӡ��Ӧ����Ʒ��Ϣxi[]�������
c = 0
while c<len(shop) :
    if i[c] > 0 :
        print(c,shop[c],'x',i[c])
    c+=1
# for key ,value in enumerate(mycart):
# #     print(key,value)
print("����Ǯ����ʣ����",money)
print("-----------------------------------------")

