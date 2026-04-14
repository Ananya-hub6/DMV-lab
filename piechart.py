import matplotlib.pyplot as plt

# Data
labels = ['Rent', 'Food', 'Utilities', 'Entertainment', 'Savings']
sizes = [1200, 600, 300, 200, 700]

# Create pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Monthly Expense Distribution')

# Show chart
plt.show()
