import random
from supermarket_logic.item import Item


class Customer:
    _id_counter = 1

    def __init__(self):
        self.id = Customer._id_counter
        Customer._id_counter += 1
        self.cart = self.generate_cart()

    def generate_cart(self):
        cart_size = random.randint(1, 5)
        items = [
            Item(f"Item{random.randint(1, 100)}",
                 round(random.uniform(1, 20), 2))
            for _ in range(cart_size)
        ]
        return items

    def checkout_total(self):
        return sum(item.price for item in self.cart)

    def __repr__(self):
        return (
            f"Customer {self.id} with {len(self.cart)} items, "
            f"Total: ${self.checkout_total():.2f}"
        )
