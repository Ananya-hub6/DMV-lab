import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D']
values = [20, 35, 30, 25]

# Create bar chart
plt.bar(categories, values)

# Labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Static Bar Chart')

# Show chart
plt.show()