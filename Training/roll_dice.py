<<<<<<< HEAD
import random

# Optional Enhancements
# Modify the program so the user can specify how many dice they want to roll.
# Add a feature that keeps track of how many times the user has rolled the dice
# during the session. This will require a counter that increments each time the
# dice are rolled.

while True:
    answer = input("Do you want to roll a dice (y/n): ").lower()

    if answer == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'({die1},{die2})')
    elif answer == 'n':
        print("Thanks for playing")
        break
    else:
        print("Ivalid command please")
=======
import random

# Optional Enhancements
# Modify the program so the user can specify how many dice they want to roll.
# Add a feature that keeps track of how many times the user has rolled the dice
# during the session. This will require a counter that increments each time the
# dice are rolled.

while True:
    answer = input("Do you want to roll a dice (y/n): ").lower()

    if answer == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'({die1},{die2})')
    elif answer == 'n':
        print("Thanks for playing")
        break
    else:
        print("Ivalid command please")
>>>>>>> 3012899 (First_commit)
