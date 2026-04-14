import numpy as np
import matplotlib.pyplot as plt


x1 = np.random.normal(2, 0.5, 30)
y1 = -x1 + np.random.normal(0, 0.5, 30)


x2 = np.random.normal(8, 0.5, 30)
y2 = -x2 + np.random.normal(0, 0.5, 30)


x = np.concatenate((x1, x2))
y = np.concatenate((y1, y2))


x = np.append(x, 5)
y = np.append(y, 10)


plt.scatter(x, y)

plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot with Clusters, Negative Correlation and Outlier")

plt.show()