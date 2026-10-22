def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage


def gradient_descent(x, y, learning_rate, iterations):
    m = len(x)
    theta0 = 0.0
    theta1 = 0.0

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

    return theta0, theta1
