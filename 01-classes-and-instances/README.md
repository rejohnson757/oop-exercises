# Classes and Instances
This problem will be starting off simple, only dealing with classes and instances.

## Problem
For the problem, you will be writing a `Movie` class. Instances of this class will have attributes such as `title` and `rating`, along with a few methods. There is a stub for your `Movie` class in [problem.py](./problem.py) for you to fill in.

For all examples below, assume an instance of `Movie` is created like this:
```py
>>> endgame = Movie(
...     title='Avengers: Endgame',
...     rating=9.5,
...     summary="The Avengers' final showdown with Thanos."
... )
```

1. Write an `__init__` method that stores the arguments for 3 parameters (`title`, `rating`, and `summary`) as attributes. The attributes should have the same names as the parameters. This will allow usage of an instance of the class like shown below.

```py
>>> endgame.title
'Avengers: Endgame'
>>> endgame.summary
"The Avengers' final showdown with Thanos."
```
