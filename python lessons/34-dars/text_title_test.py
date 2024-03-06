# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 11:10:28 2024

@author: Nasrullo Nurullayev
"""

import unittest
from text_title import titleText

class TextTitle(unittest.TestCase):
    def test_title(self):
        a = ['monday','thusday','friday']
        b = ['Monday','Thusday','Friday']
        self.assertEqual(titleText(a), b)
        
unittest.main()