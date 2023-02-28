import unittest

# PYTEST will be MOST VALUABLE 
# pytest can be run from the folder and it autmatically finds and executes the tests

class TestValues(unittest.TestCase):
	# in a different scenario setUps are useful so you dont have to re-delcare the same object
	def setUp(self) -> None:
		print("setUp")
		return super().setUp()

	def tearDown(self) -> None:
		print("tearDown")
		return super().tearDown()

	def test_int_float(self) -> None:
		print("test_int_float")
		self.assertEqual(1, 1.0)

	def test_int_string(self) -> None:
		print("test_int_string")
		self.assertNotEqual(1, "1")

	def test_int_bool(self) -> None:
		print("test_int_bool")
		self.assertEqual(1, True)

# You must have a main for calling the test with python...
# python test_setup_teardown.py
# ...to work properly.
# Caling main will go through each test with a report

if __name__ == "__main__":
	unittest.main(verbosity=2)
