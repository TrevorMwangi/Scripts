import matplotlib.pyplot as plt

x = range(7)
y = [1, 4, 3, 5, 4, 6, 1]
errors = [1, 0.3, 0.4, 0.6, 0.2, 0.1, 0.5]

plt.errorbar(x, y, yerr=errors, fmt="x", capsize=5)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Error Bars")
plt.show()