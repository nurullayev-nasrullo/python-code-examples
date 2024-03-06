# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 12:29:31 2024

@author: Nasrullo Nururllayev
"""
def get_full_name(ism, familiya, otasi=''):
    if otasi:
        return f"{ism} {otasi} {familiya}".title()   
    else:
        return f"{ism} {familiya}".title()
