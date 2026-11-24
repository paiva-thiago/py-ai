import random

# 1) Random integer between 1 and 100
number = random.randint(1, 100)
print(f"Random number: {number}")

# 2) Random float between 0.0 and 1.0
decimal = random.random()
print(f"Decimal: {decimal:.4f}")

# 3) Pick a random item from a list
fruits = ["apple", "banana", "orange", "grape"]
picked = random.choice(fruits)
print(f"Picked fruit: {picked}")

# 4) Shuffle a list in place
cards = ["A", "K", "Q", "J", "10"]
random.shuffle(cards)
print(f"Shuffled cards: {cards}")