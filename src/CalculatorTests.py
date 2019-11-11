import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_data = CsvReader('/src/Addition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.addition(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtraction(self):
        test_data = CsvReader('/src/Subtraction.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtraction(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiplication(self):
        test_data = CsvReader('/src/Multiplication.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_division(self):
        test_data = CsvReader('/src/Division.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.division(row['Value 1'], row['Value 2']), result)
            self.assertAlmostEqual(self.calculator.result, result)

    def test_squaring(self):
        test_data = CsvReader('/src/TestSquare.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square_(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_squareroot(self):
        test_data = CsvReader('/src/SquareRoot.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.sqrt_(row['Value 1']), result)
            self.assertAlmostEqual(self.calculator.result, result)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

if __name__== '__main__':
    unittest.main()
