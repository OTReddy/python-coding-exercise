class CheckoutSystem:
    def __init__(self):
        self.prices = {
            "Apple": 0.60,  # 60p
            "Orange": 0.25  # 25p
        }
        
        self.offers = {
            "Apple": self.buy_one_get_one_free,
            "Orange": self.three_for_two
        }

    def buy_one_get_one_free(self, count):
        return (count // 2 + count % 2) * self.prices["Apple"]

    def three_for_two(self, count):
        return (2 * (count // 3) + count % 3) * self.prices["Orange"]

    def calculate_total_cost(self, items):
        item_counts = {item: items.count(item) for item in set(items)}
        total_cost = 0
        for item, count in item_counts.items():
            if item in self.offers:
                total_cost += self.offers[item](count)
            else:
                total_cost += count * self.prices.get(item, 0)
        return f"£{total_cost:.2f}"

