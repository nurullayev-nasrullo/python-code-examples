# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
    
#     def get_info(self):
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
#     def set_bosqich(self,bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich

#     def update_bosqich(self):
#         """Talabanining bosqichini 1taga ko'paytirish"""
#         self.bosqich += 1
    
# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.get_info())

# talaba1.bosqich= 2
# print(talaba1.bosqich)

# talaba1.set_bosqich(3)
# print(talaba1.get_info())

# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.get_info())

# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())

# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())

# class Fan():
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
    
#     def add_student(self,talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1

#     def get_students(self):
#         return [talaba.get_info() for talaba in self.talabalar]


# matematika = Fan("Oliy Matematika")
# talaba1 = Talaba("Alijon","Valiyev",2000)
# talaba2 = Talaba("Hasan","Alimov",2001)
# talaba3 = Talaba("Akrom","Boriyev",2001)

# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)

# print(matematika.talabalar_soni)

# print(matematika.talabalar)

# mat_talabalar = matematika.get_students()
# print(mat_talabalar)

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
      
#     def set_bosqich(self,bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich
        
#     def update_bosqich(self):
#         """Talabanining bosqichini 1taga ko'paytirish"""
#         self.bosqich += 1    
    
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
    
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya
    
#     def get_fullname(self):
#         """Talabaning ism-familiyasini qaytaradi"""
#         return f"{self.ism} {self.familiya}"
    
#     def get_age(self,yil):
#         """Talabaning yoshini qaytaradi"""
#         return yil-self.tyil
    
# class Fan():
#     """Fan nomli klass"""
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
    
#     def add_student(self,talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
    
#     def get_name(self):
#         """Fan nomi"""
#         return self.nomi
    
#     def get_students(self):
#         """Fanga yozilgan talabalar haqida ma'lumot"""
#         return [x.get_info() for x in self.talabalar]
    
#     def get_students_num(self):
#         """Fanga yozilgan talabalar soni"""
#         return self.talabalar_soni
    

# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False]

# talaba1 = Talaba("Alijon","Valiyev",2000)

# print(see_methods(Talaba))

# print(see_methods(talaba1))

# print(talaba1.__dict__)

# print(talaba1.__dict__.keys())

class Avto:
    def __init__(self,model,rang,karobka,narh):
        self.model=model
        self.rang=rang
        self.karobka=karobka
        self.narh=narh
        self.kilometer=0

    def get_model(self):
        return self.model
    
    def get_rang(self):
        return self.rang
    
    def get_karobka(self):
        return self.karobka
    
    def get_narh(self):
        return self.narh
    
    def update_km(self,kilometer):
        self.kilometer += kilometer
    
    def get_info(self):
        print(f"Modeli: {self.model}, rangi: {self.rang}, karobka: {self.karobka}, narhi: {self.narh} $")



class Avtosalon:
    def __init__(self,name,adress):
        self.name=name
        self.adress=adress
        self.cars=[]

    def add_cars(self,car):
        self.cars.append(car)

    def get_name(self):
        return self.name
    
    def get_adress(self):
        return self.adress
    
    def get_info(self):
        print(f"")
        
    def get_students(self):
        return [x.get_info() for x in self.cars]
    

avto1 = Avto("cobalt","qora","avto",25000)
# print(avto1.get_narh)

# print(avto1.__dir__)
# print(avto1.__dict__)

    