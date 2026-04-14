import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create figure and axis
fig, ax = plt.subplots()

# Set axis limits
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Create a circle
circle = plt.Circle((0, 5), 0.5, fc='blue')
ax.add_patch(circle)

# Update function for animation
def update(frame):
    circle.center = (frame, 5)
    return circle,

# Create animation
ani = animation.FuncAnimation(
    fig,
    update,
    frames=np.linspace(0, 10, 100),
    interval=50
)

plt.show()