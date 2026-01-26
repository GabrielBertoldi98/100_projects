#height = 70
#
#if height > 80:
#    print("Can ride")
#else:
#    print("Can't ride")

#--------------------------------------

#Odd or Even
#number = int(input("Write a number: "))
#
#if number%2==0:
#    print("Even")
#else:
#    print("Odd")

#--------------------------------------

height = 121
age = 18
valor = 0
photos = ""

if height > 120:
    print("Can ride")
elif age >= 12 and age <= 18:
    valor = 7
elif age < 12:
    valor = 5
elif age > 18:
    valor = 12
else:
    print("Can't ride")

if photos == "Yes":
    valor += 3
    print("The total bill is $" + str(valor))

if photos == "No":
    print("The total bill is $" + str(valor))