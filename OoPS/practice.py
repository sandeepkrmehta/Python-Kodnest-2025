class Employee:
    name = 'Sandeep'
    age = 23

    def code(self):
        print('Employee is coding')

e1 = Employee()
e2 = Employee()
print(e1.name)
print(e2.age)
e1.code()
e2.code()

'''
1. Method which are present inside the class are called as Instance(object) Methods.
2. For Instance Methods self parameter is must.


3. The variables which are present inside an object such variables are called as Instance Variables.
4. For Instance Variables seperate copy will be crated
'''