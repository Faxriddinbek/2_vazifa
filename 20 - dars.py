import time


# Kodlarni qaytadan yozaman va taxlil qilaman


# class Student:
#     school_name = "TDTU"
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def change_school(cls, school_name):
#         cls.school_name = school_name
#
#     def show(self):
#         print(self.name, self.age, "school:", Student.school_name)

# faxriddin = Student("Faxriddin", 21)
# faxriddin.show()
#
# Student.change_school("Astrum Akademy")
# faxriddin.show()
#
#
# from datetime import date

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def calculate_age(cls, name, birth_year):
#         # calculate age an set it as a age
#         # return new object
#         return cls(name, date.today().year - birth_year)
#
#     def show(self):
#         print(self.name + "'s age is: " + str(self.age))
#
# jessa = Student('Jessa', 20)
# jessa.show()
#
# # create new object using the factory method
# joy = Student.calculate_age("Joy", 1995)
# joy.show()

# class Employe:
#     @staticmethod
#     def sample(x):
#         print("nimalardir", x)
# Employe.sample(10)

# class Employe(object):
#     def __int__(self, name, salary, projekt_name):
#         self.name = name
#         self.salary = salary
#         self.projekt_name = projekt_name
#
#     @staticmethod
#     def gether_requirement(projekt_name):
#         if projekt_name == "Bekend":
#             ok = ['nom_1', 'nom_2', 'nom_3']
#         else:
#             ok = ['nom']
#         return ok
#
# #     instens metods
#     def work(self):
#         ok = self.gether_requirement(self.projekt_name)
#         for i in ok:
#             print('Completed', i)
#
# emp = Employe("Faxriddin", 12000, "lalala")
# emp.work()

class Shaxs:
    """Shaxs haqida ma'lumot"""
    def __init__(self, isim, familya, pasport, tyil):
        self.ism = isim
        self.familya = familya
        self.pasport = pasport
        self.tyil = tyil

    def get_info(self):
        """shaxs xaqida ma'lumot"""
        info = f"{self.ism} {self.familya}.\n"
        info += f"Passport: {self.pasport}, {self.tyil} - yilda tug'ilgan."
        return info
    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return f"{yil- self.tyil} - yoshda."

# men = Shaxs("Faxriddin", "O'rinboyev", "AC2809886", 2004)
# print(men.get_info())
# print(men.get_age(2025))
class Manzil:
    def __init__(self, manzil):
        self.manzil = manzil
    def show_manzil(self):
        return self.manzil

class Talaba(Shaxs):
    def __init__(self, isim, familya, pasport, tyil, id, manzil_1):
        """Talabaning Xususiyatlari"""
        super().__init__(isim, familya, pasport, tyil)
        self.idraqam = id
        self.bosqich = 1
    def get_id(self):
        return self.idraqam
    def get_bosqich(self):
        return self.bosqich
manzil = Manzil("Andijon")
men = Talaba("Faxriddin", "O'rinboyev", "AC2809886", 2004,"90106898", manzil)
print(f"{men.get_info()}. ID: {men.get_id()}, Manzi: {manzil.show_manzil()}")








