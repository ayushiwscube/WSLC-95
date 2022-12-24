# avengers = ["hulk","vision","wanda"]
# ele = "hulk"
#
# for i in avengers:
#     if ele in avengers:
#         print("it is present")
#
# numbers = [3,5,7,3,5,3,5]
# print(numbers)
#
# numbers.clear()
# print(numbers)
# numbers = [3,5,7,3,5,3,5]
#
# while len(numbers) != 0:
#     numbers.pop()
#
# print(numbers)


# numbers = [3,5,7,3,5,3,5]
#
# print(numbers.count(3))
# count = 0
# for i in numbers:
#     if i == 3:
#         count+=1
# print(count)


# numbers = [3,6,7,6,5,3,5]
# sum = 0
# count = 0
# for i in numbers:
#     sum += i
#     count+=1
#
# print(sum)
# print(count)
# print("avg is", sum/count)
# numbers = [3,5,7,3,5,3,5]
#
# multiply = 1
# for i in numbers:
#     multiply *= i
#
# print(multiply)



numbers = [3,5,7,2,3,8,5,3,4,6,5]

for i in numbers:
    if i % 2 != 0:
        print(i)
