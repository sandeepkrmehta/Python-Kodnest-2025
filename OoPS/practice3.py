class Employee:
    company_name = "Code"
        
    def work(self):
        print("Employee is working.")
    def play(self):
        print("Employee is Playing.")

e1 = Employee()
e1.name = 'Sandeep'
e1.id = 101
e1.work()

e2 = Employee()
e2.name = 'Priya'
e2.id = 102
e2.work()
e2.play()