#def calculate_love_score(name1, name2):
#    name1 = list(name1)
#    name2 = list(name2)
#
##    true_love = list("truelove")
#
#    t=0
#    r=0
#    u=0
#    e=0
#
#    l=0
#    o=0
#    v=0
#    
#
#    for i, letter in enumerate(name1):
#        if name1[i].lower() == "t":
#            t += 1
#        elif name1[i].lower() == "r":
#            r += 1
#        elif name1[i].lower() == "u":
#            u += 1
#        elif name1[i].lower() == "e":
#            e += 1
#
#    for i, letter in enumerate(name2):
#        if name2[i].lower() == "t":
#            t += 1
#        elif name2[i].lower() == "r":
#            r += 1
#        elif name2[i].lower() == "u":
#            u += 1
#        elif name2[i].lower() == "e":
#            e += 1
#
#    total1 = t + r + u + e
#
#    t=0
#    r=0
#    u=0
#    e=0
#
#    l=0
#    o=0
#    v=0
#
#    for i, letter in enumerate(name1):
#        if name1[i].lower() == "l":
#            l += 1
#        elif name1[i].lower() == "o":
#            o += 1
#        elif name1[i].lower() == "v":
#            v += 1
#        elif name1[i].lower() == "e":
#            e += 1
#
#
#    for i, letter in enumerate(name2):
#        if name2[i].lower() == "l":
#            l += 1
#        elif name2[i].lower() == "o":
#            o += 1
#        elif name2[i].lower() == "v":
#            v += 1
#        elif name2[i].lower() == "e":
#            e += 1
#
#    total2 = l + o + v + e
#
#    print(f"Love score = {total1}" + f"{total2}")
#
#calculate_love_score("Kanye West", "Kim Kardashian")

def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    
    score = int(str(first_digit) + str(second_digit))
    print(score)
    
calculate_love_score("Kanye West", "Kim Kardashian")