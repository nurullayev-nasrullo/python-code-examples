# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 14:42:49 2024

@author: Nasrullo Nurullayev
"""

import unittest
from fibonnaci import fibonacci

class FibonnaciTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(fibonacci(2))
    
    def test_false(self):
        self.assertFalse(fibonacci(4))
        
unittest.main()