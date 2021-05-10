from collections import Counter
from matplotlib import pyplot as plt

grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]

# Bucket grades by decile, but put 100 in with the 90s
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

plt.bar(histogram.keys(),
        histogram.values(),
        width=10,
        align='edge',
        edgecolor=(0, 0, 0))

plt.axis([-5, 105, 0, 5])

# 5 unit ticks on the x-axis: 0, 10, ..., 100
plt.xticks(range(0, 101, 10))

plt.xlabel('Decile')
plt.ylabel('# of students')
plt.title('Distribution of Exam 1 Grades')

plt.show()