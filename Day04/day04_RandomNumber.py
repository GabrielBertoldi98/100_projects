import random

#random int
#random_int = random.randint(1, 10)
#print(random_int)

#this random never will print 1, but can print 0
#random_number_0_to_1 = random.random() * 10
#print(random_number_0_to_1)

#random_float = random.uniform(0, 2)
#print(random_float)

random_number = random.randint(1, 2)

if random_number == 1:
    print("Heads")
else:
    print("Tails")