# vectors
from typing import List

Vector = List[float] # a type alias, saying a Vecor is a list of floats

def add(v: Vector, w: Vector) -> Vector:
  """ Adds corresponding elements"""
  assert len(v) == len(w), "Vectors must be the same length"
  return [v_el + w_el for (v_el, w_el) in zip(v, w)]

# try:
#   add([1, 2, 3], [4, 5])
# except AssertionError as inst:
#   print(inst) # inst is an obj with method __str__ that return "Vectors ..."
#               # inst.__str__() is called when printing inst


def subtract(v: Vector, w: Vector) -> Vector:
  """ Subtracts corresponding elements """
  assert len(v) == len(w), "Vectors must have the same length"
  return [v_i - w_i for (v_i, w_i) in zip(v, w)]

assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]


def vector_sum(vectors: List[Vector]) -> Vector:
  """ Sums all corresponding elements """
  # Check that vectors is not empty
  assert vectors, "no vectors provided!"

  # Check the vectors are all the same size
  num_elements = len(vectors[0])
  assert all(len(vector) == num_elements for vector in vectors), "Vectors must be the same length"
  
  return [sum(element) for element in zip(*vectors)]


assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


def scalar_multiply(c: float, v: Vector) -> Vector:
  """ Multiplies every element by c """
  return [c * v_i for v_i in v]


assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


def vector_mean(vectors: List[Vector]) -> Vector:
  """ Computes the element-wise average """
  sum_vector = vector_sum(vectors)
  n = len(vectors)
  return scalar_multiply(1/n, sum_vector)


assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]


def dot(v: Vector, w: Vector) -> float:
  """ Computes v_1 * w_1 + ... + v_n * w_n """
  assert len(v) == len(w), "Vectors must have same length"
  return sum(v_i * w_i for (v_i, w_i) in zip(v, w))

assert dot([1, 2, 3], [4, 5, 6]) == 32


def sum_of_squares(v: Vector) -> float:
  """ Computes v_1 * v_1 + ... + v_n * v_n """
  return dot(v, v)

assert sum_of_squares([1, 2, 3]) == 14


import math
def magnitude(v: Vector) -> float:
  """ Computes the magnitude/length of v """
  return math.sqrt(sum_of_squares(v))

assert magnitude([3, 4]) == 5


def squared_distance(v: Vector, w: Vector) -> float:
  distance_vector = subtract(v, w)
  return magnitude(distance_vector)