name = input("Type your name:")
print("Welcome to the adventure! ", name)

answer = input(
    "you're on a dirt road, it has come to an end. You can go left or right. Which way would you like to go?").lower()

if answer == "left":
    answer = input("you come to river, you can walk around it or swim across?")

    if answer == "swim":
        print("you swam across and were eaten by alligator.")
    elif answer == "walk":
        print("you walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input(
        "you come to bridge, it look wobbly, do you want to cross it or head back(cross/back)?").lower()

    if answer == "back":
        print("you go back and lose.")
    elif answer == "cross":
        answer = input(
            "you cross the bridge and meet stranger. Do you talk them(yes/no)?")
        if answer == "yes":
            print("you talk to stranger and they give gold.you win!")
        elif answer == "no":
            print("you ignore the stranger and they are offended and you lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thank you for trying ", name)
