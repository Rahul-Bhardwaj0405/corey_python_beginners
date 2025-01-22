# language = 'Java'
# if language == 'Python':
#     print("Language is Python")
# elif language == 'Java':
#     print("Language is Java")
# else:
#     print("No Match")

# Note: Comaparison operators and boolean operations(and, or , not) mixed together

# user = 'Admin'
# logged_in = False
# if user == 'Admin' or logged_in:
#     print("Admin Page")
# else:
#     print("Bad Creds")


# user = 'Admin'
# logged_in = False
# if not logged_in:
#     print("Please log in")
# else:
#     print("Welcome")


#Note: Object identity(is): It tests if two objects have the same id which basically means if they are the same object in memory.so 
# two objects can actually be equal and not be the same objects in memory.

# a = [1,2,3]
# b = [1,2,3]
# # print(a == b)

# print(id(a))
# print(id(b))
# print(a is b)

# a = [1,2,3]
# b = a
# print(id(a))
# print(id(b))
# print(a is b)

#False Values:

#False
#None
#Zero of any numeric type ex:condition = 0
#Any empty sequence. for example: '', (), [].Ex: condition= '', condition= (), condition=[]
#Any empty mapping. for example: {}

condition = {}
if condition:
    print('Evaluted to True')
else:
    print('Evaluted to False')