from ArithmeticCalculator import calculate
import unittest

#pip install -r requirements.txt
#pip install pytest
#python -m pytest

class test_calculator(unittest.TestCase):

    def test_calculator(self):
        self.assertEqual(calculate({"num1":2, "opt" : "+", "num2": 3}), 6.0)


if __name__ == '__main__':
    unittest.main()