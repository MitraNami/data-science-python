# fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, ...

from typing import Iterator

def fib(n: int) -> Iterator[int]:
  """ generates the first n fibonacci numbers"""
  i = 0
  a, b = 1, 1
  while i < n:
    yield a
    a, b = b, a + b
    i += 1

fibonacci_generator = fib(5)
for num in fibonacci_generator:
  print(num)