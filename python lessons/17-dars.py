# ismlar = []

# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break


# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())


# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh) # ism kalit, yosh qiymat
    
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False

# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")


# cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
# while 'nexia' in cars: # toki nexia cars ro'yxati ichida ekan...
#     cars.remove('nexia') # nexia ni ro'yxatdan olib tashla
# print(cars)

# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho


# ===-=== Home works ===-===
# ==-== N1 ==-==
# orders = []
# print("Enter your orders ")
# n=1
# while True:
#     question = f"Enter {n}-food:"
#     order = input(question)
#     orders.append(order)
#     answer = input("Do you want mor food? (yes/no)")
#     if answer =='yes':
#         n+=1
#         continue
#     else:
#         break

# =-= 2 method =-=
# orders = []
# while True:
#     question = input("Enter your orders: ")
#     orders.append(question)
#     answer = input("Do you want any orders? (yes/no)")
#     if answer != 'yes':
#         break

# print(f"Your orders: {orders}")

# ==-== N2 ==-==
# print("Products")
# products = {}
# meaning = True
# while meaning:
#     product = input("Enter product name: ")
#     price = input(f"{product.title()} price: ")
#     products[product] = int(price)
    
#     answer = input("Do you want enter any product? (yes/no)")
#     if answer == "no":
#         meaning = False

# for product, price in products.items():
#     print(f"{product.title()} price: {price}")

# ==-== N3 ==-==
# orders = []
# print("Enter your orders ")
# n=1
# while True:
#     question = f"Enter {n}-food:"
#     order = input(question)
#     orders.append(order)
#     answer = input("Do you want mor food? (yes/no)")
#     if answer =='yes':
#         n+=1
#         continue
#     else:
#         break

# products = {
#     'banana':5,
#     'pineapple':8,
#     'kiwi':6,
#     'bread':3,
#     'sausage':10
# }

# while orders:
#     order = orders.pop()
#     product = products.get(order)
#     if product == None:
#         print(f"We have not {order}")
#     else:
#         print(f"{order} price: {product}")

# =-= 2 method =-=
# while orders:
#     order = orders.pop()
#     if order in products.keys():
#         price = products[order]
#         print(f"{order.title()} price: {price} $")
#     else:
#         print(f"We have not {order}")
