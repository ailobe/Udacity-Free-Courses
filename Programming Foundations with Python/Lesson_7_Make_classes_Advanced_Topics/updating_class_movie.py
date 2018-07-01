import webbrowser


class Video():
    """Store common video related information"""

    # Initializes the variables
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Movie(Video):
    """Store the movie related information"""
    # Class Variable shared by all instances
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # Initializes the variables
    def __init__(self, title, duration, storyline, poster_image, trailer_youtube):
        # Inherits from parent class Video
        Video.__init__(self, title, duration)
        # child class Movie variables
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class TvShow(Video):
    """Store the tv show related information"""

    def __init__(self, title, duration, seasons, episodes, tv_station):
        # Inherits from parent class Video
        Video.__init__(self, title, duration)
        # child class TvShow variables
        self.seasons = seasons
        self.episodes = episodes
        self.tv_station = tv_station


# Instance creation (normally on a separate folder)
toy_story = Movie("Toy Story",
                  "1h 21m",
                  "A story of a boy and his toys that come to life",
                  '<p><a href="https://en.wikipedia.org/wiki/File:Toy_Story.jpg#/media/File:Toy_Story.jpg"><img src="https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg" alt="The poster features Woody anxiously holding onto Buzz Lightyear as he flies in Andy\'s room. Below them sitting on the bed are Bo Peep, Mr. Potato Head, Troll, Hamm, Slinky, Sarge and Rex. In the lower right center of the image is the film\'s title. The background shows the cloud wallpaper featured in the bedroom."></a><br>By From <a rel="nofollow" class="external text" href="http://www.impawards.com/1995/toy_story_ver1.html">impawards</a>., <a href="https://en.wikipedia.org/w/index.php?curid=26009601">Link</a></p>',
                  'https://youtu.be/KYz2wyBy3kc')

breaking_bad = TvShow("Breaking Bad",
                      "approximately 48 minutes per episode",
                      "5 seasons",
                      "62 episodes",
                      "AMC")
print(toy_story.title)
print(toy_story.duration)
print(toy_story.storyline)
print(breaking_bad.title)
print(breaking_bad.duration)
print(breaking_bad.seasons)
print(breaking_bad.episodes)
print(breaking_bad.tv_station)
