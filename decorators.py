# import time

# def time_name(func):
#     def wrapper():
#         t1 = time.time()
#         func()
#         print(t1)
#     return wrapper()


# @time_name
# def name():
#     print('Kacper')


#Task 1
# def multiply2(func):
#     def wrapper(*args, **kwargs):
#         wynik = func(*args, **kwargs)
#         return wynik * 2
#     return wrapper

# @multiply2
# def add(a, b):
#     return a + b

# print(add(2, 4))

#Task 2
def login(func):
    def wrapper(*args):
        name = func(*args)
        print(f'Powitano {name}')
    return wrapper

@login
def greet(name):
    return f"Hi, {name}"

greet('Kacper')
