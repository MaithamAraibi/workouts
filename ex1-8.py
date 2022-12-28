# #01 - Students list

studentsname = ["maitham", "George", "Theo"]
# positive value
print (studentsname [0])
print (studentsname [1])
print (studentsname [2])

#negative value
print (studentsname [-2])
print (studentsname [-1])
print (studentsname [0])


# # Ex 02: Tuple food

food = ('Pizza', 'Legendary Burger Well-done', 'Sandwich Ice Cream')
for meal in food:
    print (f"{meal} was delicious food")

# # # Ex 3: print the last two items
# for food in meal [-2:]:
#   print(meal) #I got 3 ice creams XD 

# # Ex 4: home town population
# home_town = {
#     'city' : 'Jid Hafus',
#     'state' : 'Shamaliya',
#     'population' : 1200
# }
# # dictionary is only small letters
# print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

# # # Ex 5: print each key and value

# for key, value in home_town.items():
#   print(f"{key} = {value}")

# # Ex 6: cohort loop #food and studentsname list

cohort = []
for index, student in enumerate(studentsname):
  cohort.append({
    'student': student,
    'fav_food': meal[index]
  })

for student in cohort:
  print(student)

# # Ex 7: call for studentsname and make them awesome.

awesome_students = [f"{name} is awesome!" for name in studentsname]

for student in awesome_students:
  print(student)

# # Ex 8: call for food list and single out the letter 'a'
for food in  [food for food in meal if 'a' in food]:
    print (food)