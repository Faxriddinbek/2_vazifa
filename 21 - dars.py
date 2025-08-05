import json
# import pickle
# from uuid import uuid4
import os
# f = open("matn_tex", "r")
# for i in f:
#   print(i)



# os.remove("matn_tex")

dog_data = {
  "name": "Frieda",
  "is_dog": True,
  "hobbies": ["eating", "sleeping", "barking",],
  "age": 8,
  "address": {
    "work": None,
    "home": ("Berlin", "Germany",),
  },
  "friends": [
    {
      "name": "Philipp",
      "hobbies": ["eating", "sleeping", "reading",],
    },
    {
      "name": "Mitch",
      "hobbies": ["running", "snacking",],
    },
  ],
}
#
# with open("hello_frieda.json", mode="w", encoding="utf-8") as write_file:
#     json.dump(dog_data, write_file)





# data = {
#     "prezident" : {
#         "ismi" : "Shavkat Mirziyoyev",
#         "Davlari" : "O'zbekiston"
#     }
# }
# talaba = {"isim":"Faxriddin"}
# # with open('pi.txt', 'a') as fayl:
# #     fayl.write("Alijon Valiyev\n")
# #     fayl.write("2000")
# print(ok)

#                         Json bilan ishlash

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# print(json.dumps(x, indent=4, sort_keys=True))
# with open("yangi.json", "w") as new_file:
#   json.dump(x, new_file, indent=4)


dog_registry = {1: {"name": "Frieda"}}
dog_json = json.dumps(dog_registry)










