numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]

#########################################################

mixed = [0, 'Hello', '', False, 42, None]
truthy_elements = filter(None, mixed)
print(list(truthy_elements))  # Output: ['Hello', 42]

#########################################################


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


products = [Product('Apple', 1.0), Product('Banana', 0.5), Product('Cherry', 1.5)]
expensive_products = filter(lambda p: p.price > 1.0, products)
print([p.name for p in expensive_products])  # Output: ['Apple', 'Cherry']
