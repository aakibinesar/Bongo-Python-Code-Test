import unittest
import Problem_3

class TestLca(unittest.TestCase):
    
    #unit test for node 6 and 7
    def test_node6_7(self):
        self.assertEqual(Problem_3.LCA(Problem_3.root, 6, 7).key, 3)
    
    #unit test for node 3 and 7
    def test_node3_7(self):
        self.assertEqual(Problem_3.LCA(Problem_3.root, 3, 7).key, 3)
    
    #unit test for node 1 and 5
    def test_node6_5(self):
        self.assertEqual(Problem_3.LCA(Problem_3.root, 6, 5).key, 1)
    
    #unit test for same nodes
    def test_node_same(self):
        self.assertEqual(Problem_3.LCA(Problem_3.root, 2, 2).key, 2)
    
    #unit test for node 2 and 3
    def test_node2_3(self):
        self.assertEqual(Problem_3.LCA(Problem_3.root, 2, 3).key, 1)
    
    #unit test for node 8 and 9
    def test_node8_9(self):
        self.assertEqual(Problem_3.LCA(Problem_3.root, 8, 9).key, 4)
    
    #unit test for non existing nodes
    def test_node_none(self):
        self.assertEqual(Problem_3.LCA(Problem_3.root, 10, 10), None)
    
    #unit test for no root
    def test_node_no_root(self):
        self.assertEqual(Problem_3.LCA(None, 4, 5), None)

if __name__ == '__main__':
    unittest.main()