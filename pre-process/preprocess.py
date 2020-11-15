from skimage import data
from skimage.io import imsave, imread
import matplotlib.pyplot as plt

image = imread("./originals/100x100_2.png")

nrows, ncols, nchanls = image.shape
print("Shape: ", image.shape)

M = 512
N = 512

tiles = [image[x:x+M, y:y+N]
         for x in range(0, image.shape[0], M) for y in range(0, image.shape[1], N)]

for i in range(64):
    imsave("./p20/test/"+str(i)+".png", tiles[i])
