import unittest
from unittest import result

from partitionpi import *

class TestBase(unittest.TestCase):
    def setUp(self) -> None:
        self.p = [1, 1, 1, 2, 2]
        self.p2 = [1, 1, 2, 3, 3]
        self.p3 = [1, 1, 1, 2, 3]

    def test_dn(self):
        exp = 7
        result = dn(self.p)
        self.assertEqual(result, exp)
    
    def test_n_parts(self):
        exp = 5
        result = n_parts(self.p)
        self.assertEqual(result, exp)
    
    def test_distinct(self):
        exp = [1, 2]
        result = distinct(self.p)
        self.assertEqual(result, exp)
    
    def test_repeated(self):
        exp = [1, 3]
        result = repeated(self.p2)
        self.assertEqual(result, exp)
    
    def test_single(self):
        exp = [2]
        result = single(self.p2)
        self.assertEqual(result, exp)
    
    def test_total_comb(self):
        exp = 21
        result = total_comb(self.p)
        self.assertEqual(result, exp)
    
    def test_agg(self):
        exp = 2
        result = agg(self.p)
        self.assertEqual(result, exp)
    
    def test_disp(self):
        exp = 19
        result = disp(self.p)
        self.assertEqual(result, exp)
    
    def test_n_muted(self):
        exp = 2
        result = n_muted(self.p)
        self.assertEqual(result, exp)
    
    def test_n_joint(self):
        exp = 3
        result = n_joint(self.p)
        self.assertEqual(result, exp)

        exp = 5
        result = n_joint(self.p2)
        self.assertEqual(result, exp)

        exp = 4
        result = n_joint(self.p3)
        self.assertEqual(result, exp)
    
    def test_exponential_form(self):
        exp = [(1, 3), (2, 2)]
        result = exponential_form(self.p)
        self.assertEqual(result, exp)

        exp = [(1, 2), (2, 1), (3, 2)]
        result = exponential_form(self.p2)
        self.assertEqual(result, exp)
    
    def test_map_form(self):
        exp = {1:3, 2:2}
        result = map_form(self.p)
        self.assertEqual(result, exp)

        exp = {1:2, 2:1, 3:2}
        result = map_form(self.p2)
        self.assertEqual(result, exp)

    def test_as_str(self):
        exp = '1.1.1.2.2'
        result = as_str(self.p)
        self.assertEqual(result, exp)
    
    def test_as_tex_str(self):
        exp = r"$1^{3}2^{2}$"
        result = as_tex_str(self.p)
        self.assertEqual(result, exp)

        exp = r"$1^{2}2^{1}3^{2}$"
        result = as_tex_str(self.p2)
        self.assertEqual(result, exp)

        exp = r"$1^{3}2^{1}3^{1}$"
        result = as_tex_str(self.p3)
        self.assertEqual(result, exp)
    

if __name__ == '__main__':
    unittest.main()