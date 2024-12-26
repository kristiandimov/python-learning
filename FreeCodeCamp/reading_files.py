fhabd = open('acronyms.txt')
count = 0

for line in fhabd:
    count = count + 1
    line = line.rstrip()
    if line.startswith('IDE'):
        print(line)

print('Line Count: ',count)


fhabd2 = open('acronyms.txt')
inp = fhabd2.read()
print(len(inp))
print(inp[:20])
