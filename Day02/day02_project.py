#tip calculator
#1 - Ask the full valor of the bill
#2 - Ask how much tip you like to give (porcentage) (10, 12 or 15)
#3 - Ask how much people will split the bill

print ("Welcome to the tip calculator!")
total_bill = float(input("How was the total bill? $"))
tip_porcentage = int(input("How much tip would you like to give? 10, 12, or 15 %"))
peoples = int(input("How many people to split the bill? "))

total = float(((total_bill * (tip_porcentage/100)) + total_bill) / peoples)

print("Each person should pay: $" + str(round(total, 2)))