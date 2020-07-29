import unittest
from Problem_1 import print_depth

class Test1(unittest.TestCase):
    
    def test_print_depth(self):
        a = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4
                }
            }
        }
        result = ['key1 1','key2 1','key3 2','key4 2','key5 3']

        self.assertEqual(print_depth(a), result)

if __name__ == '__main__':
    unittest.main()
