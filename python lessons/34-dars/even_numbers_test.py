# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 11:31:35 2024

@author: Nasrullo Nururllayev
"""

import unittest
from even_numbers import give_numbers

class EvenNumberTest(unittest.TestCase):
    def test_even(self):
        a = [1,2,3,4,5,6,7,8,9,10]
        b = [2,4,6,8,10]
        self.assertEqual(give_numbers(a), b)
        
unittest.main()