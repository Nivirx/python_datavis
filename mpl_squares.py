import matplotlib.pyplot as plt

def main():
    values = [v for v in range(1,11)]
    squares = [v**2 for v in range(1,11)]

    plt.style.use('Solarize_Light2')
    fig, ax = plt.subplots()
    ax.scatter(values, squares, s=100)

    ax.set_title("Square Numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Value squared", fontsize=14)

    ax.tick_params(axis='both', labelsize=14)

    

    plt.show()

if __name__ == '__main__':
    main()