# Central Tendencies
num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

daily_minutes = [1,68.77,51.25,52.08,38.36,44.54,57.13,51.4,41.42,31.22,34.76,54.01,38.79,47.59,49.1,27.66,41.03,36.73,48.65,28.12,46.62,35.57,32.98,35,26.07,23.77,39.73,40.57,31.65,31.21,36.32,20.45,21.93,26.02,27.34,23.49,46.94,30.5,33.8,24.23,21.4,27.94,32.24,40.57,25.07,19.42,22.39,18.42,46.96,23.72,26.41,26.97,36.76,40.32,35.02,29.47,30.2,31,38.11,38.18,36.31,21.03,30.86,36.07,28.66,29.08,37.28,15.28,24.17,22.31,30.17,25.53,19.85,35.37,44.6,17.23,13.47,26.33,35.02,32.09,24.81,19.33,28.77,24.26,31.98,25.73,24.86,16.28,34.51,15.23,39.72,40.8,26.06,35.76,34.76,16.13,44.04,18.03,19.65,32.62,35.59,39.43,14.18,35.24,40.13,41.82,35.45,36.07,43.67,24.61,20.9,21.9,18.79,27.61,27.21,26.61,29.77,20.59,27.53,13.82,33.2,25,33.1,36.65,18.63,14.87,22.2,36.81,25.53,24.62,26.25,18.21,28.08,19.42,29.79,32.8,35.99,28.32,27.79,35.88,29.06,36.28,14.1,36.63,37.49,26.9,18.58,38.48,24.48,18.95,33.55,14.24,29.04,32.51,25.63,22.22,19,32.73,15.16,13.9,27.2,32.01,29.27,33,13.74,20.42,27.32,18.23,35.35,28.48,9.08,24.62,20.12,35.26,19.92,31.02,16.49,12.16,30.7,31.22,34.65,13.13,27.51,33.2,31.57,14.1,33.42,17.44,10.12,24.42,9.82,23.39,30.93,15.03,21.67,31.09,33.29,22.61,26.89,23.48,8.38,27.81,32.35,23.84]

daily_hours = [dm / 60 for dm in daily_minutes]

import sys
from typing import List
sys.path.append('../chapter-4')  ## To have access to linearAlgebra modules

def mean(xs: List[float]) -> float:
  return sum(xs) / len(xs)


def _median_odd(xs: List[float]) -> float:
  """ If len(xs) is odd, the median is the middle element"""
  return sorted(xs)[len(xs) // 2]

def _median_even(xs: List[float]) -> float:
  """ If len(xs) is even, the median is the average of the middle two elements """
  i = len(xs) // 2
  sorted_xs = sorted(xs)
  return (sorted_xs[i - 1] + sorted_xs[i]) / 2


def median(v: List[float]) -> float:
  """ Finds the 'middle-most' value of v """
  return _median_odd(v) if len(v) % 2 else _median_even(v)


assert median([1, 10, 2, 9, 5]) == 5
assert median([1, 9, 2, 10]) == (2 + 9) / 2


def quantile(xs: List[float], p: float) -> float:
  """ Returns the pth-percentile value in x """
  p_index = int(p * len(xs))
  return sorted(xs)[p_index]


def mode(x: List[float]) -> List[float]:
  """ Returns a list, since there might be more than one mode """
  from collections import Counter
  counts = Counter(x)
  max_count = max(counts.values())
  return [x_i for (x_i, count) in counts.items() if count == max_count]

# Dispersion
def data_range(xs: List[float]) -> float:
  return max(xs) - min(xs)


def de_mean(xs: List[float]) -> List[float]:
  """ Translates xs by subtracting its mean (so the result has mean 0) """
  x_bar = mean(xs)
  return [x - x_bar for x in xs]


from linearAlgebra_vectors import sum_of_squares # type: ignore
def variance(xs: List[float]) -> float:
  """ Almost the average squared deviation from the mean """
  n = len(xs)
  assert n >= 2, "variance requires at least two elements"
  deviations = de_mean(xs)
  return sum_of_squares(deviations) / (n - 1)
  

import math
def standared_deviation(xs: List[float]) -> float:
  """ The standard deviation is the square root of the variance """
  return math.sqrt(variance(xs))

def interquartile_range(xs: List[float]) -> float:
  """ Returns th difference between the 75%-ile and the 25%-ile """
  return quantile(xs, 0.75) - quantile(xs, 0.25)


# Correlation

from linearAlgebra_vectors import dot
def covariance(xs: List[float], ys: List[float]) -> float:
  assert len(xs) == len(ys), "xs and ys mus have the same length"
  return dot(de_mean(xs), de_mean(ys)) / (len(xs) - 1)


def correlation(xs: List[float], ys: List[float]) -> float:
  """ Measures how much xs and ys vary in tandem about their means """
  stdev_x = standared_deviation(xs)
  stdev_y = standared_deviation(ys)
  if stdev_x == 0 or stdev_y == 0:
    return 0   # if no variation, correlation is zero
  return covariance(xs, ys) / stdev_x / stdev_y
  

assert 0.24 < correlation(num_friends, daily_minutes) < 0.25
assert 0.24 < correlation(num_friends, daily_hours) < 0.25


# from matplotlib import pyplot as plt

# plt.scatter(num_friends, daily_minutes)
# plt.title('Correlation with an Outlier')
# plt.xlabel('# of friends')
# plt.ylabel('minutes per day')

# # plt.axis('square') plt.axis('scaled')
# plt.gca().set_aspect('equal', adjustable='box')
# plt.axis([0, 105, 0, 100])

# plt.show()

# Ignore the outlier
outlier = num_friends.index(100) # index of outlier
num_friends_good = [ x for (index, x) in enumerate(num_friends, 0)
                    if index != outlier]

daily_minutes_good = [x for (index, x) in enumerate(daily_minutes)
                      if index != outlier]

daily_hours_good = [dm / 60 for dm in daily_minutes_good]

# much stronger correlation without the outlier
0.57 < correlation(num_friends_good, daily_minutes_good) < 0.58
0.57 < correlation(num_friends_good, daily_hours_good) < 0.58


x = [-2, -1, 0, 1, 2]
y = [2, 1, 0, 1, 2]
z = [99.98, 99.99, 100, 100.01, 100.02]

print(standared_deviation(x))
print(standared_deviation(y))
print(covariance(x, y))
print(correlation(x, y)) # correlation is zero (no correlation)

print(standared_deviation(z))
print(covariance(x, z))
print(correlation(x, z)) # correlation is one (perfect correlation)
