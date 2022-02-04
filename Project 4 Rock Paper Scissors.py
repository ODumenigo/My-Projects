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

Graphic = [rock, paper, scissors]
YC = int(input('Enter 0 for rock, 1 for paper, or 2 for scissors! '))

if YC != 0 and YC != 1 and YC != 2:
    print('Please try again and choose 0 for rock, 1 for paper, or 2 for scissors.')
    quit()

CC = random.randint(0, 2)
GraphicU = Graphic[YC]
GraphicC = Graphic[CC]

if YC == 0:
    if CC == 0:
        print(f"You choose {GraphicU}")
        print(f"The computer chooses {GraphicC}")
        print("It's a tie. 🤨")
    if CC == 1:
        print(f"You choose {GraphicU}")
        print(f"The computer chooses {GraphicC}")
        print("You lost. 😢 ")
    if CC == 2:
        print(f"You choose {GraphicU}")
        print(f"The computer chooses {GraphicC}")
        print("You won! 😄")
elif YC == 1:
    if CC == 0:
        print(f"You choose {GraphicU}")
        print(f"The computer chooses {GraphicC}")
        print("You won! 😄")
    if CC == 1:
        print(f"You choose {GraphicU}")
        print(f"The computer chooses {GraphicC}")
        print("It's a tie. 🤨")
    if CC == 2:
        print(f"You choose {GraphicU}")
        print(f"The computer chooses {GraphicC}")
        print("You lost. 😢 ")
elif YC == 2:
    if CC == 0:
        print(f"You choose {GraphicU}")
        print(f"The computer chooses {GraphicC}")
        print("You lost. 😢 ")
    if CC == 1:
        print(f"You choose {GraphicU}")
        print(f"The computer chooses {GraphicC}")
        print("You won! 😄")
    if CC == 2:
        print(f"You choose {GraphicU}")
        print(f"The computer chooses {GraphicC}")
        print("It's a tie. 🤨")
