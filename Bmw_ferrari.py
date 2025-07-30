class BMW():
    def speed(self):
        print("BMW is a fast car")
    def looks(self):
        print("BMW is a good looking car")
    def price(self):
        print("BMW is a expensive car")
class Ferrari():
    def speed(self):
        print("Ferrari is a super fast car")
    def looks(self):
        print("Ferrari is a very very good looking car")
    def price(self):
        print("Ferrari is a super expensive car")
car1 = BMW()
car2 = Ferrari()
for i in (car1,car2):
    i.looks()
    i.price()
    i.speed()
print("YIPEEEEEEE")