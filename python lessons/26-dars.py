# x = 10
# print(type(x))

# matn = "salom"
# print(type(matn))

# def salom_ber():
#     print("Assalom alaykum")

# print(type(salom_ber))

# matn = "salom"
# print(matn.upper())

# son = 20
# print(son.lower())

class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
    
    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism
    
    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya
    
    def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"
    
    def get_age(self,yil):
        """Talabaning yoshini qaytaradi"""
        return yil-self.tyil
    
    def tanishtir(self):
        print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")


# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.ism)
# print(talaba1.familiya)

# talaba2 = Talaba("Olim","Olimov",1995)
# talaba3 = Talaba("Husan","Akbarov",2004)
# talaba4 = Talaba("Hasan","Akbarov",2004)

# print(talaba2.ism)
# print(talaba4.familiya)


# talaba4 = Talaba("Hasan","Akbarov",2004)
# talaba4.tanishtir()

# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.get_fullname())


# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.get_age(2021))


class User:
    def __int__(self,name,username,email):
        self.name = name
        self.uname = username
        self.mail = email

    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.name
    
    def get_uname(self):
        """Talabaning ismini qaytaradi"""
        return self.uname
    
    def get_email(self):
        """Talabaning ismini qaytaradi"""
        return self.mail
    
    def describe():
        pass
    
    def get_email():
        pass


    def get_info(self):
        print(f"Foydalanuchi: {self.uname}, ismi: {self.name}, email: {self.mail}")


