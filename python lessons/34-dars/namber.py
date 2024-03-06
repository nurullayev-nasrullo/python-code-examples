# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 09:36:30 2024

@author: Nasrullo Nurullayev
"""
def give_number(a,b,c):
    if a<b and c<b:
        return b
    elif a>b and a>c:
        return a
    else:
        return c
