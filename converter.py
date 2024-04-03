from PIL import Image
import matplotlib.image as mpimg
from matplotlib import pyplot as plt
import numpy as np

#load
input = plt.imread('input.jpg')
height = int(input.size/3/len(input[1]))
width = int(input.size/3/height)
print('breite:',width, '     höhe:', height)

#process




#save
output = Image.fromarray(input)
output.save('output.png')