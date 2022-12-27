# 1 Vowel or Consonant

# letter = input('Please enter a letter from the alphabet (a-z or A-Z): ').lower()
# if letter in 'a e i o u':
#   print(f'The letter {letter} is a vowel')
# else:
#   print(f'The letter {letter} is a consonant')


# 2 Length of Phrase

# phrase = ''
# while phrase != 'quit':
#   phrase = input('Please enter a word or phrase: ')
#   print(f'What you entered is {len(phrase)} characters long')



# 3 Dog Year

# human_years = int(input("Input a dog's age in human years: "))
# if human_years < 3:
#   dog_years = human_years * 10
# else:
#   dog_years = 20 + (human_years - 2) * 7
# print(f"The dog's age in dog years is {dog_years}")


# 04 Triangle

# print('Enter the lengths of three side of a triangle:')
# a = input('a: ')
# b = input('b: ')
# c = input('c: ')

# if a == b and b == c:
#   print(f'A triangle with sides of {a}, {b} & {c} is an equalateral triangle')
# elif a != b and a != c and b != c:
#   print(f'A triangle with sides of {a}, {b} & {c} is a scalene triangle')
# else:
#   print(f'A triangle with sides of {a}, {b} & {c} is an isosceles triangle')


# ex-05

# a = 1
# b = 1
# for term in range (50):
#   if term < 2:
#     print('term: {term} / number: {term}')
#   else:
#     c = a + b
#     print(f'term: {term} / number: {c}')
#     a = b
#     b = c

# term = 0
# a = 0
# b = 1
# while term < 50:
#   if term < 2:
#     print(f'term: {term} / number: {term}')
#   else:
#     num = a + b
#     print(f'term: {term} / number: {num}')
#     a = b
#     b = num
#   term += 1


# # ex 06 

# mo = input('Enter the month of the season (Jan - Dec):')
# day = int(input('Enter the day of the month:'))
# if input_month in ('Jan', 'Feb', 'Mar'):
#     mo = input('Enter the month of the season (Jan - Dec): ')
# day = int(input('Enter the day of the month: '))
# if mo in ('Jan', 'Feb', 'Mar'):
#   season = 'Winter'
# elif mo in ('Apr', 'May', 'Jun'):
#   season = 'Spring'
# elif mo in ('Jul', 'Aug', 'Sep'):
#   season = 'Summer'
# else:
#   season = 'Fall'
# if mo == 'Mar' and day > 19:
#   season = 'Spring'
# elif mo == 'Jun' and day > 20:
#   season = 'Summer'
# elif mo == 'Sep' and day > 21:
#   season = 'Fall'
# elif mo == 'Dec' and day > 20:
#   season = 'Winter'
# print(f'{mo} {day} is in {season}')


# mo = input('Enter the month of the year (Jan - Dec): ')
# day = int(input('Enter the day of the month: '))
# if mo in ('Dec', 'Jan', 'Feb'):
#   season = 'Fall' if mo == 'Dec' and day < 21 else 'Winter'
# elif mo in ('Mar', 'Apr', 'May'):
#   season = 'Winter' if mo == 'Mar' and day < 20 else 'Spring'
# elif mo in ('Jun', 'Jul', 'Aug'):
#   season = 'Spring' if mo == 'Jun' and day < 21 else 'Summer'
# else:
#   season = 'Summer' if mo == 'Sep' and day < 22 else 'Fall'
# print(f'{mo} {day} is in {season}')



# count('orange')

# def count(sentence):
#     vowels= ['a' , 'u' , 'e' , 'i' , 'o' , "A" , "E" , 'I' , "O" , 'U']
#     for char in range(len(sentence)):
        

# count('orange')



def getCount(scentence):
    num_vowels = 0
    for char in scentence:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels + 1
    return num_vowels
