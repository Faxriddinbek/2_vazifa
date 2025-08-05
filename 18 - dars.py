class Person:
    def __init__(self, name, age, gender):
        self.name = name   # atribut
        self.age = age  # atribut
        self.gender = gender # atribut
doe = Person(name="Doe", age=12, gender="Erkak")
print(f"Ismi {doe.name} Yoshi {doe.age} jinsi {doe.gender}")