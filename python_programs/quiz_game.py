""" 
A Simple Mini Quiz Project with basic questions. 

Step1: Take User input for the given question and compare the input with the answer
Step2: If both strings are matched then question is answered correctly, else it is wrong.

At the end show the score and also the percentage(%).
"""
print("Welcome to my computer quiz!")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()

print("okay! Let's play:)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Your answer is wrong")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Your answer is wrong")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Your answer is wrong")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Your answer is wrong")

print("you got " + str(score) + " questions correct!")
print("you got " + str((score/4)*100) + "%.")
