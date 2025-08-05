# 1 - misol
# try:
#     text = ("Salom", "dunyo")
#     text["Salom"] = "Assalom"
# except TypeError:
#     print("Tuple turini o'zgartirib bo'lmaydi")
# else:
#     print(text)
# 2 - misol
# try:
#     text = ["olma", "anor", "Shaftoli"]
#     ok = int(input("Index kiriting: "))
#     natija_1 = text[ok]
# except ValueError:
#     print("Siz butun son kiritmadingiz: ")
# else:
#     print(natija_1)

# 3 - misol
# try:
#     yil = int(input("Kabisa yili kiriting: "))
#     if    yil%4 == 0 and yil%400 != 0:
#         print("Kabisa yilini to'g'ri kiritdingiz")
#     else:
#         print("Kabisa yilini to'g'ri kiritmadingiz")
# except ValueError:
#     print("Faqat butun son kiritnadingiz!!!")

# 4 - misol
# try:
#     raqamlar = input("Raqamlar ro'yxatini kiriting (vergul bilan): ")
#     royxat = [float(x.strip()) for x in raqamlar.split(",")]
#     ortacha = sum(royxat) / len(royxat)
#     print("O'rtacha qiymat:", ortacha)
# except ValueError:
#     print("Xatolik: Barcha elementlar raqam bo‘lishi kerak.")

# 5 - misol
# try:
#     son_1 = int(input("Son_1 kiriting: "))
#     son_2 = int(input("Son_2 kiriting: "))
#     print(son_1 - son_2)
# except ValueError:
#     print("Siz butun son kritmadingiz!!!")
# finally:print("Hisoblash yakunlandi")
# 6 - misol
# try:
#     boluvchi = int(input("bo'luvchini kiriting: "))
#     bolinuvchini = int(input("bo'linuvchini kiriting: "))
# except ValueError:
#     print("Siz butun son kiritmadingiz")
# except ZeroDivisionError:
#     print("Sonni 0 ga bo'lish mumkin emas")
# else: print(bolinuvchini/boluvchi)
# # else blokda bo'lsam exsept ishlamidi !!!

# 7 - misol
# try:
#     dic = int(input("Kalit kiriting: "))
#     mevalar = {1:"olma", 2:"anor", 3:"shaftoli", 4:"nok", 5:"gilos", 6:"kakos"}
#     print(mevalar[dic])
# except KeyError:
#     print("Bunday index majud emas")

# 8 - misol

# Faylni ochish va har bir satrni o‘qib ishlash
# with open("pi.txt", 'r') as fayl:
#     for satr in fayl:
#         satr = satr.strip()
#         try:
#             son = int(satr)
#             print(son)
#         except ValueError:
#             print('Xato')

# 9 - misol
# try:
#     lis = [1, 2, 3, 4, 5, "Salom dunyo"]
#     for i in lis:
#         ok = int(i)
#         print(ok)
# except :
#     print("Listda string turi ham mavjud")
# else:
#     print("Dastur muvaffaqiyatli bajarildi")

# 10 - misol
# try:
#     my_list = []
#     if not my_list:
#         raise ValueError("Ro'yxat bo'sh!")
#     total = 0
#     for number in my_list:
#         total += number
#     print("Ro'yxatdagi sonlar yig'indisi:", total)
# except ValueError as e:
#     print("Xatolik:", e)
# else:
#     print("Amallar muvoffaqiyatli bajarildi.")
# finally:
#     print("Dastur yakunlandi.")

# Rasimdagi misollar
# 1 - misol
# soz = "programmalash"
# natija = ""
# a = soz[::2]
# b = soz[1::2][::-1]
# natija+= a
# natija += b
# print(natija)
# 2 - misol
# def dekodla(kodlangan):
#     n = len(kodlangan)
#     yarim = (n + 1) // 2
#     juft = kodlangan[:yarim]
#     toq = kodlangan[yarim:][::-1]
#     natija = [''] * n
#     j = 0
#     for i in range(0, n, 2):
#         natija[i] = juft[j]
#         j += 1
#     j = 0
#     for i in range(1, n, 2):
#         natija[i] = toq[j]
#         j += 1
#     return ''.join(natija)
# kodlangan = "Pormamagr"
# print(dekodla(kodlangan))

# 3 - misol
# s = input("Satrni kiriting: ")
# letters = [ch for ch in s if ch.isalpha() and ch.islower()]
# for i in range(1, len(letters)):
#     if letters[i] < letters[i - 1]:
#         print("Qonuniyatni buzgan harf:", letters[i])
#         break
# else:
#     print(0)
# 4 - misol
# s = input("Satrni kiriting: ")
# stack = []
# for i, ch in enumerate(s):
#     if ch == '(':
#         stack.append(i)
#     elif ch == ')':
#         if stack:
#             stack.pop()
#         else:
#             print(i)
#             break
# else:
#     if stack:
#         print(-1)
#     else:
#         print(0)

# 5 - misol
# s = input("Satrni kiriting: ")
# stack = []
# qavs_juftlik = {')': '(', ']': '[', '}': '{'}
# for i, ch in enumerate(s):
#     if ch in '([{':
#         stack.append((ch, i))
#     elif ch in ')]}':
#         if not stack:
#             print(i)
#             break
#         oxirgi, idx = stack.pop()
#         if qavs_juftlik[ch] != oxirgi:
#             print(i)
#             break
# else:
#     if stack:
#         print(-1)
#     else:
#         print(0)

