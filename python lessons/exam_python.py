# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:28:03 2024

@author: Nasrullo Nurullayev
"""
import random
def user_name():
    name = input('Ismingizni kiriting: ')[::-1]
    return f"Sizning uchun generatsiya qilingan username: {name}{random.randint(0, 9)}"


def Convert_add(num=['1','3','5']): 
    return sum([int(i) for i in num])