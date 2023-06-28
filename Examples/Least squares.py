import sys
sys.path.append('..')
import stockdata
from analysisTools import calcRegressionLine
from matplotlib import pyplot as plt


ticker = 'TSLA'
days = 30
data = stockdata.get_data_days(ticker, days)
x = []
for i in data:
    x.append(i)

y = list(range(1, len(x)+1))

a,b = calcRegressionLine(x, y)
print(a,b)

# Plot the data and the regression line
plt.plot(y, x, 'o')
plt.plot([a*i + b for i in x], x, '-')
plt.show()