import random

emojis = {'r': 'rock','p':'paper','s':'scissors'}
choices = ('r','p','s')

while True:
    user_choice = input('Rock, paper, scissors? (r/p/s): ').lower()

    if user_choice not in choices:
        print('Invalid choice!')
        continue

    computer_choice = random.choice(choices)

    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print('Tie!')
    elif (
        (user_choice == 'r' and computer_choice == 's') or 
        (user_choice == 's' and computer_choice == 'p') or 
        (user_choice == 'p' and computer_choice == 'r')):

        print('You win!')
    else:
        print('You lose')

    should_continue = input('Continue? (y/n): ').lower()

    if should_continue == 'n':
        break





## My version
# print('Welcome to rock paper scissors game!')
# print('If you want to quit the game type "exit"!')

# while True:

#     person_choice = input('Rock, paper, scissors? (r/p/s): ').lower()
#     computer_choice = random.choice(['paper','rock','scissors'])

#     if person_choice == 'r':
#         print('You chose Rock')
#         print('Computer chose ',computer_choice)

#         if computer_choice == 'scissors':
#             print('You win')
#         elif computer_choice == 'paper':
#             print('You lose')
#         else: 
#             print('Its a tie')
#     elif person_choice == 'p':
#         if computer_choice == 'scissors':
#             print('You lose')
#         elif computer_choice == 'rock':
#             print('You win')
#         else:
#             print('Its a tie')
#     elif person_choice == 's':
#         if computer_choice == 'paper':
#             print('You win')
#         elif computer_choice == 'rock':
#             print('You lose')
#         else:
#             print('Its a tie')
#     elif person_choice == 'exit':
#         break
#     else:
#         print('Invalid choice!')
    

