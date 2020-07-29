import unittest
import Problem_2

class TaskTest(unittest.TestCase):
	def test1(self):
		self.assertEqual(Problem_2.print_depth(Problem_2.D),('key1',1))

if __name__ == '__main__':
	unittest.main()
