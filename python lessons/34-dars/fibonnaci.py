# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 14:33:13 2024

@author: Nasrullo Nurullayev
"""

def fibonacci(n):
    sonlar = []
    for i in range(10):
        if i == 0 or i == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[i - 1] + sonlar[i - 2])
    
    x = n in sonlar
    return x

