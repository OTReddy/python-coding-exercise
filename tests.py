import unittest
from solution import CheckoutSystem

class TestCheckoutSystem(unittest.TestCase):
    def setUp(self):
        self.checkout = CheckoutSystem()

    def test_empty_cart(self):
        self.assertEqual(self.checkout.calculate_total_cost([]), "£0.00")

    def test_only_apples(self):
        self.assertEqual(self.checkout.calculate_total_cost(["Apple"]), "£0.60")

    def test_only_oranges(self):
        self.assertEqual(self.checkout.calculate_total_cost(["Orange", "Orange"]), "£0.50")

    def test_apples_and_oranges(self):
        self.assertEqual(self.checkout.calculate_total_cost(["Apple", "Orange"]), "£0.85")

    def test_apple_offer(self):
        self.assertEqual(self.checkout.calculate_total_cost(["Apple", "Apple", "Apple"]), "£1.20")

    def test_orange_offer(self):
        self.assertEqual(self.checkout.calculate_total_cost(["Orange", "Orange", "Orange", "Orange"]), "£0.75")

    def test_mixed_fruits_with_offers(self):
        items = ["Apple", "Apple", "Apple", "Orange", "Orange", "Orange", "Orange"]
        self.assertEqual(self.checkout.calculate_total_cost(items), "£1.95")

# Running the tests
unittest.main(argv=[''], exit=False)
