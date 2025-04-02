'''The protected variables must be accessed inside the same class or inside child class.'''

class Demo1:
    def __init__(self):
        self.name = 'AK'  #Protected variables

    def disp1(self):
        print(self.name) #  Accessomg inside the same class

d1 = Demo1()

class Demo2(Demo1):
    def disp(self):
        print(self.__name) #Accessing inside child class

d2 = Demo2()
print(d2.name)   #AK