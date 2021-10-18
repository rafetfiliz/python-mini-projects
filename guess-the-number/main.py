import random


def guess_function(computer_number, lives_of_user):
    remaining_lives = lives_of_user
    for life in range(lives_of_user):
        user_number = int(input("Make a guess: "))
        if user_number > computer_number:
            remaining_lives -= 1
            print("Too high.")
            if remaining_lives != 0:
                print("Guess again.")
                print(f"You have {remaining_lives} attempts to guess the number.")
            else:
                print("You've run out of guesses, you lose.")
                break
        elif computer_number > user_number:
            remaining_lives -= 1
            print("Too low.")
            if remaining_lives != 0:
                print("Guess again.")
                print(f"You have {remaining_lives} attempts to guess the number.")
            else:
                print("You've run out of guesses, you lose.")
                break
        else:
            print(f"You got it! The answer was {computer_number}.")
            break


logo = """
                              __                            __               
 |\ |     ._ _  |_   _  ._   /__      _   _  _ o ._   _    /__  _. ._ _   _  
 | \| |_| | | | |_) (/_ |    \_| |_| (/_ _> _> | | | (_|   \_| (_| | | | (/_ 
                                                      _|                     
"""

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

num = random.randint(1, 100)

lives = 0
if difficulty == "easy":
    lives = 10
    print("You have 10 attempts remaining to guess the number.")
elif difficulty == "hard":
    lives = 5
    print("You have 5 attempts remaining to guess the number.")

game = guess_function(num, lives)
