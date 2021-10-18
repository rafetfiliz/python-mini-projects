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

list = [rock,paper,scissors]

computer = random.choice(list)
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice > 2 or choice < 0:
  print("You typed invalid number, you lose.")
else:
  user = list[choice]

  print(user)
  print("Computer chose:")
  print(computer)



  if (user == rock and computer == scissors) or (user == paper and computer == rock) or (user == scissors and computer == paper):
    print("You win")
  elif (user == computer):
    print("Draw")
  else:
    print("You lose")