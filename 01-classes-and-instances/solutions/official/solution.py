class Movie:
    """Represents a movie.

    Args:
        name (str): The name of the movie
        rating (float): The rating of the movie
        summary (str): A short summary of the movie
    """

    def __init__(self, title, rating, length, summary):
        self.title = title
        self.rating = rating
        self.summary = summary
