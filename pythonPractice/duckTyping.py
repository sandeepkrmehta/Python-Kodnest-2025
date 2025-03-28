# class Calci:
#     def calculate(self,a,b):
#         print('calculating a and b')

class Add():
    def calculate(self,a,b):
        print(a + b)  # 30
class Mul():
    def calculate(self, a, b):
        print(a * b)  # 200
class Div():
    def calculate(self, a, b):
        print(a / b)  # 0.5

def permit(ref):
    ref.calculate(10, 20)

permit(Add())
permit(Mul())
permit(Div())