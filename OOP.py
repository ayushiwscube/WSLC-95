# class smartphone:
#     def __init__(self): #initialize
#         print("these are the details of the phone")
#     def phone(self,camera, ram, storage):
#         print(camera, ram, storage)
#     def charger(self,c_type,normal ):
#         print(c_type, normal)
#
# oneplus = smartphone()
# #oneplus.phone("48MP","12GB","256GB")
# oneplus.charger("yes","no")

"""
create a class called company
method - employeename, age, gender, salary

create object and call all the details 
also create one constructor
"""

# class company:
#     def __init__(self):
#         print("these are the employee details")
#     def employee_details(self,name, age, gender, salary):
#         print(name,age,gender,salary)
#
# emp1 = company()
# emp1.employee_details("John",24,"Male",50000)
# emp2 = company()
# emp2.employee_details("Peter",34,"Male",40000)


class bank:
    def __init__(self):
        self.balance = 5000
        self.name = "John"
    def deposit(self):
        amount= int(input("enter amount: "))
        self.balance+=amount
        print(self.balance)
        print(self.name)
        self.amount = 5000

    def withdraw(self):
        amount = int(input("enter withdrawal amount: "))
        self.balance-=amount
        print(self.balance)
        self.amount+=3000

john = bank()
#john.deposit()
john.withdraw()
