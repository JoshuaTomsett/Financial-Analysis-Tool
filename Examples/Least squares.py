import sys
sys.path.append('..')
import stockdata
from analysisTools import calcRegressionLine
from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5] # Change to use stockdata
y = [2, 5, 3, 8, 7]

a,b = calcRegressionLine(x, y)
print(a,b)

# Plot the data and the regression line
plt.plot(x, y, 'o')
plt.plot(x, [a*i + b for i in x], '-')
plt.show()