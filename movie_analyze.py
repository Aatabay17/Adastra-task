import pandas as pd
import logging

class MovieDatasetAnalyzer:

    def __init__(self, movies_csv_file, ratings_csv_file):
        self.movies_csv_file = movies_csv_file
        self.ratings_csv_file = ratings_csv_file
        self.movie_data = None
        self.ratings_data = None
    
    def load_dataset(self):
        try:
            self.movie_data = pd.read_csv(self.movies_csv_file)
            self.ratings_data = pd.read_csv(self.ratings_csv_file)
            logging.info('Dataset is loaded')
        except FileNotFoundError:
            logging.error('Dataset is not founded')

    def print_number_of_movies(self):
        if self.movie_data is not None:
            print(f"Number of movies: {self.movie_data.id.unique().size}")
        else:
            print("Dataset is empty")

    def print_average_rating_of_movies(self):
        if self.ratings_data is not None:
            print(f"Average rating of all movies: {self.ratings_data['rating'].mean()}")
        else:
            print("Dataset is empty")
    
    def print_top_n_highest_rated_movies(self, n):
        if self.ratings_data is not None:
            print(self.ratings_data.nlargest(n, 'rating'))
        else:
            print("Dataset is empty")
    
    def print_number_of_movies_released_each_year(self):
        if self.ratings_data is not None:
            self.ratings_data['datetime'] = pd.to_datetime(self.ratings_data['timestamp'], unit='s')
            self.ratings_data['year'] = self.ratings_data['datetime'].dt.year
            print(self.ratings_data['year'].value_counts())
        else:
            print("Dataset is empty")
    
    def save_to_json(self, output_file):
        if self.movie_data is not None:
            self.movie_data.to_json(output_file, orient="records")
            logging.info('Dataset saved as JSON file')
        else:
            logging.error('Dataset is not founded')
        

if __name__ == '__main__':
    logging.basicConfig(filename="movie_dataset_analyzer.log", level=logging.INFO)

    movie_dataset_analyzer = MovieDatasetAnalyzer('movies_metadata.csv', 'ratings.csv')

    movie_dataset_analyzer.load_dataset()

    movie_dataset_analyzer.print_number_of_movies()

    movie_dataset_analyzer.print_average_rating_of_movies()

    movie_dataset_analyzer.print_top_n_highest_rated_movies(5)

    movie_dataset_analyzer.print_number_of_movies_released_each_year()

    movie_dataset_analyzer.save_to_json('movies_metadata.json')
