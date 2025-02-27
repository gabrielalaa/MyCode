import random

cards = ["Heart A", "Heart 1", "Heart 2", "Heart 3", "Heart 4", "Heart 5", "Heart 6", "Heart 7", "Heart 8"]

for i in range(10):
    rand_index = random.randint(0, len(cards) - 1)
    obj = cards.pop(rand_index)
    cards.append(obj)

print(cards)