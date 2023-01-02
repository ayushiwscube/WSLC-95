#Tuples

# name = "apple","banana","kiwi"
# print(type(name))
# print(name)
# print(name[1])
#
# a = ()
# print(type(a))


# name = "apple","banana","kiwi"
# print(name)
# name = list(name)
# print(name)
# name.append("pineapple")
# print(name)
# name = tuple(name)
# print(name)
#
#
#
# a = 12345
# print(type(a))
# a = str(a)
# print(type(a))
#
# b = "apple"
# b = int(b)
# print(b)


# a =["apple"]
# print(type(a))
#
# b = ("apple",)
# print(type(b))

# name = "apple","banana","kiwi"
# values = 23,56,45
#
#
# for i, j in zip(name,values):
#     print(i,j)
#
# for i,j in enumerate(name):
#     print(i,j)




a = {}
while True:
    print("""
    press 1 to add a country
    press 2 to display a capital
    press 3 to del a country
    press 4 to display everything""")


    choice = int(input('enter choice between 1-4: '))
    if choice == 1:
        country = input("enter country: ").upper()
        capital = input('enter capital: ').upper()
        a[country] = capital
    elif choice ==2:
        country = input("enter country: ").upper()
        print(a[country])
    elif choice == 3:
        country = input("enter country: ").upper()
        del a[country]
    elif choice == 4:
        print(a)














# emp = {"Name":"John","Age":23,"Gender":"Male"}
#
# emp["Age"]=24
# emp["Designation"]="Manager"
# print(emp)
#
#
# print(emp.get("Name"))
# print(emp["Name"])
#
# del emp["Name"]
# print(emp)
#
# a = ["banana","apple","kiwi"]
# b = [2,4,5]
#
# fruits = dict.fromkeys(a,b)
# print(fruits)
#
# for i in emp.keys():
#     print(i)
#
# for i in emp.values():
#     print(i)
#
# for i in emp.items():
#     print(i)

#Task

"Library Management System"
# Books = {"Maths":0,"Science":10,'english':2}
# borrrowed_books = {}
#
# name = ayushi
# book = maths


"""press 1 to display all the books
press 2 to borrow a book
press 3 to return a book
press 4 to display all the borrowed books
"""



# company = {"Emp001":{"Name":"John","Age":23,"Gender":"Male"},
#            "Emp002":{"Name":"Peter","Age":27,"Gender":"Male"},
#            "Emp003":{"Name":"Lisa","Age":25, "Gender":"Female"}}
#
# school = {"Names":["peter","david","john"],
#           "Marks":[98,66,78]}
#
# print(school["Names"][0])
