
from DataLayer.TextVectorizer import TextVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Enums.enums import Movie_enums
from UiHandler.UserInput import UserInput
 
class MoviesMatcher:
    def __init__(self, movies_data,combine_features,favorite_movie):
        self.movies_data = movies_data
        self.combine_features = combine_features
        self.favorite_movie = favorite_movie
        self.text_vectorizer  = TextVectorizer(combine_features)
        self.text_vectorizer.convert_data_to_vector()
        self.cosine_similarity_matrix_by_selected_features = self.text_vectorizer.Get_cosine_similarity_martix()

    def get_vectores_cosine_similarity_with_favorite_move(self,favorite_movie_index):
            return self.cosine_similarity_matrix_by_selected_features[favorite_movie_index]

    
    def Get_similar_movies_to_favorite_movie(self):
        favorite_movie_index = self.get_movies_index_by_title(self.favorite_movie)
        movie_matrix_similarity = self.get_vectores_cosine_similarity_with_favorite_move(favorite_movie_index)
        similar_movies = sorted(enumerate(movie_matrix_similarity), key=lambda x: x[1], reverse=True)[:10]
        return self.get_top_10_similar_movies(similar_movies)

    def get_movies_index_by_title(self,movie_title):
        movie_index = self.movies_data[self.movies_data['title'] == movie_title]['index'].values[0]
        return movie_index
    
    def get_movies_title_by_index(self,movie_index):
        movie_title = self.movies_data[self.movies_data['index'] == movie_index].title.values[0]
        return movie_title

    def get_top_10_similar_movies(self, similar_movies):
           for i, movie_index in enumerate(similar_movies, start=1):
            UserInput.Show_movie_title(i,self.get_movies_title_by_index(movie_index[0]))

             