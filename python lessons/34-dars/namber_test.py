# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 09:45:39 2024

@author: Nasrullo Nurullayev
"""

import unittest
from namber import give_number

class bigNamberTest(unittest.TestCase):
    def test_true(self):
        self.assertAlmostEqual(give_number(7,8,6),8)
        self.assertAlmostEqual(give_number(9,5,3), 9)
        self.assertAlmostEqual(give_number(10,11,12), 12)
        
unittest.main()