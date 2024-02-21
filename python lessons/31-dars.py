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
# # print(pi)


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
birthday = '27121992'
with open('pi_million_digits.txt','r') as fayl:
    pi = fayl.read()
    answar = isinstance(birthday, pi)
    
print(answar)