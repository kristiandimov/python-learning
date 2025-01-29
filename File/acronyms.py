<<<<<<< HEAD

def find_acronym():
    look_up = input("What software acronym would like to look up?\n")

    found = False
    try:
        with open('File/acronyms.txt') as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print("File not found")
        return
    
    if not found:
        print("The acronym doesnt exist")

def add_acronym():
    acronym = input('What acronym you want to add?\n')
    definition = input('What is the definition?\n')

    with open('File/acronyms.txt','a') as file:
        file.write(acronym + ' - ' + definition + '\n')

def main():
    choice = input('Do you want to find(F) or add(A) an acronym')
    if(choice == 'F'):
        find_acronym
    elif choice == 'A':
        add_acronym()

=======

def find_acronym():
    look_up = input("What software acronym would like to look up?\n")

    found = False
    try:
        with open('File/acronyms.txt') as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print("File not found")
        return
    
    if not found:
        print("The acronym doesnt exist")

def add_acronym():
    acronym = input('What acronym you want to add?\n')
    definition = input('What is the definition?\n')

    with open('File/acronyms.txt','a') as file:
        file.write(acronym + ' - ' + definition + '\n')

def main():
    choice = input('Do you want to find(F) or add(A) an acronym')
    if(choice == 'F'):
        find_acronym
    elif choice == 'A':
        add_acronym()

>>>>>>> 3012899 (First_commit)
main()