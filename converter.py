from PIL import Image
import matplotlib.image as mpimg
from matplotlib import pyplot as plt
import numpy as np

GRID_SIZE = 10

#load
input = np.array(plt.imread('input.jpg'))
height = len(input[1])
width = len(input)
print('breite:',width, '     höhe:', height)

#process
greyscale = input
copy = np.empty([width,height],dtype = int)
grid = np.empty([width//GRID_SIZE,height//GRID_SIZE], dtype = int)
for x in range(0, width):
    for y in range(0, height):
        temp = input[x][y]
        mid = (int(temp[0])+int(temp[1])+int(temp[2]))/3
        greyscale[x][y] = mid
        copy[x][y] = mid
print(copy)

for x in range(0, width):
    for y in range(0, height):
        if x % GRID_SIZE == 0 and y % GRID_SIZE == 0:
            grid[x//GRID_SIZE][y//GRID_SIZE] = int(copy [x][y])

print(grid)

np.savetxt('grid.txt',grid)



#`.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@
#save
output = Image.fromarray(greyscale)
output.save('output.png')