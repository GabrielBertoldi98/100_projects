capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#nested list in dictionary
travel_log = {
    "France": ["Paris","Lille", "Dijon"],
    "Germany": ["Stuttgart", "Munique"]
}

#print a specifical city in France
#print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

#takin a value in a list inside other list
#print(nested_list[2][1]) #O valor 2 é o terceiro valor da primeira lista


#nedted dictionary with a list and another dictionary
travel_log = {
    "France": {
        "num_time_visited": 8,
        "cities_visited": ["Paris","Lille", "Dijon"],
    },
    "Germany": {
        "num_time_visited": 5,
        "cities_visited" : ["Stuttgart", "Munique"]
    } 
}

print(travel_log["Germany"]["cities_visited"][0])