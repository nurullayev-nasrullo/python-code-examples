# car0 = {
#         'model':'lacetti',
#         'rang':'oq',
#         'yil':2018,
#         'narh':13000,
#         'km':50000,
#         'korobka':'avtomat'
#         }

# car1 = {
#         'model':'nexia 3',
#         'rang':'qora',
#         'yil':2015,
#         'narh':9000,
#         'km':89000,
#         'korobka':'mexanika'
#         }

# car2 = {
#         'model':'gentra',
#         'rang':'qizil',
#         'yil':2019,
#         'narh':15000,
#         'km':20000,
#         'korobka':'mexanika'
#         }

# car = car0
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")

# car = car1
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")

# car = car2
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")

# cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model'].title()}, "
#           f"{car['rang']} rang, "
#           f"{car['yil']}-yil, {car['narh']}$")
    

# print(cars[0])
# print(cars[0]['model'])

# print(f"{cars[2]['rang'].title()} "
#       f"{cars[2]['model']}")

# malibus=[] # Malibu mashinalari uchun bo'sh ro'yxat yaratdik
# for n in range(10):
#     new_car = { # har bir yangi mashina uchun lug'at yaratamiz
#         'model':'malibu',
#         'rang':None, # rangi noaniq
#         'yil':2020,
#         'narh':None, # narhi belgilanmagan
#         'km':0,
#         'korobka':'avto'
#         }
#     malibus.append(new_car) # yangi lug'atni ro'yxatga qo'shamiz


# for malibu in malibus[:3]:
#     malibu['rang']='qizil'

# for malibu in malibus[3:6]:
#     malibu['rang']='qora'

# for malibu in malibus[6:]: # ohirgi 4 ta mashinani
#     malibu['rang']='qora'  # rangi qora
#     malibu['korobka']='mexanika' # korobkasi mexanika

# for malibu in malibus:
#     if malibu['korobka']=='avto':
#         malibu['narh']=40000
#     else:
#         malibu['narh']=35000

# print(malibus)

# dasturchilar = {
#     'ali':['python','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'maryam':['c++','c#']
#     }

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end=' ')
#     for til in tillar:
#         print(f'{til.upper()}', end=' ')


# hamkasblar = {
#     'ali':{'familiya':'valiyev',
#            'tyil':1995,
#            'malumot':'oliy',
#            'tillar':['python','c++']
#            },
#     'vali':{'familiya':'aliyev',
#             'tyil':2001,
#             'malumot':"o'rta-maxsus",
#             'tillar':['html', 'css', 'js']},
#     'hasan':{'familiya':'husanov',
#              'tyil':1999,
#              'malumot':'maxsus',
#              'tillar':['python','php']}
#     }

# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}, "
#           f"{info['tyil']}-yilda tug'ilgan. "
#           f"Ma'lumoti: {info['malumot']}. \n"
#           "Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())

# ===-=== Home Works ===-===
# ==-== N1 ==-==

# jobs = {
#     'name':'Steve Jobs',
#     'born':'1955',
#     'city':'San Francisco',
#     'old':'56 died',
#     'jobs':['Apple', 'iMac', 'iPod']
# }
# tim = {
#     'name':'Tim Berners-Lee',
#     'born':'1955',
#     'city':'London',
#     'old':68,
#     'jobs':['hypertext concept', 'HTTPD', 'W3C']
# }
# bill = {
#     'name':'Bill Gates',
#     'born':'1955',
#     'city':'Seattle',
#     'old':68,
#     'jobs':['Microsoft', 'MS-Dos', 'Xbox']
# }
# james = {
#     'name':'James Gosling',
#     'born':'1955',
#     'city':'Calgary',
#     'old':68,
#     'jobs':['Java', 'Emacs', 'Newa']
# }

# it_greats = [jobs, tim, bill, james]

# for person in it_greats:
#     print(f"{person['name'].title()}, "
#           f"was born is {person['born']}, "
#           f"{person['city']}, he is {person['old']} old")

# ==-== N2 ==-==
# for person in it_greats:
#     print(f"\n{person['name'].title()} jobs:")
#     for j in person['jobs']:
#         print(j)

# ==-== N3 ==-==
# films = {
#     'joe':['row', 'iron first', 'jumange'],
#     'sem':['home alone 1,2,3', 'Castenvilla', 'Krid 1,2,3'],
#     'kris':['dancer', 'step up 1,2,3,4', 'back to future']
# }
# for persone, film in films.items():
#     print(f"\n{persone.title()}'s favorit films:")
#     for i in film:
#         print(i.title())

# ==-== N4 ==-==
countries = {
    'uzbekistan':{'capital':'tashkent',
                  'area':'448978',
                  'population':'33000000',
                  'currency':'sum'
                },
    'russia':{'capital':'moscow',
                  'area':'17098246',
                  'population':'147182123',
                  'currency':'rub'
                },
    'united states':{'capital':'washington',
                  'area':'9833520',
                  'population':'334914895',
                  'currency':'usd'
                }
}

for country, item in countries.items():
    print(f"\n{country.title()} capital is {item['capital'].title()}")