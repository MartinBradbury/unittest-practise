import unittest
from evens import even_number_of_evens


class TestEvens(unittest.TestCase):
    def test_throws_error_if_value_passed_in_is_not_list(self):
        self.assertRaises(TypeError, even_number_of_evens, 4)

    def test_values_in_list(self):
        self.assertEqual(even_number_of_evens([]), False)#Writing tests here to fail and then pass in function
        self.assertEqual(even_number_of_evens([2, 4]), True)#Writing tests here to fail and then pass in function
        self.assertEqual(even_number_of_evens([2]), False) #Writing tests here to fail and then pass in function
        self.assertEqual(even_number_of_evens([1, 3, 5]), False) #Write a test to see if we pass in a odd number list of odd numbers


if __name__ == "__main__":
    unittest.main()