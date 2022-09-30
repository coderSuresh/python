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
choose_number=int(input("Whatk do you choose? Type 0 for Rock, 1 for Scissors or 2 for paper."))

#Generate Random numbers
game_rock_scissors_paper = [rock,scissors,paper]
game_last_index=len(game_rock_scissors_paper)
generate_automatic= random.randint(0,game_last_index-1)
# Rock  
if(choose_number==0):
    if(game_rock_scissors_paper[choose_number]!=game_rock_scissors_paper[generate_automatic]):
        print(game_rock_scissors_paper[choose_number])
        print("you had choosed Rock")
        generate_automatic_inrange=random.randint(1,game_last_index-1)
        if(game_rock_scissors_paper[generate_automatic_inrange]==game_rock_scissors_paper[1]):
            print(game_rock_scissors_paper[1])
            print("Opponent choosed Scissors")
            print("winner is Rock ")   
        else:
            print(game_rock_scissors_paper[2])
            print("Opponent choosed paper")
            print("winner is paper")
    else:
        print("Draw")
# Scissors
elif choose_number==1:
    if(game_rock_scissors_paper[choose_number]!=game_rock_scissors_paper[generate_automatic]):
        print(game_rock_scissors_paper[choose_number])
        print("you had choosed Scissor")
        generate_automatic_inrange=random.randrange(0,2,1)
        if(game_rock_scissors_paper[generate_automatic_inrange]==game_rock_scissors_paper[0]):
                print(game_rock_scissors_paper[0])
                print("Opponent choosed Rock")
                print("winner is Rock ")   
        else:   
                print(game_rock_scissors_paper[2])
                print("Opponent choosed paper")
                print("winner is scissor")
    else:
        print(game_rock_scissors_paper[1])
        print ("Draw")
# Paper
elif choose_number==2:
       
    if(game_rock_scissors_paper[choose_number]!=game_rock_scissors_paper[generate_automatic]):
        print(game_rock_scissors_paper[choose_number])
        print("you had choosed Paper")
        generate_automatic_inrange=random.randint(0,1)
        if(game_rock_scissors_paper[generate_automatic_inrange]==game_rock_scissors_paper[0]):
            print(game_rock_scissors_paper[0])
            print("Opponent choosed Rock")
            print("winner is paper ")   
        else:   
            print(game_rock_scissors_paper[1])
            print("Opponent choosed Scissor")
            print("winner is scissor")
    else:
        print(game_rock_scissors_paper[2])
        print ("Draw")

else:
    print("--Wawrning----invalid number !please enter correct input!")