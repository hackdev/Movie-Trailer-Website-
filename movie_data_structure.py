import webbrowser


# This module defines data structure for storing movie details
# and a method for playing movie trailer
class Movie():
    """ This class provides a way to store movie related information
        and a method for viewing movie trailer
    """
    
    def __init__(self, title, storyline, poster, trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
