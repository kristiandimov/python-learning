acronym = input('What acronym you want to add?\n')
definition = input('What is the definition?\n')

with open('File/acronyms.txt','a') as file:
    file.write(acronym + ' - ' + definition + '\n')