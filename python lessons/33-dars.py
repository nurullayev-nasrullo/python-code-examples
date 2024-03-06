# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 11:22:50 2024

@author: Nasrullo Nurullo
"""

# ==-== try-except ==-==
# yosh = input("Yoshingizni kiriting: ")
# yosh = int(yosh)
# print(f"Siz {2024-yosh} yilda tug'ilgansiz")

# =-= ValueError
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)  
#     print(f"Siz {2021-yosh} yilda tug'ilgansiz")  
# except:
#     print("Butun son kiritmadingiz")

# print("Dastur Tugadi!")

# =-= try-except-else
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)    
# except:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2021-yosh} yilda tug'ilgansiz")

# =-= ValueError
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)    
# except ValueError:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2021-yosh} yilda tug'ilgansiz")

# =-= ZeroDivisionError
# x,y=5,10
# try:
#    y/(x-5)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
    
    
# =-= IndexError
# mevalar = ['olma','anor','anjir','uzum']
# try:
#     print(mevalar[7])
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")

# =-= KeyError
# user = {"username":"sariqdev",
#         "status":"admin",
#         "email":"admin@sariq.dev",
#         "phone":"99897123456"}

# key="tel"
# try:
#     print(f'Foydalanuvchi: {user[key]}')
# except KeyError:
#     print("Bunday kalit mavjud emas")


# =-= FileNotFoundError
# filename = "data.txt" # bunday fayl mavjud emas
# with open(filename) as f:
#     text = f.read()
    
# filename = "data.txt" # bunday fayl mavjud emas
# try:
#     with open(filename) as f:
#         text = f.read()
# except FileNotFoundError:
#     print(f"Kechirasiz, {filename} fayli mavjud emas. Bosh fayl tanlang.")

# ==-== more Errors
# n = input("Butun son kiriting: ")
# try:
#     n = int(n)
#     x=20/n
# except ValueError: # agar foydalanuvchi butun son kiritmasa
#     print("Butun son kiritmadingiz")
# except ZeroDivisionError: # agar foydalanuvchi 0 kiritsa
#     print("0 ga bo'lib bo'lmaydi")
# else:
#     print(f"x={x}")

# ==-== hiden Errors
# import json
# files = ['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
# for filename in files:
#     try:
#         with open(filename) as f:
#             talaba = json.load(f)        
#     except FileNotFoundError:
#         print(f"{filename} mavjud emas")
#     else:
#         print(talaba['ism'])
#         # fayl ustida turli amallar 
        
    
# import json
# files = ['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
# for filename in files:
#     try:
#         with open(filename) as f:
#             talaba = json.load(f)        
#     except FileNotFoundError:
#         pass
#     else:
#         print(talaba['ism'])

# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh.isdigit():
#         yosh = int(yosh)
#         break        

# print(f"Siz {2021-yosh} yilda tug'ilgansiz")

