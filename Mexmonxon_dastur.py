from tkinter.font import names
royhat = {
    "Faxriddin": ["12", "standart"],
    "Jhon": ["17", "premium"]
}
def chek(data, key, value):
    for i in data.values():
        try:
            if i[key] == value:
                return True
        except:
            pass
    return False


def qoshish():
    name = input("Isimni kiriting: ")
    while name in royhat.keys():
        print("Bunday shaxs mehmonhonada mavjud.")
        name = input("Isim kiriting: ")
    number = input("Raqam kiriting: ")
    while chek(royhat, 0,number):
        print("Bu xona band boshqa hona tanlang!!!")
        number = ("Raqam kiriting: ")

    def type():
        try:
            type = input("Xona belgilarini quyidagi belgilar orqali tanlang \n e - ekanom \n s - standart \n l - luyks \n")
            if type == "e":
                turi = "ekanom"
            elif type == "s":
                turi = "standart"
            elif type == "l":
                turi = "luyks"
            royhat[name] = [number, turi]
            print(f"{name} ro'yhatga qo'shildi \n \n")
        except Exception:
            print("Xato belgi kiritdingiz!!!sdhsfu")
            type()

    type()




def show():
    print("{:<18} {:<25} {:<20}".format('Isim', 'xona', 'turi'), "\n")
    for k, v in royhat.items():
        v_1, v_2 = v
        print("{:<18} {:<25} {:<20}".format(k, v_1, v_2))
    print("\n \n")


# Ro'yhatdan chiqarish funksiyasi
def minus():
    x = input("Kimni ro'yhatdan chiqarmoqchisiz.")
    if x in royhat.keys():
        royhat.pop(x)
        print(x, "Ro'yhatdan chiqarildi")
    else:
        print("Foydalanuvchi ro'yhatda mavjud emas")

# ro'yhatni ko'rish funsiyasi
def show():
    print("{:<18} {:<25} {:<20}".format('Ismi', 'Xonasi', 'Xona turi'), "\n")
    for k, v in royhat.items():
        v1, v2 = v
        print("{:<18} {:<25} {:<20}".format(k, v1, v2))
    print("\n \n")


# To'liq jarayon uchun algoritim
while True:
    sorov = input(""
    "          Xush kelibsiz! \n Buyruqni tanlang: \n 1 - mexmon qo'shing \n 2 - mexmoni ro'yhatdan chiqarish \n 3 - mehmonlar royhatini ko'rish \n")
    if sorov == "1":
        qoshish()
    if sorov == "2":
        minus()
    if sorov == "3":
        show()
    elif sorov == "0":
        break




