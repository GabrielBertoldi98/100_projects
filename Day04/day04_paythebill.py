import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#random = random.randint(0, 4)
#print(f"{friends[random]} will pay the bill.") - using a random number to select the index from the list

print(f"{random.choice(friends)} will pay the bill.")