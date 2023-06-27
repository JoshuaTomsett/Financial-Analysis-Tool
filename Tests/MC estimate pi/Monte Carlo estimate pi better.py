### This program is an improved version of its predecessor

### Instead of having a large amount of dead space like in the previous version,
### This version's grid is 2r x 2r (60 x 60, r = 30), and only contains a circle of radius r
### So the marbles will fall into either the circle, or the square (grid)
### Meaning, there is no dead space, as the marbles fall into either the circle or the square

### Explaination: area of grid = 4r^2 , area of circle = pi x r^2

### Therefore, if we divide the area of the cicle by the area of the grid, we get pi / 4
### So pi = 4 x (marbles in circle / total marbles)

import math
from random import randint

def inCircle(x,y):
    d = math.sqrt((x-30)**2 + (y-30)**2)

    if d <= 30:
        return True
    else:
        return False


def MonteCarlo(marbleCount):
    circleCounter = 0

    for i in range(marbleCount):
        x = randint(0, 60)
        y = randint(0, 60)

        if inCircle(x, y):
            circleCounter += 1

    pi = 4 * (circleCounter / marbleCount)
    return pi

total = 0
epochs = 100

for i in range(epochs):
    total += MonteCarlo(1000)

print("pi - ", total / epochs)