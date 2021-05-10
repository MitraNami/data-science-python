# Object-Oriented Programming

class CountingClicker():
  """ Simulates clicking """

  def __init__(self, count=0):
    self.count = count
  
  def click(self, num_times=1):
    self.count += num_times

  def read(self):
    return self.count

  def reset(self):
    self.count = 0

  def __repr__(self):
    return f"{self.__class__.__name__}(count={self.count})"

# Tests:
clicker = CountingClicker()
assert clicker.read() == 0, "clicker should start with count 0"
clicker.click()
clicker.click()
assert clicker.read() == 2, "after two clicks, clicker should have count 2"
clicker.reset()
assert clicker.read() == 0, "after reset, clicker should be back to 0"

# subclasses
# Create a non-reset-able clicker by using CountingClicker as the base class
class NoResetClicker(CountingClicker):
  def reset(self):
    pass

clicker2 = NoResetClicker()
assert clicker2.read() == 0
clicker2.click()
assert clicker2.read() == 1
clicker2.reset()
assert clicker2.read() == 1, "reset shouldn't do anything"


# Iterables, Iterators, Generators

class Range(): 
  """Simulates the built-in range() function"""
  def __init__(self,start, stop, step=1):
    self.start = start
    self.stop = stop
    self.step = step

  def __iter__(self):
    return RangeIterator(self) # an iterator object


class RangeIterator():
  def __init__(self, rangeObj):
    self.current = rangeObj.start
    self.stop = rangeObj.stop
    self.step = rangeObj.step

  def __next__(self):
    if self.current < self.stop:
      current = self.current
      self.current += self.step
      return current
    raise StopIteration


# for num in Range(0, 5):
#   print(num)

# This is acutally how  a for loop works:
range_iterable = Range(0, 5) # range_ iterable is an iterable because the object returned by its __iter__ is an iterator
range_iterator = range_iterable.__iter__() # range_iterator is an iterator because its __next__ produces new values

while True:
  try:
    num = range_iterator.__next__()  # next(range_iterator)
  except StopIteration:
    break
  else:
    pass
    # what you do with num in the for block e.g print(num)


# generator function
def generate_range(start, stop, step=1):
  current = start
  while current < stop:
    yield current
    current += step
      
# for i in generate_range(0, 5):
#   print(i)

generator = generate_range(0, 2)
# print(generator is iter(generator)) # its __iter__ return self, it has both __iter__ and __next__ , both an iterable and an iterator
# print(dir(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

# infinite seqence
def natural_numbers():
  """returns 1, 2, 3, ..."""
  n = 1
  while True:
    yield n
    n += 1

natural_numbers_generator = natural_numbers()
# print(next(natural_numbers_generator))
# print(next(natural_numbers_generator))
# print(next(natural_numbers_generator))


# Generator expression
evens_below_20 = (i for i in range(1, 20) if i % 2 == 0)
# for even in evens_below_20:
#   print(even)