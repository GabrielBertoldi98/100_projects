print("Welcome to Treasure Island\nYour Mission is to find the treasure")

#Direction of the cross road
print("You're at a cross road. Where do you want to go?\n")
direction = input("Type left or right: ")
if direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake")
    swim_wait = input("Type wait to wait for a boat. Type swim to swim across. ")
    
    #Swim or wait
    if swim_wait == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors")
        door_color = input("One red, one yellow and one blue. Witch colour do you choose? ")
        
        #Door color
        if door_color == "red":
            print("Burned by fire. Game Over")
        elif door_color == "blue":
            print("Eaten by beasts. Game Over")
        elif door_color == "yellow":
            print("You Win!")
        else:
            "Game over"
    else:
        print("Attacked by trout. Game Over")
else:
    print("Fall into a hole. Game over")