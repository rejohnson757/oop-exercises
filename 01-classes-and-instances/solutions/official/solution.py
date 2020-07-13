from datetime import date


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

    def info(self):
        return (
            f'Title: {self.title}\n'
            f'Rating: {self.rating}\n'
            f'Release date: {self.release_date.strftime(r"%B %d, %Y")}\n'
            f'Summary: {self.summary}'
        )

    def released_for(self):
        return date.today() - self.release_date
