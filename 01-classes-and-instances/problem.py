class Movie:
    """Represents a movie.

    Args:
        name (str): The name of the movie
        rating (float): The rating of the movie
        release_date (datetime.date): The date the movie was released
        summary (str): A short summary of the movie
    """

    def __init__(self, title, rating, release_date, summary):
        self.title = title
        self.rating = rating
        self.release_date = release_date
        self.summary = summary
