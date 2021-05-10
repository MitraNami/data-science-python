# we want to iterate over a list or a generator and we need both the values and indices
names = ['Alice', 'Bob', 'Charlie', 'Debbie']

# # not Pythonic
# for i in range(len(names)):
#   print(f'name {i} is {names[i]}')

# # also not Pythonic
# i = 0
# for name in names:
#   print(f'name {i} is {name}')
#   i += 1

# # Pythonic
# for (i, name) in enumerate(names):
#   print(f'name {i} is {name}')

# en_names = enumerate(names, 10)
# print(dir(en_names))
# print(list(en_names))

# Randomness
import random
# random.seed(10) # this ensures we get the same results every time

four_uniforms_randoms = [random.random() for _ in range(4)]
print(four_uniforms_randoms)

print(random.randrange(2, 6))

up_to_ten = list(range(1, 11))
random.shuffle(up_to_ten)
print(up_to_ten)

my_best_friends = random.choices(["Alice", "Bob", "Charlie"], k=2)
print(my_best_friends)

four_with_replacement = random.choices(range(10), k=4)
print(four_with_replacement)


# regular expressions

import re

re_examples = [
  3 == len(re.split('[ab]', 'carbs')), # split on a or b to ['c', 'r', 's']
  'R-D-' == re.sub('[0-9]', '-', 'R2D2'), # replace digits with dashes
  not re.match('a', 'cat'), # cat doesn't start with a
  re.search('a', 'cat'), # cat has an a in it
  not re.search('c', 'dog'), # dog doesn't have a c in it
]

assert all(re_examples), 'all regular examples should be True'