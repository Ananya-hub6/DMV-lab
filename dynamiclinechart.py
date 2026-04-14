import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Create figure and axis
fig, ax = plt.subplots()

x_data = []
y_data = []

line, = ax.plot([], [], lw=2)

# Set axis limits
ax.set_xlim(0, 20)
ax.set_ylim(0, 100)

def update(frame):
    x_data.append(frame)
    y_data.append(random.randint(0, 100))
    
    line.set_data(x_data, y_data)
    return line,

# Animate
ani = animation.FuncAnimation(fig, update, frames=range(20), interval=500)

plt.title("Dynamic Line Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
