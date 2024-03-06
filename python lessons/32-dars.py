# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 11:38:57 2024

@author: Nasrullo Nurullayev
"""

import json


# x = 10
# x_json = json.dumps(x)

# ism = "anvar"
# ism_json = json.dumps(ism)

# sonlar = [12, 45, 23, 67]
# sonlar_json = json.dumps(sonlar)

# print(type(sonlar_json))

# bemor = {
#   "ism": "Alijon Valiyev",
#   "yosh": 30,
#   "oila": True,
#   "farzandlar": ("Ahmad","Bonu"),
#   "allergiya": None,
#   "dorilar": [
#     {"nomi": "Analgin", "miqdori": 0.5},
#     {"nomi": "Panadol", "miqdori": 1.2}
#   ]
# }

# bemor_json = json.dumps(bemor)
# print(bemor_json)

# bemor_json = json.dumps(bemor, indent=4)
# print(bemor_json)


# bemor = {
#   "ism": "Alijon Valiyev",
#   "yosh": 30,
#   "oila": True,
#   "farzandlar": ("Ahmad","Bonu"),
#   "allergiya": None,
#   "dorilar": [
#     {"nomi": "Analgin", "miqdori": 0.5},
#     {"nomi": "Panadol", "miqdori": 1.2}
#   ]
# }

# with open('bemor.json','w') as f:
#     json.dump(bemor,f)
    
    
# sonlar = json.loads(sonlar_json)
# bemor = json.loads(bemor_json)
# print(bemor)


# filename = 'bemor.json'
# with open(filename) as f:
#     bemor = json.load(f)
    
# print(type(bemor))


# ==-== Home work ==-==
# =-= N1 =-=
# data = {"Model":"Malibu", "Rang":"Qora", "Yil":2020, "Narh":40000}
# data_json = json.dumps(data, indent=4)
# print(data_json)

# =-= N2 =-=
# talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
# talaba = json.loads(talaba_json)

# print(f"{talaba['ism']} {talaba['familiya']}")

# =-= N3 =-=
# with open('data.json','w') as f:
#     json.dump(data,f)
    
# with open('talaba.json','w') as f:
#     json.dump(talaba,f)


# =-= N4 =-=
# with open('students.json', 'r') as f:
#     talabalar = json.load(f)

# for i in range(0,3):
#     print(f"{talabalar['student'][i]['name']} "
#           f"{talabalar['student'][i]['lastname']}, "
#           f"{talabalar['student'][i]['year']} - kurs, "
#           f"{talabalar['student'][i]['faculty']} talabasi")
    
# Alternativ
# for item in data["student"]:
#     print(f"{item['name']} {item['lastname']}." f" Faculty of {item['faculty']} ")    


# =-= N5 =-=
with open('api-result.json','r') as f:
    post = json.load(f)
    
    
print(f"{post['query']['pages']['13801']['title']}"
      f"\n{post['query']['pages']['13801']['extract']}")




