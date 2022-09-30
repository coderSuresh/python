print("Welcome to Treasure island.\nYour mission is to find the treasure")
choose=input('youre at a cross road. Where do you want to go? Type "left" or "right"')
if choose =="left":
    choose=input('you come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.')
    if choose == "wait":
        choose=input('you arrive at the island unharmed. There is a house with 3 door. one red, one yellow, and one blue. Which colour do you .')
        if choose == "red":
                print("Game over")
        elif choose == "blue":
                print("Game over")
        elif choose == "yellow":
                print("You won!")
        else:
            print("Your choosen door doesnot exist! Game over")
               
    else:
        print("You got attact by cocodile:Game over")
        
else:
    print("You fell in the hole game over.")