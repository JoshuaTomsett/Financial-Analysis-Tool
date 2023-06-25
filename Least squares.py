from matplotlib import pyplot as plt


def calcRegressionLine(x, y):
    """
    Calculates the regression line using the least squares method.

    Args:
        x: Array of x values
        y: Array of y values

    Returns:
        The slope (a) and intercept (b) of the regression line (y = ax+ b)
    """

    n = len(x)
    Sx = sum(x)
    Sx2 = sum(i*i for i in x)
    Sy = sum(y)
    Sxy = sum(a * b for a, b in zip(x, y))

    a = (n*Sxy - Sx*Sy) / (n*Sx2 - Sx**2)

    b = (Sx2*Sy - Sx*Sxy) / (n*Sx2 - Sx**2)

    return a,b


x = [1, 2, 3, 4, 5]
y = [2, 5, 3, 8, 7]

a,b = calcRegressionLine(x, y)
print(a,b)

# Plot the data and the regression line
plt.plot(x, y, 'o')
plt.plot(x, [a*i + b for i in x], '-')
plt.show()