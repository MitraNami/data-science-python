# Type annotations
def add(a: int, b: int) -> int:
  return a + b


assert add(1, 2) == 3
assert add([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]


# Reasons to use type annotations
# 1-documentation
# 2- cleaner functions and interfaces
# 3- helps the editor with autocomplete

from typing import List
vector = List[float]
def add(xs: vector) -> float:
  return sum(xs)


assert add([1, 2, 3]) == 6


from typing import Dict, Iterable, Tuple, Callable

# keys are strings, values are ints
counts: Dict[str, int] = {'data': 1, 'science': 2}

# lists and generators are both iterable
evens: Iterable[int] = (x for x in range(10) if x % 2 == 0)
odds : Iterable[int] = [1, 3, 5]

# tuples specify a type for each element
triple: Tuple[int, float, int] = (10, 2.3, 5)

# callable represents function type
# the type hint says that repeater is a function that takes two arguments
# a string and an int, and returns a string

def twice(repeater: Callable[[str, int], str], s: str) -> str:
  return repeater(s, 2)


def comma_repeater(s: str, n: int) -> str:
  n_copies = [s for _ in range(n)]
  return ', '.join(n_copies)

assert twice(comma_repeater, 'type hints') == 'type hints, type hints'


# type annotations are just Python object, we can assign them to variables
# to make them easier to refer to

Number = int
Numbers = List[Number]

def toral(xs: Numbers) -> Number:
  return sum(xs)