# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 13:27:44 2023

@author: Nikamed
"""

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
# sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
# ismlar = [] # bo'sh ro'yxat

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# print("Birinchi meva: ", mevalar[0])
# print("Ikkinchi meva: ", mevalar[1])

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# print("Birinchi meva: ", mevalar[0].title())
# print("Ikkinchi meva: ", mevalar[1].upper())

# narhlar = [12000, 18000, 10900, 22000]
# print(narhlar[2] + narhlar[3])

# car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
# print(car_models[-1]) # Listning eng oxirgi elementiga -1 bilan murojat qilamiz 

# narhlar = [12000, 18000, 10900, 22000]
# narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
# narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
# narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
# print(narhlar)

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# mevalar.append("tarvuz") # mevalar ga tarvuz qo'shamiz
# print(mevalar)

# cars = [] # bo'sh ro'yxat yaratamiz
# cars.append('Lacetti') # ro'yxatga Lacetti mashinasini qo'shamiz
# cars.append('Nexia 3') # ro'yxatga Nexia 3 mashinasini qo'shamiz
# cars.append('Cobalt')  # ro'yxatga Cobalt  mashinasini qo'shamiz
# print(cars)

# cars = ['Lacetti', 'Nexia 3', 'Cobalt']
# cars.insert(0, 'Malibu') # 1-o'ringa yangi qiymat qo'shamiz
# print(cars)
# cars.insert(2, 'Damas') # 3-o'ringa yangi qiymat qo'shamiz
# print(cars)

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# del mevalar[1] # 2-element (anjir) ni o'chirib tashlaymiz
# print(mevalar)

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# mevalar.remove('shaftoli') # Ro'yxatdan shaftolini o'chirdik
# print(mevalar)

# hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
# hayvonlar.remove("mushuk") # Ro'yxatda 2 ta mushuk bor, ulardan birinchisi o'chadi
# print(hayvonlar)

# bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
# mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
# print("Men " + mahsulot + " sotib oldim")
# print("Olinmagan mahsulotlar: ", bozorlik)

# HWork
# isimlar = ['Anvar', 'Murod', 'Abbos']
# print('Salom ' + isimlar[0] + ', bugun choyxona bormi?')
# print(isimlar[1] + ', choyxonaga boramizmi?')
# print(isimlar[2] + ', choyxona soat 3 da')

# sonlar = [15, -5, 5, 2.3]
# # print(sonlar[0] - sonlar[1] + sonlar[2] / sonlar[3])
# sonlar[0] = 9
# son = sonlar[2]
# sonlar[2] = sonlar[3]
# sonlar[3] = son
# print(sonlar)

# t_shaxslar = ['Alisher Navoiy', 'Mirzo Ulug`bek']
# z_shaxslar = ['Alisher Uzoqov', 'Ziyoda']
# shaxs1 = t_shaxslar.pop(0)
# shaxs2 = z_shaxslar.pop(0)
# print('Men tarixiy shaxslardan ' + shaxs1 + ' bilan, zamonaviy shaxslardan esa ' + shaxs2 + ' bilan suhbatlashgan bolardim.')

# freand =[]
# freand.append('Abbos')
# freand.append('Nodir')
# freand.append('Zohid')
# freand.append('Iskandar')
# freand.append('Murod')
# freand.remove('Iskandar')
# freand.append('Jasur')
# freand.insert(0, 'Muxtor')
# freand.insert(3, 'Odil')
# mehmonlar =[]
# mehmonlar.append(freand.pop(0))
# mehmonlar.append(freand.pop(0))