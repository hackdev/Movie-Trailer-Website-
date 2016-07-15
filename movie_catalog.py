import fresh_tomatoes
import movie_data_structure


# This module defines Movie instances and creates a list of movies, then calls
# open_movies_page function to generate an HTML file to display the catalog
toy_story = movie_data_structure.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = movie_data_structure.Movie("Avatar",
                        "A marine on an alien planet.",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=uZNHIU3uHT4")

kill_bill = movie_data_structure.Movie("Kill Bill: Volume 1",
                        "A former assassin wakes from a coma and sets off on her quest for revenge.",
                        "https://upload.wikimedia.org/wikipedia/en/c/cf/Kill_bill_vol_one_ver.jpg",
                        "https://www.youtube.com/watch?v=ot6C1ZKyiME")

amelie = movie_data_structure.Movie("Amelie",
                        "A young woman who discretely orchestrates the lives of the people around her, creating a world exclusively of her own making.",
                        "https://upload.wikimedia.org/wikipedia/en/5/53/Amelie_poster.jpg",
                        "https://www.youtube.com/watch?v=sECzJY07oK4")

youve_got_mail = movie_data_structure.Movie("You've Got Mail",
                        "Two business rivals who hate each other in the office fall in love over the Internet.",
                        "https://upload.wikimedia.org/wikipedia/en/e/ee/You%27ve_Got_Mail.jpg",
                        "https://www.youtube.com/watch?v=GSeeFgsqUxU")

bourne_identity = movie_data_structure.Movie("The Bourne Identity",
                        "A man is picked up by a fishing boat, bullet-riddled and suffering from amnesia, before racing to elude assassins and regain his memory.",
                        "https://upload.wikimedia.org/wikipedia/en/a/ae/BourneIdentityfilm.jpg",
                        "https://www.youtube.com/watch?v=cD-uQreIwEk")

# list of movies
movies = [toy_story, avatar, kill_bill, amelie, youve_got_mail, bourne_identity]

# generate HTML page
fresh_tomatoes.open_movies_page(movies)
