#perguntar o nome e o valor da aposta
#perguntar se tem outro lance yes/no
#se sim, entrar no loop, senão finalizar o programa e mostrar o nome e o valor do lance mais alto
#obs: a tela tem que ser limpa após cada loop

import os

bits = {}

answer = ""
high_name = ""
high_value = 0

while True: 
    name = input("What is your name?: ")
    value = int(input("What's your bid?: $"))
    bits[name] = value

    for key in bits:
        if bits[key] > high_value:
            high_value = bits[key]
            high_name = name

    exit = input("Are there any other bidders? Type 'yes' or 'no'".lower())
    os.system("cls")
    if exit == "no":
        break

print(f"The winner is {high_name} with a bid of {high_value}")