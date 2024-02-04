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
def computer():
  randomChoosenInt = random.randint(0, 2)
  if randomChoosenInt == 0:
    print(rock)
    if user_input == 0:
      print("Computer choose rock ,Its a draw")
    elif user_input == 1:
      print("Computer choose rock ,You win")
    else:
      print("Computer choose rock ,You loose")
  elif randomChoosenInt == 1:
    print(paper)
    if user_input == 1:
      print("Computer choose paper ,Its a draw")
    elif user_input == 0:
      print("Computer choose paper ,You loose.")
    else:
      print("Computer choose paper ,You win")
  else:
    print(scissors)
    if user_input == 2:
      print("Computer choose scissor ,Its a draw")
    elif user_input == 0:
      print("Computer choose scissor ,You win")
    else:
      print("Computer choose scissor ,You loose")


user_input = int(
    input('''What do you choose? Type 0 for Rock,
            1 for Paper or 2 for Scissors.'''))
if user_input == 0:
  print(rock)
  computer()
elif user_input == 1:
  print(paper)
  computer()
elif user_input == 2:
  print(scissors)
  computer()
elif user_input >= 3 or user_input < 0:
  print("Invalid input You loose!")
