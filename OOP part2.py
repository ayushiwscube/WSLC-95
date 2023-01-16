class Oneplus:
    def camera(self):
        print("48MP")
    def ram(self):
        print("8GB")

class IPhone(Oneplus):
    def camera(self):
        print("50MP")
    def ram(self):
        print("12GB")

a = Oneplus()
b = IPhone()
b.ram()



# class companyA:
#     def emp1(self):
#         print("name is John")
#     def emp2(self):
#         print("name is peter")
#
# class companyB:
#     def emp3(self):
#         print("name is Lisa")
#     def emp4(self):
#         print("name is rebecca")
#
# class companyC(companyA,companyB):
#     def emp5(self):
#         print("name is duke")
#
# A = companyA()
# B = companyB()
# C = companyC()






# class companyA:
#     def emp1(self):
#         print("name is John")
#     def emp2(self):
#         print("name is peter")
#
# class companyB(companyA):
#     def emp3(self):
#         print("name is Lisa")
#     def emp4(self):
#         print("name is rebecca")
#
# class companyC(companyB):
#     def emp5(self):
#         print("name is duke")
#
# class companyD(companyC):
#     def emp6(self):
#         print("name is lary")
#
#
# A = companyA()
# B = companyB()
# C = companyC()
# D = companyD()
# D.emp1()










# class companyA:
#     def __init__(abc):
#         abc.salary = 50000
#     def emp1(abc,name, age):
#         print(name,age)
#         print(abc.salary)
#     def emp2(abc,name, age):
#         print(name,age)
#
# a = companyA()
# a.emp1("peter",34)
#
# def emp1(self,name,age,salary):
#     print(self,name,age,salary)
#
# emp1(23,"peter",34,50000)
