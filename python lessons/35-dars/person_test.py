# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 09:53:32 2024

@author: Nasrullo Nurullayev
"""

import unittest
from person import Shaxs, Talaba

class PersonTest(unittest.TestCase):
    """Shaxs va Talaba klassini tekshirish uchun test"""
    def setUp(self):        
        ism = "Shoxruz"
        familiya = "Mubinov"
        pasport = "AA5456570"        
        self.tyil = 1999
        self.idraqam = 1235488
        self.bosqich = 1
        self.manzil = "Toshkent"
        self.shaxs1 = Shaxs(ism,familiya,pasport,tyil=self.tyil)
        self.talaba1 = Talaba(ism,familiya,pasport,tyil=self.tyil,idraqam=self.idraqam,manzil=self.manzil)
        
    def test_create(self):                
        # Qiymatlar mavjudligini assertIsNotNone metodi bilan tekshiramiz
        self.assertIsNotNone(self.shaxs1.ism)
        self.assertIsNotNone(self.shaxs1.familiya)
        self.assertIsNotNone(self.shaxs1.passport)
        self.assertIsNotNone(self.shaxs1.tyil)
        # Talaba Qiymatlar mavjudligini assertIsNotNone metodi bilan tekshiramiz
        self.assertIsNotNone(self.talaba1.idraqam)
        self.assertIsNotNone(self.talaba1.bosqich)
        self.assertIsNotNone(self.talaba1.manzil)
        # Qiymat tengligini assertEquals metodi bilan tekshiramiz
        self.assertEqual(25,self.shaxs1.get_age(2024))
        self.assertEqual(1235488,self.talaba1.get_id())
        self.assertEqual(1,self.talaba1.get_bosqich())
        self.assertEqual(self.tyil,self.talaba1.tyil)
    
    
    def test_get_info(self):
        shaxs1_info = 'Shoxruz Mubinov. Passport: AA5456570, 1999-yilda tug`ilgan'
        self.assertEqual(shaxs1_info,self.shaxs1.get_info())
        talaba1_info = 'Shoxruz Mubinov. 1-bosqich. ID raqami: 1235488'
        self.assertEqual(talaba1_info,self.talaba1.get_info())

        
unittest.main()