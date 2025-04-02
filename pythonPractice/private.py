class Demo1:
    def __init__(self):
        self.__name = 'AK'  # Private variable
    
    def disp1(self):
        print(self.__name)  #Accessing inside the same class

d1 = Demo1()
#print(d1.__name)  #error