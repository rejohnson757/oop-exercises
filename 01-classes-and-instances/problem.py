import datetime
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
        return f'Title: {self.title}\nRating: {self.rating}\nRelease date: {self.release_date.strftime(r"%B %d, %Y")}
        \nSummary: {self.summary}'
        
#if __name__ == '__main__':
    
    #details = Movie('Avengers: Endgame', 9.5, datetime.date(2019, 4, 26), "The Avengers\' final showdown with Thanos.")

    #print(details.info())