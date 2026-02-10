import random

symbols = ['!','@','#','$','%','&','*','(',')','+']
numbers = ['0','1','2','3','4','5','6','7','8','9']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','m','z']

r = int(input("How many letters would you like in your password?"))
s = int(input("How many symbols would you like?"))
n = int(input("How many numbers would you like?"))
range_password = r + s + n

random_letter = []
random_symbol = []
random_number = []
random_password = []
password = ""

for r_letters in range(0, r):
    randomizador = random.randint(0,21)
    random_letter += [letters[randomizador]]

for r_symbol in range(0,s):
    randomizador = random.randint(0,9)
    random_symbol += [symbols[randomizador]]

for r_number in range(0,n):
    randomizador = random.randint(0,9)
    random_number += [numbers[randomizador]]

random_password = random_letter + random_number + random_symbol

gera_senha = random.sample(random_password, k=range_password)

for c in gera_senha:
    password += c

print (gera_senha)
print (password)