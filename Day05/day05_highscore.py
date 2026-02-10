student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]

#high_score = 0
#counter = 0
#
#for score in student_scores:
#    if int(student_scores[counter]) > high_score:
#        high_score = int(student_scores[counter])
#    counter += 1
#
#print(f"The high score in the class is {high_score}")

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)
