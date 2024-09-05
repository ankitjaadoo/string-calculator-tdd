# test_string_calculator.py
import unittest
from string_calculator import add

class TestStringCalculator(unittest.TestCase):
    
    def test_multiply_single_number(self):
        self.assertEqual(add("2", '*'),2)
        
    def test_multiply_multiple_numbers(self):
        self.assertEqual(add("2,2", '*'),4)

    def test_add_empty_string(self):
        self.assertEqual(add("", '+'), 0)
    
    def test_add_single_number(self):
        self.assertEqual(add("1", '+'), 1)
    
    def test_add_two_numbers(self):
        self.assertEqual(add("1,2", '+'), 3)
    
    def test_add_two_numbers_random_parameter(self):
        self.assertEqual(add("1,2", '$'), 3)
    
    def test_newlines_between_numbers(self):
        self.assertEqual(add("1\n2,3", '+'), 6)
    
    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2", '+'), 3)
        self.assertEqual(add("//|\n1|2|3", '+'), 6)
    
    def test_add_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            add("1,-2,3,-4", '+')
        self.assertEqual(str(context.exception), "negative numbers not allowed: -2,-4")
    
    def test_multiply_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            add("1,-2,3,-4", '*')
        self.assertEqual(str(context.exception), "negative numbers not allowed: -2,-4")

if __name__ == '__main__':
    unittest.main()