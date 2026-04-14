import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Data
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

fig, ax = plt.subplots()
bars = ax.bar(categories, values)

ax.set_ylim(0, 50)
ax.set_title('Dynamic Bar Chart')

# Update function
def update(frame):
    for bar in bars:
        bar.set_height(random.randint(5, 45))
    return bars

# Animation
ani = animation.FuncAnimation(
    fig,
    update,
    frames=20,
    interval=1000,
    repeat=True
)

plt.show()