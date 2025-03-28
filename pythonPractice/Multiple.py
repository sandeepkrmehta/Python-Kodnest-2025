class Demo1:
    def  disp1(self):
        print("Inside dis1 method")
class Demo2:
    def  disp2(self):
        print("Inside dis2 method")
class Demo3(Demo1, Demo2):
    def  disp3(self):
        print("Inside dis3 method")


d = Demo3()
d.disp3()
d.disp2()
d.disp1()