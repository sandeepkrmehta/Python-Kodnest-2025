class Demo1:
    def magic(self):
        print('Inside magic method of demo1')
class Demo2:
    def magic(self):
        print('Inside magic method of demo2')
class Demo3(Demo1, Demo2):
    pass
d3 = Demo3()
d3.magic()    #Inside magic method of demo1

print(Demo3.__mro__)





class Demo1:
    def magic(self):
        print('Inside magic method of demo1')
class Demo2:
    def magic(self):
        print('Inside magic method of demo2')
class Demo3(Demo2, Demo1):
    pass
d3 = Demo3()
d3.magic()    #Inside magic method of demo2