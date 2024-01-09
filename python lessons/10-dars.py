import math
# avtolar = ['audi','bmw','volvo','kia','hyundai']
# for avto in avtolar: # avtolar ichidagi har bir avto uchun ...
#     if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
#         print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
#     else: # aks holda ... 
#         print(avto.title()) # avto nomini faqat birinchi harfini katta bilann yoz.

# ism = input('Ismingiz nima?\n>>>') # Foydalanuvchi ismini so'raymiz
# if ism.lower() != 'ali': # Agar ism Aliga teng bo'lmasa ...
#     print(f"Uzr, {ism.title()} biz Alini kutayapmiz.") # quyidagi xabar chiqadi
# else:
#     print("Salom, Ali")

# javob = float(input("12x6 nechiga teng?>>>"))
# if javob!=72:
#     print("Javob xato!")

# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh>=18: # yosh 18 dan katta yoki teng bo'lsa
#     print('Xush kelibsiz!')
# else: # ask holda
#     print('Kirish mumkin emas!')

# login = input("Yangi login tanlang:")
# if len(login)<=5: # login uzunligini tekshiramiz
#     print("Login 5 harfdan ko'proq bo'lishi shart!")

# yil = int(input("Tug'ilgan yilingizni kiriting:"))
# if 2020-yil<18: # foydalanuvchining yoshini hisoblaymiz
#     print(f"Yoshingiz {2020-yil}da ekan.")
#     print("Kirish mumkin emas!")
# else:
#     print("Xush kelibsiz!")

# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")

# x, y = 25, 50 # x=25 va y=50
# print("x>y") if x>y else print("x<y")

# HWork

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())

# login = input('Loginni kiriting: ')
# if login.lower() == 'admin':
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f'Xush kelibsiz, {login}!')

# x = input('1- son kiriting: ')
# y = input('2- son kiriting: ')

# if x == y:
#     print('Sonlar teng ekan')

# number = int(input('Istalgan son kiriting: '))
# if number >= 0:
#     print('Musbat son')
# else:
#     print('Manfiy son')

numb = int(input('Son kiriting: '))
if numb > 0:
    print(math.sqrt(numb))
else:
    print('Musbat son kiriting')