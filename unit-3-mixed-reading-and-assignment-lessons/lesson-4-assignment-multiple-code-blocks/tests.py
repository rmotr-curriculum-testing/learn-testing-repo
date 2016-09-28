import unittest


class CalculatorTestCase(unittest.TestCase):
    def test_calculator_with_one_operation(self):
        calc = Calculator(
            operations={
                'add': AddOperation
            }
        )
        res = calc.calculate(1, 5, 13, 2, 'add')
        self.assertEqual(res, 21)

    def test_calculator_with_multiple_operations(self):
        calc = Calculator(
            operations={
                'add': AddOperation,
                'subtract': SubtractOperation
            }
        )
        res = calc.calculate(1, 5, 13, 2, 'add')
        self.assertEqual(res, 21)
        res = calc.calculate(13, 3, 7, 'subtract')
        self.assertEqual(res, 3)

    def test_calculator_invoked_with_an_invalid_operation(self):
        calc = Calculator(
            operations={
                'add': AddOperation
            }
        )
        with self.assertRaises(OperationInvalidException):
            res = calc.calculate(1, 5, 13, 2, 'INVALID')
