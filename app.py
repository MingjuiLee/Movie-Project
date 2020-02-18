"""
- Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:

- Add movies
- See movies
- Find a movie
- Stop running the program

Tasks:
[x]: Where to store movies
[]: What is the format of a movie
[]: Show the user the main interface and get their input
[]: Allow users to add movies
[]: Show all their movies
[]: Find a movie
[]: Stop running the program when they type 'q'
"""

movies = []


def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies()
        elif user_input == 'f':
            find_movie()
        else:
            print("Unknown command-please try again.")

        user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")


def add_movie():
    name = input('Enter the movie name: ')
    director = input('Enter the movie director: ')
    year = int(input('Enter the movie release year: '))

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })


menu()

print(movies)
