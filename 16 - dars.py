# def group_generator(lst, n):
#     stask = [(0, [])]
#     while stask:
#         idx, current_group = stask.pop()
#         if len(current_group) == n:
#             yield tuple(current_group)
#         else:
#             for i in range(idx, len(lst)):
#                 new_group = current_group + [list[i]]
#
#                   Dekaratorlar
# def deco(friends, *args):
#     for f in args:
#         def g(*args, **kwargs):
#             nonlocal friends
#             friends = f(*args, **kwargs)
#         return g
#
# @deco
# def func(x):
#     return 2*x
# # func = deco(func)
# print(func(2))

# def deco(f):
#     def g(*args, **kwargs):
#         return f(*args, **kwargs)
#     return g
# @deco
# def func(x):
#     print("Ma'lumot  turi")
#     return 2*x
# print(func(4))

# def update_dekorator():





















