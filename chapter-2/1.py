word_counts = {}
document = ['hi', 'bye', 'hi', 'hi', 'hello']

# first approach
# for word in document:
#   if word in word_counts:
#     word_counts[word] += 1
#   else:
#     word_counts[word] = 1

# second approach
# for word in document:
#   try:
#     word_counts[word] += 1
#   except KeyError:
#     word_counts[word] = 1

# third approach
# for word in document:
#   word_counts[word] = word_counts.get(word, 0) + 1

# fourth approach
# from collections import defaultdict
# word_counts = defaultdict(int)
# for word in document:
#   word_counts[word] += 1

# fifth approach
from collections import Counter
word_counts = Counter(document)


# Sort the list by absolute value from largest to smallest
x = sorted([-4,1,-2,3], key=abs, reverse=True)   # [-4, 3, -2, 1]

# Sort the words and counts from highest count to lowest
sorted_word_counts = sorted(word_counts.items(), key=lambda x : x[1], reverse=True)

# List Comprehensions
even_numbers = [x for x in range(5) if x % 2 == 0]
squares = [x * x for x in range(5)]
even_squares = [x * x for x in range(5) if x % 2 == 0]
square_dict = {x: x*x for x in range(5)}
square_set = {x*x for x in [-1, 1]}
zeros = [0 for _ in even_numbers]
pairs = [(x, y)
          for x in range(10)
          for y in range(10)
]
increasing_pairs = [(x, y)
                    for x in range(10)
                    for y in range(x + 1, 10)
]


# Assert things about inputs for functions
def smallest_item(xs):
  assert xs, "empty list has no smallest item"
  return min(xs)
 