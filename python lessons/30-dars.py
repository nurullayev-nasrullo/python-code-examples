class Avto:
    __num_avto = 0
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narh):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1
    
    def __repr__(self):
        """Obyekt haqida ma'lumot"""
        return f"Avto: {self.rang} {self.make} {self.model}"
    
    def __eq__(self,boshqa_avto):
        """Tenglik"""
        return self.narh == boshqa_avto.narh
    
    def __lt__(self,boshqa_avto):
        """Kichik"""
        return self.narh<boshqa_avto.narh
    
    def __le__(self,boshqa_avto):
        """Kichik yoki teng"""
        return self.narh<=boshqa_avto.narh
    

# class AvtoSalon:
#     """Avtosalon klassi"""
#     def __init__(self,name):
#         self.name = name
#         self.avtolar = []

#     def __repr__(self):
#         return f"{self.name} avtosaloni"
    
#     def add_avto(self,avto):
#         if isinstance(avto,Avto): # agar avto Avto klassidan bo'lsa
#             self.avtolar.append(avto)
#         else:
#             print("Avto obyketini kiriting")

#     def __len__(self):
#         return len(self.avtolar)
    

# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# print(avto1)

# x,y = 5,10
# print(x>y)
    
# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# avto1>avto2
    
# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# print(avto1>avto2)

# avto3 = Avto("Honda","Accord","Oq",2017,40000)
# print(avto1==avto3)

# matn = 'hello world'
# print(len(matn))
    
# sonlar = [12, 34, 56, 66]
# print(len(sonlar))

# len(avto1)

# salon1 = AvtoSalon("MaxAvto")
# print(salon1)

# Avto obyektlarini yaratamiz
# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)

# # Yuqoridagi obyektlarni salon1 ga qo'shamiz
# for avto in [avto1, avto2, avto3]: 
#     salon1.add_avto(avto)

# print(len(salon1))
    
# class AvtoSalon:
#     """Avtosalon klassi"""
#     def __init__(self,name):
#         self.name = name
#         self.avtolar = []

#     def __repr__(self):
#         return f"{self.name} avtosaloni"
    
#     def __len__(self):
#         return len(self.avtolar)
    
#     def add_avto(self,avto):
#         if isinstance(avto,Avto): # agar avto Avto klassidan bo'lsa
#             self.avtolar.append(avto)
#         else:
#             print("Avto obyketini kiriting")
    
#     def __getitem__(self,index):
#         return self.avtolar[index]
    
#     def __setitem__(self,index,value):
#         if isinstance(value,Avto):
#             self.avtolar[index]=value

# salon1 = AvtoSalon("MaxAvto")
# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)

# for avto in [avto1, avto2, avto3]: 
#     salon1.add_avto(avto)

# # print(salon1[2])
    

# avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
# salon1[0]=avto4
# print(salon1[0])
    

class AvtoSalon:
    """Avtosalon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def __len__(self):
        return len(self.avtolar)

    def __getitem__(self,index):
        return self.avtolar[index]
    
    def __setitem__(self,index,value):
        if isinstance(value,Avto):
            self.avtolar[index]=value
    
    def add_avto(self,*qiymat):
        for avto in qiymat: 
            if isinstance(avto,Avto):
                self.avtolar.append(avto)
            else:
                print("Avto obyketini kiriting")

    def __add__(self,qiymat):
        if isinstance(qiymat,AvtoSalon):
            yangi_salon =  AvtoSalon(f"{self.name} {qiymat.name}")
            yangi_salon.avtolar = self.avtolar + qiymat.avtolar
            return yangi_salon
        elif isinstance(qiymat,Avto):
            self.add_avto(qiymat)
        else:
            print(f"AvtoSalon ga {type(qiymat)} qo`shib bo`lmaydi")

    def __call__(self,*param):
        if param: # agar parametr bo'lsa
            for avto in param:
                self.add_avto(avto)
        else: # agar parametr bo'lmasa
            return [avto for avto in self.avtolar]


salon1 = AvtoSalon("MaxAvto")
salon2 = AvtoSalon("Avto Lider")

avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
avto5 = Avto("Volkswagen","Polo",'Qora',2015,30000)
avto6 = Avto("Honda","Accord","Oq",2017,42000)

salon1.add_avto(avto1, avto2, avto3)
salon2.add_avto(avto4, avto5, avto6)

salon3 = salon1+salon2
# print(salon3)
# print(salon3[:])

avto7 = Avto("BMW", 'X7','Qora',2015,75000)
salon1 + avto7
# print(salon1[:])


avto_new = Avto("Mercedes-Benz", 'E200','Silver',2015,80000)
salon1(avto_new) # Yangi avto qo'shamiz
salon1() # salondagi mashinalarni ko'ramiz


# ==-== Home work ==-==
class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def __repr__(self):
        return f"{self.ism} {self.familiya}"


class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil,bosqich=1):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.bosqich = bosqich

    def __lt__(self,boshqa_talaba):
        """Kichik"""
        return self.bosqich < boshqa_talaba.bosqich

    def __eq__(self,boshqa_talaba):
        return self.bosqich == boshqa_talaba.bosqich
    


class Fan:
    def __init__(self,name):
        self.name = name
        self.talabalar = []

    def add_student(self):
        pass

    def __getitem__(self):
        pass

    def __setitem__(self):
        pass

    def __len__(self):
        return len(self.talabalar)
    

talaba1 = Talaba("Alijon","aliyev","ff86546",1992,2)
talaba2 = Talaba("valijon","shamsiyev","aa86464",2000)
# print(talaba1==talaba2)
# print(talaba1>talaba2)
