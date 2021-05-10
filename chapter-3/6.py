import matplotlib.pyplot as plt


friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes, marker='*', color='black')

# label each point
for (label, friend, minute) in zip(labels, friends, minutes):
  plt.annotate(label,
              xy=(friend, minute), #put the label with its point
              xytext=(10, -5),    #but slightly offset
              textcoords='offset points',
              color='red')

plt.xlabel('# of friends')
plt.ylabel('daily minutes spent on the site')
plt.title('Daily Minutes Vs. Number of Friends')

plt.show()