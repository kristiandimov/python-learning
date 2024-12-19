total = 0
expenses = []
num_expenses = int(input("Enter # of expenses: "))

for i in range(num_expenses):
    expenses.append(float(input("Enter expense: ")))


total = sum(expenses)
# sum = 0

# for x in expenses:
#     sum = sum + x

print('You spent $', total, sep = '')
