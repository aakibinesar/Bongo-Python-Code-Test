import unittest
import Problem_1

class TaskTest(unittest.TestCase):
	def test1(self):
		self.assertEqual(Problem_1.print_depth(Problem_1.D), ('key1', 1))

	def test2(self):
		self.assertEqual(Problem_1.print_depth(Problem_1.C), ('key1', 1))

if __name__ == '__main__':
	unittest.main()
