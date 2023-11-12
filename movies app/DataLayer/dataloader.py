import pandas as pd

class DatasetLoader:
    def __init__(self, file_path,selected_features):
        self.file_path = file_path
        self.dataset = None
        self.selected_features = selected_features
        self.features_dataset = None

    def load_dataset(self):
        try:
            self.dataset = pd.read_csv(self.file_path)
            print(f"Dataset loaded from {self.file_path}")
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def get_dataset(self):
        return self.dataset
    
    def get_features_data(self):
        if self.dataset is not None:
            # Create a new dataset with only the selected features
            self.features_dataset = self.dataset[self.selected_features]
            return self.preprocess_dataset()
             


    def preprocess_dataset(self):
            if self.features_dataset is not None:
                for feature in self.selected_features:
                    self.features_dataset[feature].fillna('')
                return self.features_dataset

        
    def combine_features_dataset(self , features_data ):

        if features_data is not None:
            
            #Convert numeric columns to strings before concatenation
            combined_features = (
            features_data['genres'] + ' ' +
            features_data['popularity'].astype(str) + ' ' +
            features_data['vote_average'].astype(str) + ' ' +
            features_data['director'] + ' ' +
            features_data['cast'].astype(str)
            )
            return combined_features

    def load_and_combine_features_data(self):
                    features_dataset = self.get_features_data()
                    return  self.combine_features_dataset(features_dataset)
                 

                   