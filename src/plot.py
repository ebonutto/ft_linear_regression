import matplotlib.pyplot as plt

from model import estimate_price


def plot_fit(mileage, price, theta0, theta1):
    line_x = [min(mileage), max(mileage)]
    line_y = [estimate_price(x, theta0, theta1) for x in line_x]

    plt.scatter(mileage, price, marker="+", label="data")
    plt.plot(line_x, line_y, color="red", label="model")
    plt.xlabel("mileage (km)")
    plt.ylabel("price (€)")
    plt.legend()
    plt.show()
