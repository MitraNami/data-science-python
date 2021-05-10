list1 = ['a', 'b', 'c']
list2 = range(1, 6)

zipped = zip(list1, list2)
# print(dir(zipped)) # has __iter__and __next__
# print(zipped) # a zip object
# to see what the zip object is, put it in a for loop or list func or next func
# print(next(zipped)) # ('a', 1)
zipped_list = [pair for pair in zipped] # or list(zipped)
# print(zipped_list) #[('b', 2), ('c', 3)]


# To unzip a list
pairs = [('a', 1), ('b', 2), ('c', 3)]
# we want to get x = ['a', 'b', 'c'] and y = [1, 2, 3]

x, y = zip(*pairs) # x = ('a', 'b', 'c') y = (1, 2, 3)


def add(a, b):
  return a + b


add(1, 2)  # 3
try:
  add([1, 2])
except TypeError:
  print('add expects two inputs')

add(*[1, 2]) # equivalent to add(1, 2) which returns 3



# Let’s say we want to create a higher-order function that takes as input some function f
# and returns a new function that for any input returns twice the value of f

def doubler(f):
  def g(x):
    return 2 * f(x)

  return g


def f1(x):
  return x + 1

g = doubler(f1)
assert g(3) == 8
assert g(-1) == 0

# this doesn't work for more than one single argument
def f2(x, y):
  return x + y

g = doubler(f2)
try:
  g(1)
except TypeError:
  print('As defined, g only takes one argument')


def doubler_correct(func):
  def g(*args, **kwargs):
    return 2 * func(*args, **kwargs)
  
  return g

g = doubler_correct(f2)
assert g(1, 2) == 6


def magic(*args, **kwargs):
  print('Positional arguments:', args)
  print('Key-word arguments:', kwargs)

# magic(1, 2, key="word", key2="word_2") 

def other_way_magic(x, y, z):
  return x + y + z


x_y_list = [2, 4]
z_dict = {'z': 5}
assert other_way_magic(*x_y_list, **z_dict) == 11  # other_way_magic(*x_y_list, **z_dict) equivalent other_way_magic(2, 4, z=5)

