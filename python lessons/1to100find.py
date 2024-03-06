# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 12:22:11 2024

@author: Nasrullo Nurullayev
"""

#JUMBOQ1 - 1 dan 100 gacha sonlar ro'yxatidan qolib ketgan sonni topish

import random
n = 100
numbers = list(range(1, n + 1))
x = numbers.pop(random.randint(1, n + 1))
print(x)
# x ni toping

# No tog'ri usul resurslarni kop ishlatadi
# numbers2 = list(range(1, n + 1))
# print(sum(numbers2) - sum(numbers))


# Range faqat Pythonga xos funksiya
# for i in range(1,n):
#     if i not in numbers:
#         print(i)
#         break



# Optimal va tog'ri variant
summa = n * (n + 1) / 2
print(summa - sum(numbers))