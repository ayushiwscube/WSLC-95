# def hw():
#     #print("hello world")
#     print("my name is ayushi")
#
# hw()
#
# def add():
#     x = 45
#     y = 67
#     print(x+y)
#
# add()
#
# def add1(x,y,z): #Parameters
#     print(x+y+z)
#
# add1(12,67,67) #Arguments
# add1(45,67,89)

# def odd_even(num):
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("odd")
#
# odd_even(40)

# def hw():
#     return "hello world"
#     return "hello"
#
# print(hw())



# def add(x,y):
#     print(x)
#     print(y)
#     return (x+y)
#
# add(2,6)

# x = lambda x,y,z : x + y + z
#
# print(x(12,7,8))


# def hw():
#     print("hello world")
#     hw()
#
# hw()

# fact = 1
# for i in range(1,6):
#     fact = fact*i
#
# print(fact)

# def fact(num):
#     if num == 1:
#         return 1
#     else:
#         return num*fact(num-1)
#
# print(fact(6))

def fibo(num):
    if num<=1:
        return num
    else:
        return fibo(num-1)+fibo(num-2)

for i in range(8):
    print(fibo(i))
