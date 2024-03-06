# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:42:46 2024

@author: Nasrullo Nurullayev
"""

# ===-=== RegEx ===-===
import re

# word1 = "темир"
# word2 = "томир"
# word3 = "тулпор"

# andoza = "^т...р"

# print(re.match(andoza, word1))
# print(re.match(andoza, word2))
# print(re.match(andoza, word3))


from uzwords import words
# andoza = "^т...р$"

# matches = []
# for word in words:
#     if re.match(andoza,word):
#         matches.append(word)
# print(matches)




# авв ҳарфларидан бошланган сўзларни топамиз
# andoza = '^авв'
# andoza = '^авв...'
# 6 harfdan iborat, лоқ bilan tugaydigan matn uchun andoza
andoza = '...лоқ$'
matches = []
[matches.append(word) for word in words if re.match(andoza, word)]
print(matches)