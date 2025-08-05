# 1 - misol
# son = int(input("Son kiriting: "))
# natija = ""
# for i in str(son):
#     if i == "4":
#         natija+= "7"
#     elif i == "7":
#         natija+= "4"
#     else:
#         natija+= i
# print(natija)
# 2- misol
# def teskari_soz(matn):
#     harflar = ''.join(ch for ch in matn if not ch.isdigit())
#     return harflar[::-1]
# matn = "A1b2c3d4"
# print(teskari_soz(matn))
# from yangisi_pdp import natija_1


# 3 - misol
# data = (("apple", 3), ("banana", 5), ("cherry", 2))
# new_dict = {}
# for i in data:
#     a = i[0]
#     b = i[1]
#     new_dict[a] = b
# print(new_dict)

# 4 - misol
# scores = [(1, 78), (2, 95), (3, 88), (4, 65)]
# natijasi = sorted(scores, key=lambda x: x[1], reverse=True)
# print(natijasi)

# 5 - misol
# son = int(input("Sonni kiriting: "))
# with open("data.txt", "r") as file:
#     ok = file.read().split()
#     natija = 0
#     for i in range(son+1):
#         for j in ok:
#             natija+= int(j)
#     print(natija/son)

# soz = "programmalash"
# natija = ""
# a = soz[::2]
# b = soz[1::2][::-1]
# natija+= a
# natija+= b
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














