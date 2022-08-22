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

game_on = True
while game_on:

    question = input('What do you choose? Type "0" for Rock, "1" for Paper or "2" for Scissors ')
    possibilities = [rock, paper, scissors]
    answer = int(question)

    if answer >= 3 or answer < 0:

        print("You trolled. Game over.")

    else:
        print(f"Your choice: \n{possibilities[answer]}")

        pc_answer = random.randint(0, 2)
        print(f"Computer chose: \n {possibilities[pc_answer]}")

        if answer == pc_answer:
            print("Draw.")

        elif answer == 0 and pc_answer == 1:
            print("You lose.")

        elif answer == 0 and pc_answer == 2:
            print("You win!")

        elif answer == 1 and pc_answer == 0:
            print("You win!")

        elif answer == 1 and pc_answer == 2:
            print("You lose.")

        elif answer == 2 and pc_answer == 0:
            print("You lose.")

        elif answer == 2 and pc_answer == 1:
            print("You win!")

    game = input("\nWant to play a new game? Type 'y/n': ").lower()

    if game == "y":
        game_on 

    elif game == 'n':
        game_on = False
        print("\nGoodbye!")
        
    else:
        game_on = False
        print("\nTyping error. Exit program.")
