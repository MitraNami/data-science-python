# matrices
from typing import List, Tuple, Callable

Vector = List[float]
Matrix = List[List[float]] # type alias

def shape(A: Matrix) -> Tuple[int, int]:
  """ Returns (# of rows of A, # of columns of A) """
  row_nums = len(A)
  column_nums = len(A[0]) if A else 0
  assert all(len(row) == column_nums for row in A), "all rows must have the same length"
  return (row_nums, column_nums)


assert shape([[1, 2, 3], [4, 5, 6,]]) == (2, 3) # 2 rows, 3 columns
assert shape([]) == (0, 0)


def get_row(A: Matrix, i:int) -> Vector:
  """ Returns the i-th row of A (as a Vector) """
  return A[i]


def get_column(A: Matrix, j:int) -> Vector:
  """ Returns the j-th column of A (as a Vector) """
  return [row[j] for row in A]


def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
  """
  Returns a num_rows x num_cols matrix
  whose (i, j)-th entry is entry_fn(i, j)
  """

  return [
    [entry_fn(i, j) for j in range(num_cols)]
    for i in range(num_rows)   # Create one list for each i
  ]


def identity_matrix(n: int) -> Matrix:
  """ Returns the n x n identity matrix """
  return make_matrix(n, n, lambda i, j : 1 if i == j else 0)


assert identity_matrix(4) == [[1, 0, 0, 0],
                              [0, 1, 0, 0],
                              [0, 0, 1, 0],
                              [0, 0, 0, 1]]


