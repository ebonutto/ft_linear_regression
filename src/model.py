def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage


def compute_cost(x, y, theta0, theta1):
    m = len(x)
    total = 0.0

    for i in range(m):
        error = estimate_price(x[i], theta0, theta1) - y[i]
        total += error ** 2

    return total / (2 * m)


def gradient_descent(x, y, learning_rate, iterations):
    m = len(x)
    theta0 = 0.0
    theta1 = 0.0
    cost_history =[]

    for _ in range(iterations):
        gradient0 = 0.0
        gradient1 = 0.0

        for i in range(m):
            prediction = estimate_price(x[i], theta0, theta1)
            error = prediction - y[i]

            gradient0 += error
            gradient1 += error * x[i]

        gradient0 /= m
        gradient1 /= m

        theta0 -= learning_rate * gradient0
        theta1 -= learning_rate * gradient1

        cost_history.append(compute_cost(x, y, theta0, theta1))

    return theta0, theta1, cost_history
