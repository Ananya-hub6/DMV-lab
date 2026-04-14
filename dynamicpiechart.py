import matplotlib.pyplot as plt

while True:
    a = int(input("Enter value for A: "))
    b = int(input("Enter value for B: "))
    c = int(input("Enter value for C: "))

    plt.clf()  # clear previous chart
    plt.pie([a, b, c], labels=["A", "B", "C"], autopct="%1.1f%%")
    plt.title("Dynamic Pie Chart")
    plt.show()
2