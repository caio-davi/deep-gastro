import os
from skimage import data
from skimage.io import imsave, imread, imshow
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

ORIGINAL = "./originals/100x100_1.png"
TRAIN_PATH = "./p20/train/"
TEST_PATH = "./p20/test/"

SAMPLE_IMAGE = "./p20/train/images/1.png"
SAMPLE_LABEL = "./p20/train/labels/0.png"
SAMPLE_ANOTATION = "./p20/train/anotations/0.png"


def split_image(image_path, save_path, splited_dimensions):
    image = imread(image_path)
    nrows, ncols, nchanls = image.shape
    M, N = splited_dimensions
    tiles = [image[x:x+M, y:y+N]
             for x in range(0, image.shape[0], M) for y in range(0, image.shape[1], N)]
    for i in range(64):
        imsave(save_path+str(i)+".png", tiles[i])


# Spliting Original Image:
# split_image(ORIGINAL, TRAIN_PATH, (512, 512))


def saveBW(image_name, image_path, label_path):
    label = imread(image_path+image_name)
    label = 255 * (label[:, :, 1] > 0)
    plt.imshow(label)
    plt.show()
    imsave(label_path+image_name, label)


def createLabels(anotation_path, label_path):
    a = os.listdir(anotation_path)
    for img in a:
        saveBW(img, anotation_path, label_path)
    print(a)


# saveBW("1.png", TRAIN_PATH+"anotations/", TRAIN_PATH+"labels/")
createLabels(TRAIN_PATH+"anotations/", TRAIN_PATH+"labels/")
