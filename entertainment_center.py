# Entertianment Center

import media
import fresh_tomatoes

# Create instances of the Movie object with my favorited movies

forest_gump = media.Movie("Forest Gump",
                          "2h 22m",
                          "Slow-witted Forrest Gump (Tom Hanks) has never "
                          "thought of himself as disadvantaged, "
                          "and thanks to his supportive mother "
                          "(Sally Field), he leads anything but a "
                          "restricted life. Whether dominating on the "
                          "gridiron as a college football star, "
                          "fighting in Vietnam or captaining a "
                          "shrimp boat, Forrest inspires people with his "
                          "childlike optimism. "
                          "But one person Forrest cares about "
                          "most may be the most difficult to save -- his "
                          "childhood love, the "
                          "sweet but troubled Jenny (Robin Wright).",
                          "https://i.ytimg.com/vi/EtYNngO7eq4/movieposter.jpg",
                          "https://www.youtube.com/watch?v=uPIEn0M8su0")
shooter = media.Movie("Shooter",
                      "2h 6m",
                      "A top Marine sniper, Bob Lee Swagger "
                      "(Mark Wahlberg), leaves the military "
                      "after a mission goes horribly awry and "
                      "disappears without a trace. Swagger is "
                      "coaxed back into service "
                      "after high-profile government officials "
                      "convince him to help thwart "
                      "a plot against the President of the "
                      "United States. Swagger realizes "
                      "he has been betrayed and becomes the "
                      "target of a nationwide manhunt. "
                      "Instead of hiding, he seeks revenge against"
                      "some of the most powerful "
                      "and corrupt leaders in the free world.",
                      "http://fr.web.img4.acsta.net/c_215_290/medias/"
                      "nmedia/18/63/77/83/18750618.jpg",
                      "https://www.youtube.com/watch?v=natRMn81kiY")
rounders = media.Movie("Rounders",
                       "2h 1m",
                       "Mike McDermott (Matt Damon) loses his "
                       "money in a poker game "
                       "against Russian gangster Teddy \"KGB\" "
                       "(John Malkovich). Under "
                       "pressure from his girlfriend, Jo (Gretchen Mol), "
                       "he promises to quit "
                       "gambling. This lasts until his friend, "
                       "Lester \"Worm\" Murphy (Edward Norton), "
                       "gets out of prison and needs to pay off an "
                       "old debt. The pair come close "
                       "to earning the money back but are caught "
                       "cheating. Then Mike finds out the "
                       "debt is owed to Teddy and makes one last-ditch "
                       "effort to beat the Russian.",
                       "https://images-na.ssl-images-amazon.com"
                       "/images/I/41iydX-u5ZL.jpg",
                       "https://www.youtube.com/watch?v=-Qv4K-4-FZM")
usual_suspects = media.Movie("Usual Suspects",
                             "1h 48m", "The greatest trick the devil "
                             "ever pulled was convincing the world "
                             "he didn't exist, says con man Kint "
                             "(Kevin Spacey), drawing a comparison "
                             "to the most enigmatic criminal of all time, "
                             "Keyser Soze. Kint attempts "
                             "to convince the feds that the mythic crime "
                             "lord not only exists, but is "
                             "also responsible for drawing Kint and his "
                             "four partners into a multi-million "
                             "dollar heist that ended with an explosion "
                             "in San Pedro Harbor - "
                             "leaving few survivors.",
                             "https://images-na.ssl-images-amazon.com"
                             "/images/I/51ANy73yJuL._SY300_.jpg",
                             "https://www.youtube.com/watch?v=oiXdPolca5w")
gladiator = media.Movie("Gladiator",
                        "2h 51m",
                        "Commodus (Joaquin Phoenix) takes power "
                        "and strips rank from Maximus "
                        "(Russell Crowe), one of the favored generals "
                        "of his predecessor and "
                        "father, Emperor Marcus Aurelius, the great "
                        "stoical philosopher. Maximus "
                        "is then relegated to fighting to the death in the "
                        "gladiator arenas.",
                        "https://images-na.ssl-images-amazon.com/images"
                        "/I/41ISIQ06CbL.jpg",
                        "https://www.youtube.com/watch?v=owK1qxDselE")


# Create an array, moviesArray that will contain every instance of the Movie
# object created above
# Pass the moviesArray to the open_movies_page method

moviesArray = [forest_gump, shooter, rounders, usual_suspects, gladiator]

fresh_tomatoes.open_movies_page(moviesArray)
