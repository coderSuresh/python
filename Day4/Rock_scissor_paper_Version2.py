import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
#Generate Random numbers
game_images =[rock , paper, scissors]
user_choice = int(input("What do you choose? Type O for Rock. 1 for paper, 2 for Scissors"))
print(game_images[user_choice])
computer_choice = random. randint(0, 2)
print(f"Computer chose{computer_choice}")
if user_choice >=3 or user_choice < 0:
    print("You typed an invalid number, you lose!" )
elif user_choice==0 and computer_choice==2:
    print("You win!" )
elif computer_choice==2 and user_choice==0: 
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("you win")
elif computer_choice == user_choice:
    print("It is Draw")
    
    