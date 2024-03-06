# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 14:30:29 2024

@author: Nasrullo Nurullayev
"""

# with open('pi.txt') as fayl:
#     pi = fayl.read()
    
# pi = pi.rstrip() # qator ohiridagi bo'shliqlarni olib tashlaymiz
# pi = pi.replace('\n','') # qator tashlash belgisini almashtiramiz
# pi = float(pi) # matnni float (o'nlik) songa o'tkazamiz
# print(pi)


# faylnomi = 'ustozlar.txt'# ochilayotgan (yaratilayotgan) fayl nomi
# with open(faylnomi,'w') as fayl:
#     fayl.write('anvar narzullaev') # faylga yozilayotgan ma'lumot
    

    
    
# faylnomi = 'new_file.txt'
# ism = 'Olimjon Hasanov'
# tyil = 2004
# with open(faylnomi,'w') as fayl:
#     fayl.write(ism+'\n')
#     fayl.write(str(tyil)+'\n')
    

# with open(faylnomi,'a') as fayl:
#     fayl.write('Alijon Valiyev\n')
#     fayl.write('2000')
    
    
# import pickle

# talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2003, 'kurs': 2}
# talaba2 = {'ism':'alijon', 'familiya':'valiyev', 'tyil':2004, 'kurs': 1}

# with open('info','wb') as file:
#     pickle.dump(talaba1,file)
#     pickle.dump(talaba2,file)
    
    
# with open('info','rb') as file:
#     talaba1 = pickle.load(file)
#     talaba2 = pickle.load(file)
    
    
# print(talaba1)
# print(talaba2)


# ==-== Home Work ==-==
# =-= N1 =-=
# faylnomi = 'matn.txt'
# learn_1 = 'with'
# learn_2 = 'pickle'
# learn_3 = 'w - write'
# learn_4 = 'r - read'
# learn_5 = 'dump'
# learn_6 = 'load'

# with open(faylnomi,'w') as fayl:  
#     fayl.write(learn_1+'\n')
#     fayl.write(learn_2+'\n')
#     fayl.write(learn_3+'\n')
#     fayl.write(learn_4+'\n')
#     fayl.write(learn_5+'\n')
#     fayl.write(learn_6+'\n')
    
# with open(faylnomi,'r') as fayl:
#     text = fayl.read()
    
# print(text)

# =-= N2 =-=
# birthday = '27121992'
# with open('pi_million_digits.txt','r') as fayl:
#     pi = fayl.read()

# def find_num(x):
#     namb = pi.find(x)
#     if namb == -1:
#         return False
#     else:
#         return True

# day = find_num(birthday)
# print(day)

# =-= N3 =-=
# import pickle
# with open('pi_million_digits.txt','r') as fayl:
#     pi = fayl.read()
    
    
# pi = pi.rstrip()
# pi = pi.replace('\n','')
# pi = pi.replace(' ','')
# pi = float(pi)

# with open('pi_digits','wb') as file:
#     pickle.dump(pi,file)

# =-= N4 =-=
# name = input('Familiya ismingizni kiriting: ')
# tyil = input('Tugilgan yilingizni kiriting: ')
# kurs = input('Kursingizni kiriting: ')
# with open('input_file.txt', 'a') as fayl:
#     fayl.write(f"{name}\n")
#     fayl.write(f"{tyil}\n")
#     fayl.write(f"{kurs}\n")
    
    
# Alternativ
import pickle

with open('pi_million_digits.txt') as file:
    pi = file.read()
pi = pi.rstrip() # qator ohiridagi bo'shliqlarni olib tashlaymiz
pi = pi.replace('\n','') # qator tashlash belgisini almashtiramiz
pi = pi.replace(' ','')

# Tug'ilgan kunim pi da bormi?
bdate = '27121992'
print(bdate in pi)

pi = float(pi) # matnni float (o'nlik) songa o'tkazamiz

with open('pi_float.dat','wb') as file:
    pickle.dump(pi,file)







