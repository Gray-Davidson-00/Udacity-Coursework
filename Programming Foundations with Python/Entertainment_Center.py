import fresh_tomatoes
import media


toy_story = media.Movie("Toy Story",
                        "A story of Living Toys",
                        "http://static.comicvine.com/uploads/original/12/126071/2427179-2427161-toyjun11.jpeg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc" )

avatar = media.Movie("Avatar",
                     "Dances with wolves in space",
                     "https://sleephotography.files.wordpress.com/2013/05/avatar_poster_21.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


hero = media.Movie("Hero1",
                     "Nested stories told in color and martial arts.",
                     "http://www.topchinesemovies.com/wp-content/uploads/2012/04/Hero-Movie-Poster-One.jpg",
                     "https://www.youtube.com/watch?v=srFhXDZhUZI")



toy_story_1 = media.Movie("Toy Story1",
                        "A story of Living Toys",
                        "http://static.comicvine.com/uploads/original/12/126071/2427179-2427161-toyjun11.jpeg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc" )

avatar_1 = media.Movie("Avatar1",
                     "Dances with wolves in space",
                     "https://sleephotography.files.wordpress.com/2013/05/avatar_poster_21.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


hero_1 = media.Movie("Hero1",
                     "Nested stories told in color and martial arts.",
                     "http://www.topchinesemovies.com/wp-content/uploads/2012/04/Hero-Movie-Poster-One.jpg",
                     "https://www.youtube.com/watch?v=srFhXDZhUZI")


#print (toy_story.storyline)
#print (avatar.title)


#avatar.show_trailer()
#hero.show_trailer()
movies = [toy_story, avatar, hero, toy_story_1, avatar_1, hero_1]

#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)

print(media.Movie.__name__)
print(media.Movie.__module__)

