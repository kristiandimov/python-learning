age = int(input("How old are you? \n"))

decates = age // 10 #this is // whole number devision it returns on 25 2 only not 2.5
years = age % 10

print("You are " + str(decates) + " 25decates and " +
      str(years) + " years old")