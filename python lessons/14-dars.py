# talaba_0 = {
#     'ism':'alijon',
#     'familiya':'shamshiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#     }

# print(talaba_0.items())

# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n")

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }

# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")

# mahsulotlar = { # Do'kondagi mahsulotlar
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }

# print(mahsulotlar.keys())

# print('Do\'kondagi mahsulotlar:')
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())


# bozorlik = ['anor','uzum','non','baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum} ham olib keling")

# print("Do'konimizdagi mahsulotlar:")    
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())


# print(telefonlar.values())
# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel)

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawei p30',
#     'tohir':'iphone x',
#     'umar':'iphone x'    
#     }

# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel)


# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in set(telefonlar.values()):
#     print(tel)


# ===-=== Home Work ===-===
# ==-== N-1 ==-==
# dic = {
#     'integer':'butun sonlar',
#     'float':'qoldiqli sonlar',
#     'string':'satirli malumot',
#     'if':'mantiqiy operator',
#     'else':'mantiqiy operator',
#     'swich':'mantiqiy operator',
#     'variable':'ozgaruvchi',
#     'arrays':'masivlar',
#     'function':'funksiya',
#     'liner_function':'chiziqli funksiya'
#     }


# sorted_words = sorted(dic.items())
# for word, val in sorted_words:
#     print(f"{word.title()} - {val.title()}")


# ==-== N-2A ==-==
# countries = {
#     'Uzbekistan':'Tashkent',
#     'Kazakstan':'Nursulton',
#     'Tajikistan':'Dushanbe',
#     'Russia':'Moscow',
#     'Albania':'Tirana'
# }

# countrie = sorted(countries.keys())
# capital = sorted(countries.values())

# print('Countres:')
# for countr in countrie:
#     print(countr.upper())

# print(f'\nCapitals:')
# for i in capital:
#     print(i)

# ==-== N-2B ==-==
# countries = {
#     'Uzbekistan':'Tashkent',
#     'Kazakstan':'Nursulton',
#     'Tajikistan':'Dushanbe',
#     'Russia':'Moscow',
#     'Albania':'Tirana'
# }
# countrie = input('Which country do you wont know: ').title()
# if countrie in countries:
#     print(countries[countrie])
# else:
#     print("Sorry, we don't have that information")

# ==-== N-3 ==-==
menu = {
    'freas':25,
    'pizza':30,
    'hotdog':35,
    'burger':30,
    'cheezburger':35,
    'sendvich':25,
    'soup':30,
    'creemsoup':60,
    'beefshtecks':125,
    'juice':15
}

foods = {}
print('Please enter 3 foods: ')
foods[0] = input('1-food: ')
foods[1] = input('2-food: ')
foods[2] = input('3-food: ')

# for 
if foods.values() in menu.keys():
    print(f"{foods.title()} {menu.values()} $")
else:
    print('Sorry we has not this food!')
