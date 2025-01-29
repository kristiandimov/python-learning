<<<<<<< HEAD
acronym = input('What acronym you want to add?\n')
definition = input('What is the definition?\n')

with open('File/acronyms.txt','a') as file:
=======
acronym = input('What acronym you want to add?\n')
definition = input('What is the definition?\n')

with open('File/acronyms.txt','a') as file:
>>>>>>> 3012899 (First_commit)
    file.write(acronym + ' - ' + definition + '\n')