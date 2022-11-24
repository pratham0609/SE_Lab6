
import unittest

from Prog1 import add

class TestSum(unittest.TestCase):
	def test_1(self):
		a_1 = 1
		b_1 = 1
		result = add(a_1, b_1)
		self.assertEqual(result, 2)
		
	def test_2(self):
		a_2 = 10
		b_2 = 5
		result = add(a_2, b_2)
		self.assertEqual(result, 15)

	def test_3(self):
		a_3 = 5
		b_3 = 5
		result = add(a_3, b_3)
		self.assertEqual(result, 10)

	def test_4(self):
		a_4 = 2
		b_4 = 5
		result = add(a_4, b_4)
		self.assertEqual(result, 12) 

	def test_5(self):
		a_5 = 5
		b_5 = 4
		result = add(a_5, b_5)
		self.assertEqual(result, 20)

if __name__ == '__main__':
	unittest.main()
