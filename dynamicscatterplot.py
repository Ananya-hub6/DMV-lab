import matplotlib.pyplot as plt

while True:
    x = list(map(int, input("Enter X values (space separated): ").split()))
    y = list(map(int, input("Enter Y values (space separated): ").split()))

    plt.clf()  # clear previous plot
    plt.scatter(x, y)
    plt.title("Dynamic Scatter Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()
