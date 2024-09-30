import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2,7),9)
        self.assertEqual(self.calc.add(-3,2),-1)
        self.assertEqual(self.calc.add(-4,2),-2)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(8,3),5)
        self.assertEqual(self.calc.subtract(7,3),4)
        self.assertEqual(self.calc.subtract(13,3),10)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(8,3),24)
        self.assertEqual(self.calc.multiply(18,4),72)
        self.assertEqual(self.calc.multiply(16,3),48)

    def test_division(self):
        self.assertEqual(self.calc.divide(16,4),4)
        self.assertEqual(self.calc.divide(55,5),11)
        self.assertEqual(self.calc.divide(27,9),3)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))

