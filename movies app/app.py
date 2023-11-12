# Import the DatasetLoader class
from DataLayer.dataloader import DatasetLoader
from Matcher.MoviesMatcher import MoviesMatcher
from UiHandler.UserInput import UserInput
from fuzzywuzzy import fuzz


if __name__ == "__main__":
    # Create an instance of the DatasetLoader class
    selected_features = ['genres', 'popularity', 'vote_average', 'director', 'cast']
    loader = DatasetLoader('movies.csv',selected_features)  # Replace with your CSV file path
    # Load the dataset
    loader.load_dataset()
    # Get the loaded dataset
    movies_dataset = loader.get_dataset()
    # Example: View the first few rows of the dataset
    if movies_dataset is not None:
        combine_features = loader.load_and_combine_features_data()
        favorite_movie_title = UserInput.get_favorite_movie_name(movies_dataset["title"].tolist())
        movie_matcher = MoviesMatcher(movies_dataset,combine_features,favorite_movie_title)
        movie_matcher.Get_similar_movies_to_favorite_movie()     

    