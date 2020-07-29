import unittest
from Problem_2 import print_depth, Person

class Test2(unittest.TestCase):
    
    def test_print_depth(self):
        person_a = Person("first_name:","last_name:","father:")
        person_b = Person("first_name:","last_name:",person_a)

        data = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "user": person_b
                }
            }
        }
        result = ['key1 1','key2 1','key3 2','key4 2','key5 3', 
        'user 3', 'first_name 4', 'last_name 4', 'father 4', 'first_name 5',
        'last_name 5', 'father 5']

        self.assertNotEqual(print_depth(data), result)

if __name__ == '__main__':
    unittest.main()