import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint
calculator = Calculator()

class MyTestCase(unittest.TestCase):

    def test_addition_calculator(self):
        test_input = CsvReader('/src/Addition.csv').data
        for row in test_input:
            self.assertEqual(calculator.addition(row['Value 1'], row['Value 2']), int(row['Result']))

    def test_subtract_calculator(self):
        test_input = CsvReader('/src/Subtraction.csv').data
        for row in test_input:
            self.assertEqual(calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))

    def test_multiply_calculator(self):
        test_input = CsvReader('/src/Multiplication.csv').data
        for row in test_input:
            self.assertEqual(calculator.multiply(row['Value 1'], row['Value 2']),int(row['Result']))

    def test_divide_calculator(self):
        test_input = CsvReader('/src/Division.csv').data
        for row in test_input:
            self.assertEqual(calculator.divide(row['Value 1'], row['Value 2']),float(row['Result']))

    def test_square_calculator(self):
        test_input = CsvReader('/src/TestSquare.csv').data
        for row in test_input:
            self.assertEqual(calculator.square(row['Value 1']),int(row['Result']))

    def test_sqroot_calculator(self):
        test_input = CsvReader('/src/SquareRoot.csv').data
        for row in test_input:
            result = round(calculator.sqroot(int(row['Value 1'])), 8)
            self.assertEqual(result, round(float(row['Result']), 8))

    def test_times_calculator(self):
        test_input = CsvReader('/src/Multiplication.csv').data
        for row in test_input:
            self.assertEqual(calculator.times(row['Value 1'], row['Value 2']),int(row['Result']))


if __name__ == '__main__':
    unittest.main()
