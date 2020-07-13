# Classes and Instances
This problem will be starting off relatively simple.

## Problem
For the problem, you will be writing a `Movie` class. Instances of this class will have attributes such as `title` and `release_date`, along with a few methods. There is a stub for your `Movie` class in [problem.py](./problem.py) for you to fill in.

For all examples below, assume an instance of `Movie` is created like this:
```py
>>> endgame = Movie(
...     title='Avengers: Endgame',
...     rating=9.5,
...     release_date=datetime.date(2019, 4, 26),
...     summary="The Avengers' final showdown with Thanos."
... )
```

1. Write an `__init__` method that stores the arguments for 3 parameters (`title`, `rating`, `release_date`, and `summary`) as attributes. The attributes should have the same names as the parameters. This will allow usage of an instance of the class like shown below.

    ```py
    >>> endgame.title
    'Avengers: Endgame'
    >>> endgame.release_date
    datetime.date(2019, 4, 26)
    ```

2. Let's create a method for this class. We will call this new method `info`. The `info` method will return information on the movie, including the title, rating, release date, and summary. The output of the info method should exactly match the follow format:

    ```py
    >>> print(endgame.info())
    Title: Avengers: Endgame
    Rating: 9.5
    Release date: April 26, 2019
    Summary: The Avengers' final showdown with Thanos.
    ```

3. We will create one more method for our `Movie` class. It will be called `released_for` and it will return a `datetime.timedelta` object representing how many days have passed since the movie was released (days was calculated when this was written, so it may be different for you).

    ```py
    >>> endgame.released_for()
    datetime.timedelta(days=444)
    ```
