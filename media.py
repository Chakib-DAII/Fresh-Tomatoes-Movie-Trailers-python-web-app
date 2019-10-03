import webbrowser
class Movie() :
    """this class provides a way to store movie related informations"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self,movie_title,movie_story_line,poster_image,movie_youtube_url):
        self.title = movie_title
        self.story_line = movie_story_line
        self.poster_image_url = poster_image
        self.youtube_url = movie_youtube_url

    def show_movie_youtube(self):
        webbrowser.open(self.youtube_url)

    def show_title(self):
        print(self.title)
        
    def show_title(self):
        print(self.story_line)
        
    def show_title(self):
        webbrowser.open(self.poster_image_url)
        
        
