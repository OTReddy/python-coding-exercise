class CheckoutSystem:
    def __init__(self):
        self.prices = {
            "Apple": 0.60,  # 60p
            "Orange": 0.25  # 25p
        }

    def calculate_total_cost(self, items):
        item_counts = {item: items.count(item) for item in set(items)}
        total_cost = 0
        for item, count in item_counts.items():
            total_cost += count * self.prices.get(item, 0)
        return f"£{total_cost:.2f}"

