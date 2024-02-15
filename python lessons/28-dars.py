class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    

# inson = Shaxs("Hasan","Alimov","FB001122",1995)
# print(f"{inson.get_info()}. {inson.get_age(2021)} yoshda.")


# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self, ism, familiya, passport, tyil):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)


# talaba = Talaba("Valijon","Aliyev","FA112299",2000)
# print(talaba.get_info())
# print(talaba.get_age(2021))

# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self, ism, familiya, passport, tyil,idraqam):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1
    
#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam
    
#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich
    


# talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012")
# print(f"{talaba.get_info()}. ID raqami:{talaba.get_id()}")
# print(f"{talaba.get_bosqich()}-bosqich talabasi")
    
# ===-=== Polimorfizm ===-===
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []
    
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def fanga_yozil(self,matematika,fizika):
        self.fanlar.append(matematika)
        self.fanlar.append(fizika)

    def remove_fan(self,fan):
        for i in self.fanlar:
            if fan != i:
                print("Siz bu fanga yozilmagansiz")
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info

# talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012")
# print(talaba.get_info())

class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self,uy,kocha,tuman,viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
    
    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil
    

class Fan:
    def __init__(self,name):
        self.name = name



class Professor(Shaxs):
    def __init__(self, ism, familiya, passport, tyil,tajriba,ish_joyi):
        super().__init__(ism, familiya, passport, tyil)
        self.tajriba = tajriba
        self.ish_joyi = ish_joyi

    def get_tajriba(self):
        return self.tajriba
    
    def get_ishjoyi(self):
        return self.ish_joyi

    def get_info(self):
        """Professor haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Tajribam: {self.get_tajriba()} yil. Hozirgi ish joyim: {self.get_ishjoyi()}"
        return info


class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, passport, tyil,user_name,email):
        super().__init__(ism, familiya, passport, tyil)
        self.u_name = user_name
        self.email = email

    def get_username(self):
        return self.u_name
    
    def get_email(self):
        return self.email

    def get_info(self):
        """Foydalanuvchi haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"User name: {self.get_username()}. Email adress: {self.get_email()}"
        return info
    

class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, passport, tyil, user_name, email):
        super().__init__(ism, familiya, passport, tyil, user_name, email)

    def ban_user(self):
        print("Foydalanuvchi bloklandi")


matematika = Fan("Oliy matematika")
fizika = Fan('Fizika')
    

talaba_manzil = Manzil(12,'Olmazor',"Bog'bon","Samarqand")
talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012",talaba_manzil)
print(talaba.manzil.get_manzil())
print(talaba.manzil.tuman)
