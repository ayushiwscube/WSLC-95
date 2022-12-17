# for i in range(1,20):
#     if i == 16:
#         break
#     else:
#         print(i)

#


while True:
    print("Welcome to INOX")

    normal_seats = 300
    recliners = 450
    name = input("enter your name: ")
    amount = 0
    print("the price of recliner is 450 and the price of normal seats is 300")
    choice = int(input("press 1 for recliner or press 2 for normal seats: "))
    if choice == 1:
        seats = int(input("how many seats do you want? "))
        amount = (seats*recliners )

    elif choice == 2:
        seats = int(input("how many seats do you want? "))
        amount = (seats * normal_seats)

    print("amount to be paid", amount)

    popcorn = input("would you like to have a combo of popcorn of rs 150(yes/no): ")

    if popcorn == "yes":
        quantity = int(input("how many combos do you want? "))
        new_amount = amount + (150*quantity)
        print("the new amount to be paid is", new_amount)
    else:
        print()

    repeat = input("do you want to repeat again?(yes/no): ")
    if repeat == "no":
        break
