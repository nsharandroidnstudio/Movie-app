from fuzzywuzzy import fuzz, process

class UserInput:
    @classmethod
    def get_favorite_movie_name(self,movie_names):

            while True:
                user_input = input("Please enter the name of a movie that you already like: ")
                # Use fuzzy string matching to find the closest matching movie name
                closest_match = process.extractOne(user_input, movie_names)

                if closest_match:
                    closest_movie_name, similarity_score = closest_match
                    print(f"Closest matching movie name: {closest_movie_name} (Similarity: {similarity_score}%)")

                    # Ask the user if they are okay with the movie or want to try again
                    response = input(f"Are you okay with '{closest_movie_name}'? (yes/no): ").strip().lower()
            
                    if response == 'yes':
                        return closest_movie_name
                    else :
                        print("Let's try again.")
                else:
                    print("No close match found. Please try again.")
    @classmethod
    def Show_movie_title(self,recomnder_number,movie_title):
            print(f"#{recomnder_number}: {movie_title}")

            


