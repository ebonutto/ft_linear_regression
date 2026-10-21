def gradient_descent(x, y, learning_rate, iterations):
    m = len(x)
    theta0 = 0.0
    theta1 = 0.0

    for _ in range(iterations):
        gradient0 = 0.0
        gradient1 = 0.0

        for i in range(m):
            prediction = theta0 + theta1 * x[i]
            error = prediction - y[i]

            gradient0 += error
            gradient1 += error * x[i]

        gradient0 /= m
        gradient1 /= m

        theta0 -= learning_rate * gradient0
        theta1 -= learning_rate * gradient1

    return theta0, theta1
