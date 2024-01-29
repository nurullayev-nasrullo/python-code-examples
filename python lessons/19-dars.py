# def toliq_ism_yasa(ism, familiya):
#     """Toliq isma qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism # qiymat qaytarish uchun return operatorini ishlatamiz

# talaba1 = toliq_ism_yasa('olim','hakimov')
# talaba2 = toliq_ism_yasa('hakim','olimov')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """Toliq isma qaytaruvchi funksiya"""
#     if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()

# talaba1 = toliq_ism_yasa('olim','hakimov') #otasining_ismi kiritilmadi
# talaba2 = toliq_ism_yasa('hakim','olimov','abrorovich')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")

# def oraliq(min,max,step=1):
#     sonlar = [] # bo'sh ro'yxat
#     while min<max:
#         sonlar.append(min)
#         min += step
#     return sonlar

# print(oraliq(0,10))
# print(oraliq(10,21))
# print(oraliq(0,21,2))

# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end='')
#     kompaniya=input("\nIshlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
    
#     #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#     #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break

# print('\nSalonimizdagi avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang'].title()} {avto['model'].title()}, {korobka} korobka. Narhi: {narh}")

# ===-=== Home works ===-===
# ==-== N1 ==-==
# def user_info(ismi, familiya, tug_yili, tug_joyi, email=None, telefon=None):
#     user = {'ism':ismi,
#             'familiya':familiya,
#             'tugilgan yili':tug_yili,
#             'tugilgan joyi':tug_joyi,
#             'email':email,
#             'telefon':telefon,
#             'yoshi':2024-tug_yili}
#     return user

# ==-== N2 ==-==
# mijozlar = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end='')
#     ismi=input("\nIsmingizni kiriting: ")
#     familiya=input("Familiyanizni kiriting: ")
#     tug_yili=int(input("Tug'ilgan yilinizni kiriting: "))
#     tug_joyi=input("Tug'ilgan joyingizni kiriting: ")
#     email=input("emailingizni kiriting: ")
#     telefon=input("Telefon raqamingizni kiriting: ")
    
#     #Foydalanuvchi kiritdan ma'lumotlardan user_info yordamida 
#     #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     mijozlar.append(user_info(ismi, familiya, tug_yili, tug_joyi, email, telefon))
    
#     # Yana mijoz qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana mijoz qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break

# print('\nMijozlar:')
# for user in mijozlar:
#     if user['email'] and user['telefon']:
#         email = user['email']
#         telefon = user['telefon']
#     elif user['telefon'] and user['email'] == None:
#         telefon = user['telefon']
#         email = "Noma'lum"
#     elif user['telefon'] == None and user['email']:
#         email = user['email']
#         telefon = "Noma'lum"
#     else:
#         email = "Noma'lum"
#         telefon = "Noma'lum"
#     print(f"{user['ism'].title()} {user['familiya'].title()}, {user['tugilgan yili']} yilda {user['tugilgan joyi'].title()}da tug'ilgan, email manzili: {user['email']}, telefon raqami: {user['telefon']}, yoshi: {user['yoshi']}")

# ==-== N3 ==-==
# def max_number(a, b, c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c


# a = int(input('1-sonni kiriting: '))
# b = int(input('2-sonn: '))
# c = int(input('3-sonn: '))

# max = max_number(a,b,c)
# print(f"orasida eng kattasi: {max}")

# ==-== N4 ==-==
# def aylana(r):
#     ayl = {'radiusi':r,
#             'diametri':r+r,
#             'perimetri':2*3.14*r,
#             'yuzi':3.14*(r**2),
#             }
#     return ayl

# r = int(input('Aylana radiusini kiriting: '))
# R = aylana(r)
# print(f"Aylana R: {R['radiusi']}, D: {R['diametri']}, P: {R['perimetri']}, S: {R['yuzi']}")

# ==-== N5 ==-==
def tub_sonlar(a,z):
    sonlar = [] # bo'sh ro'yxat
    while a<z:
        if a % 2 == 0:
            continue
        elif a % 3 == 0:
            continue
        elif a % 1 and a % a:
            sonlar.append(a)
        a += 1
    return sonlar

a = int(input('1-sonni kiriting: '))
z = int(input('2-sonni kiriting: '))
tub_son = tub_sonlar(a,z)
print(tub_son)