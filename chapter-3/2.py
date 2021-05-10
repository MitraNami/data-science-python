import matplotlib.pyplot as plt


# create a bar chart
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

plt.bar(range(len(movies)), num_oscars)
plt.title('My Favorite Movies')
plt.ylabel('# of Academy Awards')

# label x-axis with movie names at bar centers
plt.xticks(range(len(movies)), movies)
plt.show()