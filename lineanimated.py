import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create figure and axis
fig, ax = plt.subplots()

# Set axis limits
ax.set_xlim(0, 10)
ax.set_ylim(0, 100)

# Create empty line
line, = ax.plot([], [], lw=2)

# Data
x_data = []
y_data = []

# Initialization function
def init():
    line.set_data([], [])
    return line,

# Update function
def update(frame):
    x_data.append(frame)
    y_data.append(frame * frame)  # y = x^2
    line.set_data(x_data, y_data)
    return line,

# Create animation
ani = animation.FuncAnimation(
    fig,
    update,
    frames=np.linspace(0, 10, 100),
    init_func=init,
    interval=50,
    blit=True
)

plt.show()