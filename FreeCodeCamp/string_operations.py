
# string = 'I am here'

# print(string[:5])
# print(string[5:])

# print(type(string))
# print(dir(string)) ## with this we can get all the functions/operations/methods we ca use on the string 

str = 'X-DSPAM-Confidence: 0.8475 '

ipos = str.find(':')
print(ipos)
piece = str[ipos + 1:].strip()
print(piece)
value = float(piece)
print(value)


str = 'bannana' # 7 chars

for n in str:
    print(n)

print(len(str))

