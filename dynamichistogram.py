import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
data = np.random.randn(1000)

def update(frame):
    ax.clear()
    new_data = np.random.randn(1000)
    ax.hist(new_data, bins=30, color='skyblue', edgecolor='black')
    ax.set_title("Dynamic Histogram")
    ax.set_xlim(-4, 4)
    ax.set_ylim(0, 150)

ani = FuncAnimation(fig, update, interval=500)
plt.show()
