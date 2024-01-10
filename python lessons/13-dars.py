# car_0 = {'model':'ferrari','rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])

# talaba_0 = {'ism':'murod olimov','yosh':24,'t_yil':2000}
# # print(f"{talaba_0['ism'].title()},\
# #  {talaba_0['t_yil']}-yilda tu'gilgan,\
# #  {talaba_0['yosh']} yoshda")

# talaba_0['kurs'] = 4 # yangi, 'kurs' nomli kalit so'zga 4 qiymatini yuklaymiz
# talaba_0['fakultet'] = 'informatika' # 'fakultet' ga esa 'informatika'
# print(talaba_0)

# talaba_1 = {}
# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 20
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# talaba_1['kurs'] = 4 # 'kurs' ni 4 ga o'zgartiramiz.
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
# print(talaba_0)
# del talaba_0['yosh'] # yosh degan kalit so'z (va qiymatni) o'chiramiz
# print(talaba_0)

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }

# phone = telefonlar['ali']
# print(f"Alining telefoni {phone}")

# phone = telefonlar['hasan']
# print(f"Hasanning telefoni {phone}")

# phone = telefonlar.get('hasan','Bunday ism mavjud emas')
# print(phone)

# phone = telefonlar.get('hasan')
# print(phone)

# ===-=== Home Work ===-===
# ==-== N-1 ==-==
# father = {
#     'Name':'Akrom',
#     'years':'1958',
#     'city':'Samarkand'
# }

# print(f"My father's name {father['Name']}, born in {father['years']}, in the city of {father['city']}")

# ==-== N-2 ==-==
# favoriteFoods = {
#     'Ali':'Osh',
#     'Kamola':'Ikra',
#     'Akram':'Manti',
#     'Zuxra':'Baliq',
#     'Nasrullo':'Baray'
# }

# print(f"Brother's favorite food {favoriteFoods['Ali']},\
#     Sister's favorite food {favoriteFoods['Kamola']},\
#     Father's favorite food {favoriteFoods['Akram']}")

# ==-== N-3 ==-==
dic = {
    'integer':'butun sonlar',
    'float':'qoldiqli sonlar',
    'string':'satirli malumot',
    'if':'mantiqiy operator',
    'else':'mantiqiy operator',
    'swich':'mantiqiy operator',
    'variable':'ozgaruvchi',
    'arrays':'masivlar',
    'function':'funksiya',
    'liner_function':'chiziqli funksiya'
}

word = input('Kalit so`z kiriting: ')
# print(dic[word])
keyWord = dic.get(word)

if keyWord == None:
    print('Bunday so`z mavjud emas')
else:
    print(f"{word.title()} so'zi {keyWord} deb tarjima qilinadi")
