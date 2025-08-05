# def upper_dekarator(func):
#     def qamrov(*args, **kwargs):
#         natija = func(*args, **kwargs)
#         return natija.upper()
#     return qamrov
# @upper_dekarator
# def ok(name):
#     return f" Salom {name}"
# arr = ok("faxriddin")
# print(arr)
# import time
# def time_decaretion(func):
#     def wrapper(*args, **kwargs):
#         star_time = time.time()
#         natija = func(*args, **kwargs)
#         finish_time = time.time()
#         print(f"{func.__name__} uchun {finish_time - star_time: .2f} sekund vaqt ketti")
#         return natija
#     return wrapper
#
# @time_decaretion
# def some_function():
#     a = 0
#     for i in range(999999999):
#         a += 5
#
# some_function()

def count_cal(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_cal
def some_funk():
    a = 0
    for i in range(5):
        a += 5
    return a
f = some_funk()
g = some_funk()
q = some_funk()
print(some_funk.calls)

n , count = 5 , 0




















