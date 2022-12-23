# days = ["thur","fri","sat","sun"]
# 
# print(days)
# 
# temp = days[0]
# print(temp)
# days[0]=days[-1]
# print(days)
# days[-1] = temp
# print(days)


#
# days[0],days[-1]=days[-1],days[0]
# print(days)





# numbers = [3,7,4,6,9,4,7,0,-4]
#
# print(numbers.count(4))
#
# count = 0
# for i in numbers:
#     if i == 4:
#         count+=1
# print(count)






# numbers = [3,7,4,6,9,4,7,0,-4]
#
# print(len(numbers))
#
# count = 0
# for i in numbers:
#     count+=1
#
# print(count)






# numbers = [3,7,4,6,9,4,7,0,-4]
#
# print(min(numbers))
# print(max(numbers))
#
# #how to get min and max values without using min and max functions
# numbers.sort()
# print(numbers)
# print(numbers[0])
# print(numbers[-1])








# company = {"John":"John@123", "Ayushi":"Ayushi@12345","Jalaj":"Jalaj@123456"}

# print(company["John"])
# print(company['Ayushi'])
#
# for i in company.keys():
#     print(i)




# print("Welcome to our portal")
# print("Enter your Credentials here")
#
#
# Username = input("Enter Username: ")
# if Username in company.keys():
#     Password = input("enter password: ")
#     if Password == company[Username]:
#         print("Login Successful")
#     else:
#         print("Incorrect password")
# else:
#     print("Incorrect Username")




# school = {"Name":"John","Marks":80, "Age":12, "Gender":"Male"}

# print(school)
# print(school["Marks"])

#iteration
# for i,j in school.items():
#     print(i,"=", j)
#
# for i in school.keys():
#     print(i)
#
# for i in school.values():
#     print(i)











# fruits = ["apple","kiwi","cherry",'banana',"leechi","blueberry","pineapple"]
#
# print(fruits[6])
# for i,j in enumerate(fruits):
#     print(i,j)
