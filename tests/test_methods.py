import unittest
from unittest import result

from partitionpi import *

class TestMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.p = [1, 1, 1, 2, 2]
        self.p2 = [1, 1, 2, 3, 3]
        self.p3 = [1, 1, 1, 2, 3]

    def test_joint_parents(self):
        exp = [[1, 1, 1, 1, 1, 2]]
        result = joint_parents(self.p)
        self.assertEqual(result, exp)

        exp = [[1, 1, 1, 1, 3, 3], [1, 1, 1, 2, 2, 3]]
        result = joint_parents(self.p2)
        self.assertEqual(result, exp)
    
    def test_muted_parents(self):
        exp = [[1, 1, 1, 1, 2, 2],
                [1, 1, 1, 2, 2, 2],
                [1, 1, 1, 2, 2, 3]]
        result = muted_parents(self.p, max_dn=10)
        self.assertEqual(result, exp)
    
    def test_all_ancestors(self):
        p_4 = [1,2]
        exp = [[1,2], [1,1,2], [1,1,1], [1,1,1,1]]
        result = all_ancestors(p_4, 4)
        self.assertEqual(result, exp)
    
    def test_all_muted(self):
        exp = [[1, 1, 1, 2], [1, 1, 2, 2]]
        result = all_muted(self.p)
        self.assertEqual(result, exp)
    
        p_lin = [1, 1, 1]
        exp = [[1, 1]]
        result = all_muted(p_lin)
        self.assertEqual(result, exp)
    
    def test_all_joint(self):
        exp = [[1, 1, 1, 4], [1, 1, 2, 3], [1, 2, 2, 2]]
        result = all_joint(self.p)
        self.assertEqual(result, exp)
    
    def test_partitional_complex(self):
        p_lin = [1, 1, 2]
        exp = [[1,1,2], [1,1], [1,2], [1,3], [2,2], [1], [2], [3], [4]]
        result = partitional_complex(p_lin)
        self.assertEqual(result, exp)
    
    def test_partitions_of(self):
        exp = [[1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2], [4]]
        result = list(partitions_of(4))
        self.assertEqual(result, exp)
    
    def test_partitions_at_most(self):
        exp = [[1], [1, 1], [2], [1, 1, 1], [1, 2], [3]]
        result = partitions_at_most(3)
        self.assertEqual(result, exp)
    
    def test_common_muted_ancestor(self):
        exp = [1, 1, 1, 2, 2, 3, 3]
        result = common_muted_ancestor(self.p, self.p2)
        self.assertEqual(result, exp)

        exp = [1, 1, 1, 2, 2, 3]
        result = common_muted_ancestor(self.p, self.p3)
        self.assertEqual(result, exp)
    
    def test_common_joint_parents(self):
        p1 = [1, 4]
        p2 = [2, 3]
        exp = [[1, 1, 3], [1, 2, 2]]
        result = common_joint_parents(p1, p2)
        self.assertEqual(result, exp)

        exp = []
        result = common_joint_parents([3], [4])
        self.assertEqual(result, exp)
    
    def test_common_parents(self):
        exp = [[1, 3], [1, 4]]
        result = common_parents([1], [4])
        self.assertEqual(result, exp)
    
    def test_ref_partition(self):
        parts = [[5], [1], [2,3]]
        exp = [[1,1,3], [1,2,2], [1, 1, 1, 2], [1, 1, 1, 1, 1]]
        result = ref_partition(parts)
        self.assertEqual(result, exp)
    

if __name__ == '__main__':
    unittest.main()