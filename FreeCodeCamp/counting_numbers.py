<<<<<<< HEAD
count = 0
total  = 0

while True:
    input_value = input("Enter a number: ")

    if input_value.lower() == 'done':
        break

    try:
        fval = float(input_value)

    except ValueError:
        print('Invalid input')
        continue
    
    count += 1
    total += fval

print(f'Total: {total} | Count: {count} | Average: {total / count}')




# # This is a solution but its overeginneer keep it simple 
# #count = 0
# #total = 0
# #average = 0
# # entered_numbers = []

# # while True :
    
# #     try:
# #         input_number = input('Enter a number: ')
        
# #         if input_number.lower() == 'done':
# #             print(f'Total: {sum(entered_numbers)} | Count: {len(entered_numbers)} | Average: {sum(entered_numbers) / len(entered_numbers)}')
# #             break

# #         entered_numbers.append(float(input_number))

# #     except ValueError:
# #         print('Not a valid number')
# #         continue
=======
count = 0
total  = 0

while True:
    input_value = input("Enter a number: ")

    if input_value.lower() == 'done':
        break

    try:
        fval = float(input_value)

    except ValueError:
        print('Invalid input')
        continue
    
    count += 1
    total += fval

print(f'Total: {total} | Count: {count} | Average: {total / count}')




# # This is a solution but its overeginneer keep it simple 
# #count = 0
# #total = 0
# #average = 0
# # entered_numbers = []

# # while True :
    
# #     try:
# #         input_number = input('Enter a number: ')
        
# #         if input_number.lower() == 'done':
# #             print(f'Total: {sum(entered_numbers)} | Count: {len(entered_numbers)} | Average: {sum(entered_numbers) / len(entered_numbers)}')
# #             break

# #         entered_numbers.append(float(input_number))

# #     except ValueError:
# #         print('Not a valid number')
# #         continue
>>>>>>> 3012899 (First_commit)
