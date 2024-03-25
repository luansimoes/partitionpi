import unittest
from unittest import result

from partitionpi import *

class TestOperators(unittest.TestCase):
    def setUp(self) -> None:
        self.p = [1, 1, 1, 2, 2]
        self.p2 = [1, 1, 2, 3, 3]
        self.p3 = [1, 1, 1, 2, 3]
    
    def test_concat(self):
        exp = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3]
        result = concat(self.p, self.p2)
        self.assertEqual(result, exp)

        exp = [1, 1, 1, 1, 1, 1, 2, 2, 2, 3]
        result = concat(self.p, self.p3)
        self.assertEqual(result, exp)
    
    def test_diff(self):
        exp = [1, 2]
        result = diff(self.p, self.p2)
        self.assertEqual(result, exp)

        exp = [3, 3]
        result = diff(self.p2, self.p)
        self.assertEqual(result, exp)
    
    def test_intersection(self):
        exp = [1, 1, 2]
        result = intersection(self.p, self.p2)
        self.assertEqual(result, exp)

        result = intersection(self.p2, self.p)
        self.assertEqual(result, exp)

        exp = [1, 1, 1, 2]
        result = intersection(self.p, self.p3)
        self.assertEqual(result, exp)
    
    def test_union(self):
        exp = [1, 1, 1, 2, 2, 3, 3]
        result = union(self.p, self.p2)
        self.assertEqual(result, exp)

        exp = [1, 1, 1, 2, 2, 3]
        result = union(self.p, self.p3)
        self.assertEqual(result, exp)

    def test_mute(self):
        p_lin = [1, 1, 1, 2]
        result = mute(self.p, 2)
        self.assertEqual(result, p_lin)

        p_lin = [1, 1, 1]
        result = mute(result, 2)
        self.assertEqual(result, p_lin)
    
    def test_join(self):
        p_lin = [1, 2, 2, 2]
        result = join(self.p, 1, 1)
        self.assertEqual(result, p_lin)

        p_lin = [1, 1, 2, 3]
        result = join(self.p, 1, 2)
        self.assertEqual(result, p_lin)

        p_lin = [1, 1, 1, 4]
        result = join(self.p, 2, 2)
        self.assertEqual(result, p_lin)

    def test_graph(self):
        draw_complex([1,1,1,1])


if __name__ == '__main__':
    unittest.main()