import time
from threading import Thread

basket = 0

class A(Thread):
    cook_name = ''
    basket_count = 50
    def run(self) -> None:
        global basket
        print(self.cook_name,'正在做蛋挞')
        if basket >= 500:
            time.sleep(3)
        else:
            basket = basket + self.basket_count

class B(Thread):
    customer_name = ''
    customer_money = 3000
    eggshell = 2
    eggshell_count = 30
    def run(self) -> None:
        global basket
        while True:
            print(self.customer_name,'正在买蛋挞')
            if basket == 0:
                time.sleep(2)
            else:
                self.customer_money = self.customer_money - self.eggshell* self.eggshell_count
            if self.customer_money == 0:
                break

a1 = A()
b1 = B()
a1.cook_name = '张三'
b1.customer_name = '老大'

a1.start()
b1.start()

a2 = A()
b2 = B()
a2.cook_name = '李四'
b2.customer_name = '老二'

a2.start()
b2.start()