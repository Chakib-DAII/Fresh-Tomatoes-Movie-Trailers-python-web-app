import media
import webbrowser
import fresh_tomatoes

celebrities_vid = media.Movie("11 celebrities who have aged beatifully",
                  "11 celebrities who have aged beatifully",
                  "https://web.facebook.com/deliriumcha/photos/a.1323914067721481.1073741826.1323911264388428/1323914091054812/"
                  ,"https://www.youtube.com/watch?v=SAs2FG-YEg0")

wars_vid = media.Movie("5 wars has destroyed life",
                  "5 wars has destroyed life",
                  "https://plus.google.com/u/1/photos/114085331065889781008/albums/profile/6450971498780441698?iso=false",
                  "https://www.youtube.com/watch?v=wpvYML5WeQY")

targ_teaser_vid = media.Movie("targ teaser",
                  "targ teaser",
                  "https://plus.google.com/u/1/photos/114085331065889781008/albums/profile/6450971498780441698?iso=false",
                  "https://www.youtube.com/watch?v=CBcl4pJ5l8g")

targ_vibes_vid = media.Movie("Targ vibes",
                  "Targ vibes",
                  "https://plus.google.com/u/1/photos/114085331065889781008/albums/profile/6450971498780441698?iso=false",
                  "https://www.youtube.com/watch?v=LcEGku-Jgow")

#print(celebrities_vid.title +"\n"
#      +celebrities_vid.story_line +"\n"
#      +celebrities_vid.poster_image_url +"\n"
#      +celebrities_vid.youtube_url +"\n")
#webbrowser.open(celebrities_vid.youtube_url)
#webbrowser.open(celebrities_vid.poster_image_url)
#celebrities_vid.show_movie_youtube()
movies = [celebrities_vid, wars_vid, targ_teaser_vid, targ_vibes_vid]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
