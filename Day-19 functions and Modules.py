# def person(name,age,gender):
#     print(name)
#     print(age)
#     print(gender)
#
# person(age= 25,gender="female",name = "ayushi")

#args
# def person(*data):
#     print(data)
#     for i in data:
#         print(i)
#
# person("ayushi",25,"female","trainer")

#kwargs

# def person(name,**data):
#     print(name)
#     print(data)
#     for i,j in data.items():
#         print(i,"-",j)
#
# person(name="ayushi",age = 25, gender = "female")

# a = 12 #global
#
#
# def wscube():
#     global a
#     a = 6 #local
#     print(a)
#
#
# wscube()
# print(a)


# score = 2
#
# def inc_score():
#     global score
#     score += 2
#     print(score)
#
# inc_score()


# a = 49
# print(a**(1/2))
#
# import math
#
# print(math.sqrt(a))

#random


# import random

# dice = [1,2,3,4,5,6]
#
# toss = random.choice(dice)
# print(toss)


# print(random.randrange(1,100))
# fruits = ["kiwi","pineapple","apple","banana"]
# a = random.choice(fruits)
# print(a)

# import random
#
# choice = input("even or odd? ")
#
# if choice == "even":
#     a =random.randrange(0,100,2)
#     print(a)
# else:
#     a = random.randrange(1,100,2)
#     print(a)


import random

words = ["TELEPHONE","SATURN","STRAWBERRY","PYTHON","JAVASCRIPT",'SMARTPHONE']
word = random.choice(words)
#print(word)
total_chances = 7

dashes = "-"*len(word)


while total_chances>0:
    print(dashes)
    letter = input("guess a letter: ").upper()
    if letter in word: #STRAWBERRY 
        for i in range(len(word)): # --r-------  --R----R--  --R----RR-
            if word[i] == letter:
                dashes = dashes[:i]+letter+dashes[i+1:]

        if dashes == word:
            print("congratulations you won!")
            break
    else:
        total_chances-= 1
        print("you lost a chance")
        print("total chances are",total_chances)
else:
    print("game over")
    print("the correct word is", word)
