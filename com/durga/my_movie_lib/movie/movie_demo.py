class Movie:
    def __init__(self, title, hero, heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine

    def info(self):
        print('Movie title is: ', self.title)
        print('Movie hero is: ', self.hero)
        print('Movie heroine is: ', self.heroine)


if __name__ == '__main__':
    list_of_movies = []
    while True:
        title = input('Enter movie title: ')
        hero = input('Enter movie hero: ')
        heroine = input('Enter movie heroine: ')
        movie = Movie(title, hero, heroine)
        list_of_movies.append(movie)
        print('Movie details added...')
        for movie in list_of_movies:
            movie.info()
        option = input('Do you want to add more movie details [yes/no]: ')
        if option.lower() == 'no':
            print('Thanks for using our application...')
            break
