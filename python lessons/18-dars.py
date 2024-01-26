# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")

# salom_ber()

# def salom_ber(ism):
#     """Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")

# salom_ber('Husan')
# salom_ber() # Type Error missing 1 argument
    
# print(salom_ber.__doc__)
# salom_ber('hasan')
# salom_ber('olim')
    
# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")

# toliq_ism('olim','hakimov')

# def yosh_hisobla(ism, tugilgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2024-tugilgan_yil} yoshda")

# yosh_hisobla('olim', 1997)

# yosh_hisobla(1997, 'olim') # attributError
    
# yosh_hisobla(tugilgan_yil=1997, ism='olim')

# def yosh_hisobla(tugilgan_yil, joriy_yil=2024): # joriy yil uchun st.qiymat 2024
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")


# yosh_hisobla(1995,2020)
# yosh_hisobla(1993)

# ==-== Errors ==-==
# def yosh_hisobla(tugilgan_yil, joriy_yil=2020):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
# tyil = input("Tug'ilgan yilingizni kiriting: ")
# yosh_hisobla(tyil)

# def yosh_hisobla(tugilgan_yil, joriy_yil):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

# yosh_hisobla(1993)

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")

# salom_ber('hasan')

# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
 
# toliq_ism('olim hakimov')

# ===-=== Home works ===-===
# ==-== N1 ==-==
# def years_old(name, birth):
#     """Counting age function"""
#     print(f"{name.title()} your age is {2024-birth}")


# name = input('Enter your name: ')
# age = int(input('Enter your birth year: '))
# years_old(name=name, birth=age)


# ==-== N2 ==-==
# def square(numb):
#     """Function square and cube number"""
#     print(f"Square {numb} is {numb**2}",
#           f"\nCube {numb} is {(numb**2)*numb}")
    

# number = int(input('Enter number: '))
# square(number)

# ==-== N3 ==-==
# def even_odd(numb):
#     """Function even and odd"""
#     if numb % 2 == 0:
#         print(f"{numb} is even")
#     else:
#         print(f"{numb} is odd")

# number = int(input('Enter your number: '))
# even_odd(number)
    

# ==-== N4 ==-==
# def big_small(numb1, numb2):
#     """Function big or small nubers"""
#     if numb1 == numb2:
#         print(f"Numbers {numb1} and {numb2} is equal")
#     elif numb1 < numb2:
#         print(f"{numb1} small {numb2}")
#     else:
#         print(f"{numb1} big {numb2}")


# nuber1 = input('Enter number 1: ')
# nuber2 = input('Enter number 2: ')
# big_small(nuber1, nuber2)

# ==-== N5 ==-==
# def square_x(x, y=2):
#     """Function x square(y)"""
#     print(x**y)

# x = int(input('Enter x:'))
# y = int(input('Enter y: '))
# square_x(x, y)

# ==-== N6 ==-==
# def numb(number):
#     for i in range(2, 11):
#         if number % i == 0:
#             print(f"{number} divisible {i}")

# number = int(input('Enter your number: '))
# numb(number)
