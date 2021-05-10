from matplotlib import pyplot as plt

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]

total_error = [x + y for (x, y) in zip(variance, bias_squared)]
xs = range(len(variance))

# we can make multiple calls to plt.plot
plt.plot(xs, variance, 'g-', label='variance', marker='o') # green solid line
plt.plot(xs, bias_squared, 'r-.', label='bias^2')  # red dot-dashed line
plt.plot(xs, total_error, 'b:', label='toral error')  # blue dotted line

plt.legend(loc=9)
plt.xlabel('model complexity')
plt.title('The Bias-Variance Tradeoff')
plt.xticks([])
plt.show()
