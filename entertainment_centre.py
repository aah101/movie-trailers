import fresh_tomatoes
import media_doc

china_town = media_doc.Movie("Chinatown",
                       "A private eye investigates corruption among LA's wealthy",
                       "https://images-na.ssl-images-amazon.com/images/I/515RWbgdsdL.jpg",
                       "https://www.youtube.com/watch?v=3aifeXlnoqY")

#print(china_town.storyline)


br_2049 = media_doc.Movie("Blade Runner 2049",
                       "A replicant sent to retire an earlier model finds a buried box that will change mankind",
                       "https://vignette.wikia.nocookie.net/bladerunner/images/f/f2/Blade_Runner_2049_Poster.jpg/revision/latest?cb=20171003044201",
                       "https://www.youtube.com/watch?v=gCcx85zbxz4")

in_the_mood = media_doc.Movie("In the Mood for Love",
                       "A journalist in 1950s Hong Kong begins a secret friendhsip with the wife of his own wife's lover",
                       "http://i.ebayimg.com/00/s/NTAwWDM0Mg==/z/FcMAAOxyVLNS-qb9/$_3.JPG?set_id=2",
                       "https://www.youtube.com/watch?v=iixUc63lfGc")

eternal_sunshine = media_doc.Movie("Eternal Sunshine of the Spotless Mind",
                       "How do you erase the heartbreak of a relationship gone wrong?",
                       "https://ih0.redbubble.net/image.15450819.9699/poster%2C210x230%2Cf8f8f8-pad%2C210x230%2Cf8f8f8.lite-1u2.jpg",
                       "https://www.youtube.com/watch?v=yE-f1alkq9I")

tootsie = media_doc.Movie("Tootsie",
                       "An out of work actor finds the only way he can get work is dressing as a woman",
                       "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfgVVI82HF73lGhNNaVOJAVRBA1S2HZKtr7ryngwq_-_rggPEm1w",
                       "https://www.youtube.com/watch?v=NgZI5VZvAy8")

third_man = media_doc.Movie("The Third Man",
                       "A private eye investigates corruption among LA's wealthy",
                       "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6enDOLByqb1ZTWS2vwIQeVUpzJ8CXXPxLJ1eog3Sr5gbhO7Vz",
                       "https://www.youtube.com/watch?v=F-QWLAndD1E")

movies = [china_town, br_2049, in_the_mood, eternal_sunshine, tootsie, third_man]
print(media_doc.Movie.valid_ratings)
#fresh_tomatoes.open_movies_page(movies)


#print(BladeRunner_2049.storyline)
#BR_2049.show_trailer()
#china_town.show_trailer()

