### Using a 2D grid (100 x 100), a square with side length r (), and circle with radius r
### Randomly place marbles into grid, if inside a shape, increment shape counter
### pi = circle count / square count

### Explaination: square area = r^2, Circle area = pi x r^2

### therefore as placement is random the number of marbles in the circle is equal to
### the number of marbles in the square times pi 

import math
from random import randint

def inCircle(x,y):
    d = math.sqrt((x-30)**2 + (y-70)**2)

    if d <= 30:
        return True
    else:
        return False


def inSquare(x,y):

    if (x>=70) and (x<=100) and (y>=0) and (y<=30):
        return True
    else:
        return False


def MonteCarlo(marbleCount):
    squareCounter = 0
    circleCounter = 0

    for i in range(marbleCount):
        x = randint(0, 100)
        y = randint(0, 100)

        if inCircle(x, y):
            circleCounter += 1
        
        elif inSquare(x, y):
            squareCounter += 1

    pi = circleCounter / squareCounter
    return pi


# To accurately find pi, run the simuulation repeatedly and return the average

total = 0
epochs = 100

for i in range(epochs):
    total += MonteCarlo(100000)

print("pi - ", total / epochs)