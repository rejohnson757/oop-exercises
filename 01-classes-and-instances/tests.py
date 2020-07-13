import datetime
import unittest

from problem import Movie


class MovieTests(unittest.TestCase):

    def setUp(self) -> None:
        """Create a new Movie instance before running each test."""
        self.title = 'Black Panther'
        self.rating = 9.0
        self.release_date = datetime.date(2018, 2, 16)
        self.summary = "T'Challa returns home to the African nation of Wakanda to take his rightful place as king."

        self.movie = Movie(
            title=self.title,
            rating=self.rating,
            release_date=self.release_date,
            summary=self.summary
        )

    def test_101_instantiation(self) -> None:
        """The parameters given to __init__ should be assigned to attributes with the same names."""
        for attribute in ('title', 'rating', 'release_date', 'summary'):
            with self.subTest(attribute=attribute):
                self.assertTrue(
                    hasattr(self.movie, attribute),
                    msg=f'The Movie instance has no `{attribute}` attribute.'
                )
                self.assertEqual(getattr(self, attribute), getattr(self.movie, attribute))

    def test_102_info(self) -> None:
        """The `info` method should return the correct information on a movie."""
        self.assertTrue(hasattr(self.movie, 'info'), msg='Movie has no `info` method.')

        expected = (
            'Title: Black Panther\n'
            'Rating: 9.0\n'
            'Release date: February 16, 2018\n'
            "Summary: T'Challa returns home to the African nation of Wakanda to take his rightful place as king."
        )

        self.assertEqual(expected, self.movie.info())

    def test_103_released_for(self) -> None:
        """The `released_for` method should return how many days have passed."""
        self.assertTrue(hasattr(self.movie, 'released_for'), msg='Movie has no `released_for` method.')
        
        expected = datetime.date.today() - self.release_date

        self.assertEqual(expected, self.movie.released_for())
