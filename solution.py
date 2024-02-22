class CheckoutSystem:
    def __init__(self):
        self.prices = {
            "Apple": 0.60,  # 60p
            "Orange": 0.25,  # 25p
            "Banana": 0.20,  # 20p
        }

    def buy_one_get_one_free(self, count, price):
        """Calculates the price for 'buy one, get one free' offer."""
        return (count // 2 + count % 2) * price

    def three_for_two(self, count, price):
        """Calculates the price for '3 for the price of 2' offer."""
        return (2 * (count // 3) + count % 3) * price

    def calculate_total_cost(self, items):
        item_counts = {item: items.count(item) for item in set(items)}
        total_cost = 0

        for item, count in item_counts.items():
            if item == "Apple" or item == "Banana":
                # Apply 'buy one, get one free' offer for both apples and bananas
                total_cost += self.buy_one_get_one_free(count, self.prices[item])
            elif item == "Orange":
                # Apply '3 for the price of 2' offer for oranges
                total_cost += self.three_for_two(count, self.prices[item])
            else:
                total_cost += count * self.prices.get(item, 0)

        # Special handling for bananas bought with apples
        if "Banana" in item_counts and "Apple" in item_counts:
            # Determine the number of free bananas or apples (whichever is cheaper, in this case, bananas)
            free_items = min(item_counts["Banana"], item_counts["Apple"])
            # Deduct the cost of the free bananas
            total_cost -= free_items * self.prices["Banana"]

        return f"£{total_cost:.2f}"
