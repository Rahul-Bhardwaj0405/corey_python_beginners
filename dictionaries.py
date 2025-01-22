student = {'name': 'Rahul', 'age': 25, 'courses': ['Math', 'CompSci']}
# print(student)
# print(student['name'])
# print(student.get('phone')) # If key doesn't exist then, get will return none by default.
# print(student.get('phone', 'not Found')) # change the default value of get.


# ****Adding new entry to dictionary***************

# student['phone'] = '555-5567'
# print(student)

# if key alredy exist and we want to upadte value :

# student['name'] = 'Jane'
# print(student)

# we can also use update method to update value , but it is used when you want to update multiple values:

# student.update({'name': 'Jane', 'age': 34, 'phone': '555-55567'})
# print(student)

# Delete specfic key and its value:

# del student['age']
# age = student.pop('age')
# print(student)
# print(age)


#****LOOP through Dictionary

# print(len(student))
# print(student.keys())
# print(student.values())
# print(student.items())

for key, value in student.items():
    print(key, value)