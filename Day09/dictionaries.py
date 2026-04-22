#creating a dictionarie

colours = {
    "apple": "red",
    "pear": "green",
    "banana": "yellow"
}

#print(colours["pear"])

colours["orange"] = "orange"

#adding a data in our dictionary
colours["orange"]
print(colours)

#creating a new dictionary from zero
empty_dictionary = {}

#editing an item in a dictionary
colours["apple"] = "white"

#loop through a dictionary
for key in colours:
    print(colours[key])

#reseting the datas of a dictionary
colours = {}


