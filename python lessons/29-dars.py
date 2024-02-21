from uuid import uuid4
# class Avto:
#     """Avtomobil klassi"""
#     def __init__(self,make,model,rang,yil,narh,km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
    
#     def get_km(self):
#         return self.__km
    
#     def get_id(self):
#         return self.__id
    
#     def add_km(self,km):
#         """Mashinaning km ga yana km qo'shish"""
#         if km>=0:
#             self.__km += km
#         else:
#             print("Mashina km kamaytirib bo'lmaydi")
    

# avto1 = Avto("GM","Malibu","Qora",2020,40000,100000)
# avto1.__km

# print(f"ID: {avto1.get_id()}")

# avto1.add_km(1500)
# print(avto1.get_km())

# class Avto:
#     """Avtomobil klassi"""
#     __num_avto = 0
#     def __init__(self,make,model,rang,yil,narh,km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
#         # Avto.num_avto += 1
#         """Inkapsulyatsiya"""
#         Avto.__num_avto += 1


# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# print(avto1.num_avto)
# avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
# print(Avto.num_avto)

# ==-== Classga oid methodlar ==-==
# class Avto:
#     """Avtomobil klassi"""
#     __num_avto = 0
#     def __init__(self,make,model,rang,yil,narh,km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
#         Avto.__num_avto += 1
    
#     @classmethod
#     def get_num_avto(cls):
#         return cls.__num_avto
    


# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
# print(Avto.get_num_avto())

# ==-== Home work ==-==
class Shaxs:
    odamlar_soni = 0
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.__tyil = tyil
        Shaxs.odamlar_soni +=1


    @classmethod
    def get_odamlar_soni(cls):
        return cls.odamlar_soni
    
    def get_tyil(self):
        return self.__tyil

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.get_tyil()}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.__tyil
    

class Talaba(Shaxs):
    talabalar_soni = 0
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil,idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.__idraqam = idraqam
        self.bosqich = 1
        Talaba.talabalar_soni += 1
    
    @classmethod
    def get_talabalar_soni(cls):
        return cls.talabalar_soni
    def get_id(self):
        """Talabaning ID raqami"""
        return self.__idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    

talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012")
print(f"{talaba.get_info()}. ID raqami:{talaba.get_id()}")
print(f"{talaba.get_bosqich()}-bosqich talabasi")
print(Shaxs.get_odamlar_soni())
print(Talaba.get_talabalar_soni())
