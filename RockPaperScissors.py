


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

import random

# Your selection
user_selection = int(input("enter your choice: rock - 0, paper - 1, scissors - 2  :   "))
if (user_selection == 0):
    print("You selected Rock")
    print(rock)
elif (user_selection == 1):
    print("You selected Paper")
    print(paper)
elif (user_selection == 2):
    print("You selected Scissors")
    print(scissors)
else:
    print("Invalid entry")

# computer selection
# Rock - 0, Paper - 1, scissors - 2
comp_selection = random.randint(0,2)
if (comp_selection == 0):
    print("Computer selected Rock")
    print(rock)
elif (comp_selection == 1):
    print("Computer selected Paper")
    print(paper)
elif (comp_selection == 2):
    print("Computer selected Scissors")
    print(scissors)
else:
    print("Invalid entry")

# Rock - 0, Paper - 1, scissors - 2
if (user_selection == comp_selection):
    print("Game Tied. Try again")
elif (user_selection == 0) and (comp_selection == 2):
    print("You win")
elif (comp_selection == 0) and (user_selection == 2):
    print("Computer wins")
elif (user_selection == 2) and (comp_selection == 1):
    print("You win")
elif (comp_selection == 2) and (user_selection == 1):
    print("Computer wins")
elif (user_selection == 1) and (comp_selection == 0):
    print("You win")
elif (comp_selection == 1) and (user_selection == 0):
    print("Computer wins")



# // alternate logic
# elif (user_selection == 0) and (comp_selection == 2):
#     print("You win")
# elif (comp_selection == 0) and (user_selection == 2):
#     print("Computer wins")
# elif (user_selection 2 > comp_selection 1):
#     print("You win")
# elif (comp_selection > user_selection):
#     print("Computer wins")



# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.
