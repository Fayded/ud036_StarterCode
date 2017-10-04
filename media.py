import webbrowser
import video

# Movie Class
# Extends the Video class with poster_image_url &
# trailer_youtube_url arguments


class Movie(video.Video):
    def __init__(self, title, duration, storyline,
                 poster_image, trailer_youtube):
        video.Video.__init__(self, title, duration, storyline)
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Creates a method of the object that will open a browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
