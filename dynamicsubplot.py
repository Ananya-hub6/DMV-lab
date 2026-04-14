import matplotlib.pyplot as plt

while True:
    x = list(map(int, input("Enter X values (space separated): ").split()))
    y1 = list(map(int, input("Enter Y1 values: ").split()))
    y2 = list(map(int, input("Enter Y2 values: ").split()))

    plt.clf()  # clear previous figure

    plt.subplot(1, 2, 1)
    plt.plot(x, y1)
    plt.title("Plot 1")

    plt.subplot(1, 2, 2)
    plt.plot(x, y2)
    plt.title("Plot 2")

    plt.tight_layout()
    plt.show()
