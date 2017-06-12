import unittest
from temp_converter import convert_celcius_to_farenheit

class TempConverterTest(unittest.TestCase):
	 #given temp in celcius = correct value in farenheit
	 #check for null values and throw an error
	 #data type for input
	 # throws an exception when data type is incorrect

	def test_celcius_is_converted_to_farenheit(self):
		"""
		  F= C * 9/5 + 32
		"""
		actual = convert_celcius_to_farenheit(10)
		expected = 50
		self.assertEqual(actual, expected, 'celcius should convert to correct farenheit')
		self.assertEqual(convert_celcius_to_farenheit(20), 68, 'celcius should convert to correct farenheit')


# if __name__ == '__main__':
#     unittest.main()