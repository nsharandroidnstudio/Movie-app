from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class TextVectorizer:
    def __init__(self, data):
        self.data = data.fillna('').astype(str)
        self.vectorizer = TfidfVectorizer()
        self.feature_vectors = None

    
    def convert_data_to_vector(self):
        self.feature_vectors = self.vectorizer.fit_transform(self.data)

    def Get_cosine_similarity_martix(self):
        return cosine_similarity(self.feature_vectors)    
    
   

   


