# print("good, food is a homemade food.")

# here is a comment => you can use comman / to enable comments

"""
here is a block of comments to read

"""
#declare a variable

# my_variable = 5
# print (my_variable)

#dataTypes
#None
# my_bank_account = None
# print(type(my_bank_account))
# : indecates block of code => adds an indentation
# if (my_bank_account == True):
#     print("this is true")
# else:
#     print("this is not true...")


#Bollean - True pr False
# is_operating = True
# is_broken = False
#
# print(is_operating)
# print(is_broken)
#
# print(type(is_operating))
# print(type(is_broken))
#

#Numbers
# int=123
# print(type(int))

# float=21.123
# print(type(float))
# pi = 3.14
# print(type(pi))
# nigative = -1
# print(type(nigative))
# my_complex = 3+4j
# print(type(my_complex))
#split
# x = greeting.split (" ")
# print(x)

#index
# x = greeting.index("o")
# print(x)
# greeting = "Welcome SEI 02"
# Uppercase
# x = greeting.upper()
# print(x)

# Lowercase
# x = greeting.lower()
# print(x)

#replace method
# x = greeting.replace("SEI 02", "Champion")
# print(x)

#check the length: length always start count from 1 unlike index will start from 0
# x = len(greeting)
# print(x)


# in => you can find anything using the in operator
# x = "eggs" in "green eggs and bread"
# print(x)

# x = "Welcom" in greeting
# print(x)
# String interpolation
#f = format
# state = "Manama"
# year = 1973
# n = 4
# my_message = f"{state} was the {n}th to join the GCC in {year}."
# print(my_message)

#Arithmatic Operators

#add
# add = 2+2
# print (add)
#sub
# sub = 2-2
# print(sub)
#mul
# mul=2*2
# print(mul)
#div
# div = 7/2
# print(div)

# div = 7//2
# print(div)

# exponencial
# exp = 2**3
# print(exp)

# exp = 2**999
# print(exp)

#comparison operatiors

# == // for equality
# != // for inquality
# >= // greater or equal
# <= // less or equal


# Control Flow
# a = 33
# b = 200

# if b > a:
#     print("b is greater than a")
# elif a == b:
#     print("a and b are equal")
# else:
#     print("a is greater than b")


# vip = True
# food_place = "busy"
# if (food_place == "full" and not vip):
#     print("sorry we have no room tonight")
# elif(food_place == "busy" and not vip ):
#     print("please wiat 10  mins for table")
# else:
#     print("Welcome! Come sit down right away.")


# Ternaru Expression: a whole line of command

# age = 34
# age_test = print("you are a mid age") if age  >= 40 else print ("You are not old")

# Ranges in Python
# Syntax: [start:end:step]

# x = "my code" [3]
# print(x)
# x = "my code" [-1]
# print(x)
# x = "my code" [0:7]
# print(x)

#Python loops
# for num in range (0, 11,2):
#     print(num)

# for num in range (10, 0,-1):
#     print(num)

# % 
# for i in range (0,11):
#     if i % 2 == 0 :
#         print("{} is even". format(i))
#     if i % 2 == 1 :
#         print("{} is odd".format(i))

        # Iterating over an array / list
# foods = ["Carrots", "Graps", "Blue Berries"]
# for food in foods:
#     print ("I like",food)

# foods = ["Carrots", "Graps", "Blue Berries"]
# for food in foods:
#     print ("I like",food, foods.index(food))

# foods = ["Carrots", "Graps", "Blue Berries"]
# for i, food in enumerate(foods):
    # print("{}. {}" .format(i, food))


    # Nested Loops

    # outer = ["red", "spicy", "chile"]
    # inner = ["apple", "banana", "cherry"]
    # for x in outer:
    #     for y in inner:
    #         print(x,y)

#while loop
# i= 1
# while i < 6:
#     print(i)
#     i +=1

#LAB Session
        #fin index number of i
# str = "This is a string"
# char = "i"
# # str = ["This is a string"]
# for i in range (len (string)):
#     if string [i] == char:
#         print("index = ", i)

# Python Function/ Methods
# def greeting ():
#     print("Sha7wal, ya denya")

# greeting()

# def my_function()

#Stubbing
# def my_function():
    # pass

    # Function with 1 parameter
# def greeting(name):
#     print("Hello", name)
# greeting('Maitham')
# greeting('Salman')
# greeting('Alaraibi')


#function with multipa parameters
#Name argument xyzplace=abcplace
# def about_me(fave_food, fave_animal, fave_place):
#     print ('I love to eat', fave_food, 'while petting my', fave_animal, 'at', fave_place)
#Named argument
# about_me(fave_food="Machboos", fave_animal="cat", fave_place="home")

# Return from function
# def add(num1, num2, num3,):
#     return num1 + num2 + num3
# total = add (2,1,3)
# print (total)

#Global vs Local Variables
# def greeting():
#     print('Hello', name)
# #Global variable
# name = "Maitham"
# greeting()

#Callback function

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul (a,b):
#     return a*b
# def div(a,b):
#     return a/b
# def compute(a, b, op):
#     return op(a, b)
# print (compute(2, 0, add))
# print (compute(2, 0, sub))
# print (compute(2, 0, mul))
# print (compute(2, 1, div))


# *args = collect all arguments
# def f(*args):
#     print(type(args))
#     for arg in args:
#         print(arg)
# f(1, 2, 151, "Maitham", "Salman")


# def dev_skills(dev_name, *args):
#     dev = {'name': dev_name, 'skills': []}
#     for skill in args:
#         dev ['skills'].append(skill)
#     return dev
# print (dev_skills("Maitham Alaraibi",'HTML', 'CSS', 'JS', 'Python'))


# **kwargs - keywoord argument
# def dev_skills(dev_name, **kwargs):
#     dev = {'name': dev_name, 'skills': {}}
#     for skill, rating in kwargs.items():
#         dev ['skills'][skill] =rating
#     return dev
# print (dev_skills("Maitham Alaraibi", HTML=5, CSS=5, JS=5, ruby=5, Python=5))


# Combine arg, args, kwargs
# def arg_demo(pos1, pos2, *args, **kwargs):
#     print(f"Positional Params: {pos1}, {pos2}")
#     print('*args:')
#     for arg in args:
#         print('', arg)
#     print('**kwargs')
    
#     for keyword, value in kwargs.items():
#         print(f'{keyword}:{value}')

# arg_demo('A', 'B', 1, 2, 3, 4, 5, color='purple', shape='circle', food='pizza')

# Python Containers



# Python Lists
# colors = ["red", "yellow", "blue", 2,3]
# print(colors)
# print(type(colors)) #type is used to see what is the class
# print(colors[0])
# print(colors[1])
# print(colors[2])


# Basic List operation
# len: length of string

# my_class = ["Maitham", "Maryam", "Amal","Salman", "Ali"]
# num_students=len(my_class)
# print("There are", num_students, "Students in the class")

# append() - push to the end of the array

# my_class.append("Salma")
# print(my_class)

# # Insert: where to push the data
# my_class.insert(0, "Mew")
# print(my_class)

# pop() - like pop in JS to delete the last element
# my_class.pop(0) # put a numer to move an element from the array
# print(my_class)

# clear ()
# my_class.clear()
# print(my_class)

# Numeric List Operation

# Sum
# scores = [2, 3, 50, 151, 0.5]
# scores_average = sum(scores) / len(scores)
# print (scores_average)

# min() and max()
# print ("min", min(scores))
# print("max", max(scores))

# num=[1,2,3,4,5,6,7,8,9,10]
# squares = []
# for n in num:
#     squares.append(n*n)
# print(squares)

# List Comprehension : to reduce the codes into one line
# Syntax
# since its a list it will start with [<expresion of what you want> for <item> in <list>]
# squares = [ n*n for n in num]
# print(squares)

# # i want n*n, if n * n is even
# even_squares = [n*n for n in num if (n*n) %2 ==0]
# print (even_squares)
# odd_squares = [n*n for n in num if (n*n) %2 ==1]
# print (odd_squares)

# Listing Scorting
# scores = [100, 200, 0.0025, 1700, 50]

# # ascending
# scores.sort()
# print (scores)
# #Descending
# scores.sort(reverse=True)
# print(scores)
# #reverse
# scores.reverse
# print(scores)

# Python Tuples
# it is a readonly
# Syntax
# color = ('red', 'green', 'blue', 'yellow')
# print(type(color))
# print(color)
# # len
# print(len(color))

# empty_tuple = () : used for values that wont be changed. Like gender
# gender = (male, female)

# Syntax
# object_name = {key1: value1, value2, ...}

# dict = {}
# print (dict)

# adding element to a dictionary
# dict[0] = 'Hello'
# print (dict)

# dict[2] = 'world'
# print(dict)

# dict[3] = 1
# print(dict)

# dict['value_set'] = 2,3,4 # if you add [] it will be an array inside the object
# print(dict)

# Nested Dictionary
# five = 5
# dict [five] = {'Nested': {'1': 'Goodbye', '2':'Friend'}}
# print (dict)

# print (dict[5])
# print(dict[5]['Nested']['2'])

# Car
# car = {
#     "Brand": "Nissan",
#     "Model": "Pathfinder",
#     "Year": 2018,
#     "Color": ["white", "Blue", "red"]
# }
# print(car)

# #len
# print (len(car))

# #Type
# print(type(car))

# #printing all the keys
# print(car.keys)


# #Printing all the values
# print(car.values())

# Modify any value using key in a dictionary
# car ["Brand"] = "SomethingElse"
# print(car)

# del car ["Brand"]
# print(car)

# if 'Brand' in car:
#     print("Yes, Brand is one of the keys in car dictionary")

# # Looping though the object
# for key in car:
#     print(key, "=>", car[key])

# Python Dictionary Functions

# def drive(distance):
#     print("Vroom!!! We drove", distance, "KM")

# car = {
#     "Brand": "Nissan",
#     "Model": "Pathfinder",
#     "Year": 2018,
#     "Color": ["white", "Blue", "red"],
#     "drive": drive
# }
# car["drive"](19)


# Lab 01: The Movie Database
# Movie1 = {
#     "titel": "Who are you?",
#     "duration": "25 min",
#     "stars": ["Me", "Myself", "and Whooho"]
# }

# Movie2 = {
#     "titel": "Once upon a December",
#     "duration": "125 min",
#     "stars": ["Jakie", "Chan", "Big Kitty"]
# }

# Movie3 = {
#     "titel": "Harry Potter",
#     "duration": "90 min",
#     "stars": ["Danial", "Robert", "Ian", "and the rest"]
# }

# list = [Movie1, Movie2, Movie3]
# print(Movie1)
# print(Movie2)
# print(Movie3)


# Lab 02: The Reading List

# Book1 = 
# {
#     'Title': 'Pistacio part2',
#     'Author': 'Pistacio the author',
#     'Finished reading': True
# }
# Book2 =
# {
#     'Title': 'The Hobit,
#     'Author': 'JR Tolkin',
#     'Finished reading': False
# }


# Reading = [
# {
#     "titel": "Lord of the Rings",
#     "Author": "JR Tolkin",
#     "alreadyRead": False
# },
#  {
#     "titel": "Hobit?",
#     "Author": "JR Tolkin",
#     "alreadyRead": True
# },
# {
#     "titel": "End the Saga: The condemned",
#     "Author": "Maitham",
#     "alreadyRead": True
# }
# ]
# for Book in Reading:
#     if(Book["alreadyRead"] == False):
#         print('you still need to read' , Book["titel"] , 'by' , Book["Author"])
#     else:
#         print('you read', Book["titel"], 'by', Book["Author"])