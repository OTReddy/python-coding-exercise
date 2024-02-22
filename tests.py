import unittest
from solution import CheckoutSystem

class TestCheckoutSystem(unittest.TestCase):
    def setUp(self):
        self.checkout = CheckoutSystem()

    def test_empty_cart(self):
        self.assertEqual(self.checkout.calculate_total_cost([]), "£0.00")

    def test_only_apples(self):
        self.assertEqual(self.checkout.calculate_total_cost(["Apple", "Apple"]), "£1.20")

    def test_only_oranges(self):
        self.assertEqual(self.checkout.calculate_total_cost(["Orange", "Orange", "Orange"]), "£0.75")

    def test_apples_and_oranges(self):
        self.assertEqual(self.checkout.calculate_total_cost(["Apple", "Apple", "Orange", "Apple"]), "£2.05")

# Running the tests
unittest.main(argv=[''], exit=False)
