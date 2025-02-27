class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price, quantity):
        if item not in self.items:
            self.items[item] = {'quantity': quantity, 'price': price}
        else:
            self.items[item]['quantity'] += quantity
            self.items[item]['price'] = price

    def remove_item(self, item):
        if item in self.items:
            if self.items[item]['quantity'] > 1:
                self.items[item]['quantity'] -= 1
            else:
                del self.items[item]
        else:
            print(f"{item} is not in the cart.")

    def calculate_total_price(self):
        total = 0
        for item in self.items:
            total += self.items[item]['price'] * self.items[item]['quantity']
        return total


cart = ShoppingCart()
cart.add_item("apple", 0.99, 2)
cart.add_item("banana", 0.50, 3)
cart.add_item("apple", 0.99, 1)  # Adding one more apple
cart.remove_item("banana")  # Removing one banana
cart.remove_item("banana")  # Removing another banana
cart.remove_item("banana")  # Removing the last banana
cart.remove_item("orange")  # Trying to remove an item not in the cart

print("Total price:", cart.calculate_total_price())
print("Cart items:", cart.items)