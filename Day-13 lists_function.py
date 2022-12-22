grocery = []

print("""Press 1 to add something to the list
Press 2 to remove something from the list
Press 3 to display the list""")

while True:
	choice = int(input("enter your choice between 1-3: "))

	if choice == 1:
		item = input("enter item name: ").lower()
		grocery.append(item)

	elif choice == 2:
		item = input("enter item name: ").lower()
		grocery.remove(item)

	elif choice == 3:
		print(grocery)

	else:
		print("invalid input. try again")






















# fruits = ["apple","banana","pineapple","kiwi","blueberry"]
# numbers = [1,3,5,6,3,5,6,3,5,7,4,6]
# vegies = ["potato",'carrot',"broccoli"]





# print(min(numbers))
# print(max(numbers))



# fruits.reverse()
# print(fruits)

# fruits.clear()
# print(fruits)

#print(fruits.index("kiwi"))




# fruits.pop(2)
# print(fruits)

# fruits.remove("kiwi")
# print(fruits)

# fruits.insert(3,"kiwi")
# print(fruits)







# numbers.sort()
# print(numbers)
# fruits.sort()
# print(fruits)




# fruits.append("strawberry")
# print(fruits)
# fruits.append("chikoo")
# print(fruits)

# fruits.insert(1,"papaya")
# print(fruits)
# fruits.insert(3,"cherry")
# print(fruits)







# vegies.extend(fruits)
# print(vegies)

# print(len(fruits))
# print(numbers.count(7))
# c = fruits.copy()
# print(c)
# fruit2 = [i for i in fruits]
# print(fruit2)











# fruits = ["apple","banana","pineapple","kiwi","blueberry"]
# print(fruits[-4:-1])
