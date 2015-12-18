import webbrowser


class Video():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class Movie(Video):
    """This class provdes a way to store movie-related information"""
    VALID_RATINGS = ["G", "PG", "PG13", "R"]
    def __init__(self, thtle, duration, movie_storyline, poster_image, trailer_youtube):
        self.title = duration
        self.duration = duration
         self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

        
    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class TvShows(Video):
    def __init__(self, title, duration,


                 
