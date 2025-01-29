<<<<<<< HEAD
current_movies = {
    'The Grinch':'11:00am',
    'Rudolph':'1:00pm'
}

print("We are showing the following movies: \n")
for key in current_movies:
    print(key)

movie =  input('What movie would you like the showtime for? \n')

showtime = current_movies.get(movie)

if showtime == None:
    print('Requested movie not found')
else:
=======
current_movies = {
    'The Grinch':'11:00am',
    'Rudolph':'1:00pm'
}

print("We are showing the following movies: \n")
for key in current_movies:
    print(key)

movie =  input('What movie would you like the showtime for? \n')

showtime = current_movies.get(movie)

if showtime == None:
    print('Requested movie not found')
else:
>>>>>>> 3012899 (First_commit)
    print("Here is you movies showtime: ",showtime)