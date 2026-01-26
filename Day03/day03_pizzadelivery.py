print ("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want cheese? Y or N: ")
total_bill = 0

if size == "S":
    total_bill = 15
elif size == "M":
    total_bill = 20
elif size == "L":
    total_bill = 25

if size == "S" and pepperoni == "Y":
    total_bill += 2
elif size == "M" and pepperoni == "Y" or size == "L" and pepperoni == "Y" :
    total_bill += 3

if extra_cheese == "Y":
    total_bill += 1

print(f"Your final bill is: ${total_bill}")