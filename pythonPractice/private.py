'''Privates variable must be accessed inside the same class.'''

class Demo1:
    def __init__(self):
        self.__name = 'AK'  # Private variable
    
    def disp1(self):
        print(self.__name)  #Accessing inside the same class

d1 = Demo1()
#print(d1.__name)  #error

'''
Public: When we want to access variables anywhere in the code.
Protected: When we want to access variables inside the same class and inside child class.
Private: When we want to access variables inside the same class.

Access Declearations:

public a = 10
protected: _a = 10
private: __a = 10

'''

