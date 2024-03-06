# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 11:18:27 2024

@author: Nasrullo Nurulayev
"""

def give_numbers(a):
    b = []
    for i in a:
        if i % 2 == 0:
            b.append(i)
            
    return b