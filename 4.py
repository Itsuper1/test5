import time
from threading import Thread

basket = 0

class A(Thread):
    cook_name = ''
    basket_count = 1
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
    eggshell_count = 1
    def run(self) -> None:
        global basket
        print(self.customer_name,'正在买蛋挞')
        if basket == 0:
            time.sleep(2)
        else:
            self.customer_money = self.customer_money - self.eggshell* self.eggshell_count
a = A()
b = B()
a.cook_name = '张三'
b.customer_name = '老大'

a.start()
b.start()
