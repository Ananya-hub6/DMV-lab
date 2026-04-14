import matplotlib.pyplot as plt

def main():
    
    weights = [25, 28, 29, 29, 30, 34, 35, 35, 37, 38]

    
    plt.boxplot(weights)

   
    plt.xlabel("Weights (grams)")
    plt.title("Box Plot of Box Weights")

   
    plt.show()

if __name__ == "__main__":
    main()