# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 14:07:13 2024

@author: Nasrullo Nurullayev
"""

import unittest
from name import get_full_name

class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        formatted_name = get_full_name('alijon','valiyev')        
        self.assertEqual(formatted_name, 'Alijon Valiyev')
    def test_toliq_ism_otasi(self):
        name = get_full_name('hasan','husanov','olimovich')
        self.assertEqual(name,'Hasan Olimovich Husanov')

unittest.main()