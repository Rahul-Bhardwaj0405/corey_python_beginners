# def hello_func():
#     pass

# hello_func()  # pass means we are not doing anything now but it wont throw error while leaving it blank.

# def hello_func():
#     print("Hello Function!")

# hello_func()
# hello_func()
# hello_func()
# hello_func()



# def hello_func():
#     return 'Hello Functions'


# print(hello_func().upper())


# def hello_func(greetings, name):
#     return f" {greetings}, {name}"

# print(hello_func("Hi", "Rahul"))


# def hello_func(greetings, name='You'):
#     return f"{greetings}, {name}"

# print(hello_func("Hi"))


# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)

# student_info('Math', 'Art', name='Rahul', age=22)

# upack values of args and kwargs:

# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
# courses = ['Math', 'Art']
# info = {'name': 'Rahul', 'age': 22}

# student_info(*courses, **info)


month_days = [0, 31, 28, 31, 30]

def is_leap(year):
    return year % 4 == 0 and (year % 100 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return "Invalid month"
    if month == 2 and is_leap(year):
        return 29
    return month_days