# ******LIST*****
# courses = ['Histrory', 'Math', 'Physics', 'ComputerScience']
# print(len(courses))
# print(courses[-2])
# print(courses[0:2])
# print(courses[:2])
# print(courses[2:])

# ****Adding items in the list and its various method to do that***:

# courses.append('Art')  #It will add 'Art' at the end of the list
# courses.insert(0, 'Art') # Use this if you want to insert something at specfic location in the list
# course_2 = ['Art', 'Education']
# courses.extend(course_2)
# print(courses)

# ****Remove Item from the list***
# courses.remove('Math')
# popped=courses.pop() # It will remove the last item from the list by default and its return the pop item means last value in list.
# print(popped)
# print(courses)

# ****Reverse a List***
# courses = ['History', 'Math', 'Physics', 'ComputerScience']
# nums = [5,6,73,4,2]
# courses.reverse()
# courses.sort() # sort in alphabetical order
# nums.sort()
# nums.sort(reverse=True)
# output = sorted(courses) # sorted function return sorted list . so, we have to save it in variable.
# print(nums)
# print(output)

# ***min, max and sum***:
# print(min(nums))
# print(max(nums))
# print(sum(nums))

# **Find index of certain item***:
# print(courses.index('Math'))

# If we want to check a certain item is on our list or not:
# print('Math' in courses) # It will return True or False 
# for item in courses:
#     print(item)

# for index, item in enumerate(courses): # it will return the item as well as the index of item
#     print(index, item)

#**If we want to enumerate from certain index:

# for index, item in enumerate(courses, start=1): #It will loop from first index
#     print(index, item)

# If we want to turn list into strings separated by ceratin value:

# courses = ['History', 'Math', 'Physics', 'ComputerScience']
# courses_str = ', '.join(courses)
# print(courses_str)

# #**Convert strings into list:
# courses_list = courses_str.split(', ')
# print(courses_list)


# List comprehension
# list_one = [1,2,3,4,5,6,7,8,9]
# print([item for item in list_one if item%3==0])



# *****TUPLES**************************

# Mutable

# list_1 = ['History', 'Math', 'Physics', 'ComputerScience']
# list_2 = list_1
# print(list_1)
# print(list_2)

# list_1[0] = 'Art'
# print(list_1)
# print(list_2)

# IMmutable (tuple):

# tuple_1 = ('History', 'Math', 'Physics', 'ComputerScience')
# tuple_2 = tuple_1
# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Art'
# print(tuple_1)
# print(tuple_2)

# Creating a tuple
tuple1 = (1, 2, 3, 4)
tuple2 = ("apple", "banana", "cherry")
tuple3 = (1, "apple", 3.14, [1, 2, 3])

# Accessing elements
print(tuple1[0])  # Output: 1
print(tuple2[1])  # Output: banana
print(tuple3[2])  # Output: 3.14

# Slicing a tuple
print(tuple1[1:3])  # Output: (2, 3)
print(tuple2[:2])   # Output: ('apple', 'banana')
print(tuple3[2:])   # Output: (3.14, [1, 2, 3])

# Concatenating tuples
tuple4 = tuple1 + tuple2
print(tuple4)  # Output: (1, 2, 3, 4, 'apple', 'banana', 'cherry')

# Repeating tuples
tuple5 = tuple1 * 2
print(tuple5)  # Output: (1, 2, 3, 4, 1, 2, 3, 4)

# Using count()
tuple6 = (1, 2, 3, 2, 4, 2)
print(tuple6.count(2))  # Output: 3

# Using index()
print(tuple6.index(2))  # Output: 1

# Unpacking a tuple
a, b, c, d = tuple1
print(a, b, c, d)  # Output: 1 2 3 4

# Nested tuples
nested_tuple = (1, (2, 3), (4, 5))
print(nested_tuple[1])     # Output: (2, 3)
print(nested_tuple[1][0])  # Output: 2

# Immutability of tuples
try:
    tuple1[0] = 10
except TypeError as e:
    print(e)  # Output: 'tuple' object does not support item assignment


# Note : we we want something to modify use "LIST" and if we want to access or loop through items we can use "TUPLE".



#******************************SET**** set are the values that are unordered and also have no duplicates. 
# It is used mainly to remove duplicate value and also to check whether certain value is part of the set or not.



# cs_courses =  {'History', 'Math', 'Physics', 'ComputerScience', 'Math'}
# print(cs_courses)
# cs_courses =  {'History', 'Math', 'Physics', 'ComputerScience'}
# print('Math' in cs_courses) 

cs_courses =  {'History', 'Math', 'Physics', 'ComputerScience'}
art_courses = {'History', 'Math', 'Art', 'Design'}

# print(cs_courses.intersection(art_courses)) # It will show comman couses  from both the set.

# print(cs_courses.difference(art_courses)) # It will show which courses are different in cs_courses from art courses.

print(cs_courses.union(art_courses))


# Creating a set
set1 = {1, 2, 3, 4}
set2 = set([1, 2, 3, 4])

set1.add(5)
print(set1)  # Output: {1, 2, 3, 4, 5}

set1.update([6, 7])
print(set1)  # Output: {1, 2, 3, 4, 5, 6, 7}

set1.remove(7)
print(set1)  # Output: {1, 2, 3, 4, 5, 6}

set1.discard(6)
print(set1)  # Output: {1, 2, 3, 4, 5}

removed_element = set1.pop()
print(removed_element)  # Output: 1 (or any other element)
print(set1)  # Output: {2, 3, 4, 5}

set1.clear()
print(set1)  # Output: set()

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
print(set3)  # Output: {1, 2, 3, 4, 5}


set4 = set1.intersection(set2)
print(set4)  # Output: {3}

set5 = set1.difference(set2)
print(set5)  # Output: {1, 2}

set6 = set1.symmetric_difference(set2)
print(set6)  # Output: {1, 2, 4, 5}

set7 = {1, 2}
print(set7.issubset(set1))  # Output: True

print(set1.issuperset(set7))  # Output: True

set8 = {6, 7}
print(set1.isdisjoint(set8))  # Output: True

set9 = set1.copy()
print(set9)  # Output: {1, 2, 3, 4, 5}

print(len(set1))  # Output: 5

print(3 in set1)  # Output: True
print(6 in set1)  # Output: False


# Create empty list, tuple and set

# Empty List(2 ways to do it)
empty_list = []
empty_list = list()

#Empty Tuple

empty_tuple = ()
empty_tuple = tuple()


# Empty set

empty_set = set()





