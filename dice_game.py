<<<<<<< HEAD
import random

def roll_dice():
    roll_dice = random.randint(1,6) + random.randint(1,6);
    return roll_dice

player1 = input("Enter the name of player 1: \n")
player2 = input("Enter the name of player 2: \n")

roll1 = roll_dice()
roll2 = roll_dice()

print(player1,'rolled',roll1)
print(player2,'rolled',roll2)

if roll1 > roll2:
    print(player1,'wins!')
elif roll2 > roll1:
    print(player2,'wins!')
else:
    print('You tie!')
=======
import random

def roll_dice():
    roll_dice = random.randint(1,6) + random.randint(1,6);
    return roll_dice

player1 = input("Enter the name of player 1: \n")
player2 = input("Enter the name of player 2: \n")

roll1 = roll_dice()
roll2 = roll_dice()

print(player1,'rolled',roll1)
print(player2,'rolled',roll2)

if roll1 > roll2:
    print(player1,'wins!')
elif roll2 > roll1:
    print(player2,'wins!')
else:
    print('You tie!')
>>>>>>> 3012899 (First_commit)
