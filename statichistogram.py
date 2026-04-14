import numpy as np
import matplotlib.pyplot as plt

# Sample data
data = np.random.randn(1000)

# Plot histogram
plt.hist(data, bins=30, color='steelblue', edgecolor='black')

# Labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Static Histogram')

plt.show()
