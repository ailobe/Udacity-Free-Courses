import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        '<p><a href="https://en.wikipedia.org/wiki/File:Toy_Story.jpg#/media/File:Toy_Story.jpg"><img src="https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg" alt="The poster features Woody anxiously holding onto Buzz Lightyear as he flies in Andy\'s room. Below them sitting on the bed are Bo Peep, Mr. Potato Head, Troll, Hamm, Slinky, Sarge and Rex. In the lower right center of the image is the film\'s title. The background shows the cloud wallpaper featured in the bedroom."></a><br>By From <a rel="nofollow" class="external text" href="http://www.impawards.com/1995/toy_story_ver1.html">impawards</a>., <a href="https://en.wikipedia.org/w/index.php?curid=26009601">Link</a></p>',
                        "https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     '<p><a href="https://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg#/media/File:Avatar-Teaser-Poster.jpg"><img src="https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg" alt="Avatar-Teaser-Poster.jpg"></a><br>By Source, <a href="//en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg" title="Fair use of copyrighted material in the context of Avatar (2009 film)">Fair use</a>, <a href="https://en.wikipedia.org/w/index.php?curid=23732044">Link</a></p>',
                     "https://youtu.be/5PSNL1qE6VY")

# print(avatar.storyline)
# avatar.show_trailer()
movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.__doc__)
# print(media.Movie.__name__)
# print(media.Movie.__module__)
