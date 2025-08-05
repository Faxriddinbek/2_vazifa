# a = 1
# isim = input("Isim kiriting: ")
# while a<=10:
#     print(isim)
#     a+=1
#


# son = int(input("Sonni kiriting: "))
# yigindi = 0
#
# while son > 0:
#     raqam = son % 10
#     yigindi += raqam
#     son //= 10
#
# print("Raqamlar yig'indisi:", yigindi)

# ok = 10
#
# while ok >=1:
#     print(ok)
#     ok = ok - 1
# 3. While orqali 1 dan 100 gacha bo'lgan toq solar yig'indisini topuvchi dastur tuzing

ok = 1
natija = range(1,101,2)
natija_1 = 0
while ok <=100:
    for i in natija:
        natija_1 = natija_1 + i
        continue
    print(sum(natija_1))
    ok += 1







