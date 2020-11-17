from skimage import data
from skimage.io import imsave, imread
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

ORIGINAL = "./originals/100x100_1.png"
TRAIN_PATH = "./p20/train/images/"
TEST_PATH = "./p20/test/"

SAMPLE_IMAGE = "./p20/train/images/1.png"
SAMPLE_LABEL = "./p20/train/labels/0.png"


def split_image(image_path, save_path, splited_dimensions):
    image = imread(image_path)
    nrows, ncols, nchanls = image.shape
    M, N = splited_dimensions
    tiles = [image[x:x+M, y:y+N]
             for x in range(0, image.shape[0], M) for y in range(0, image.shape[1], N)]
    for i in range(64):
        imsave(save_path+str(i)+".png", tiles[i])


# Spliting Original Image:
split_image(ORIGINAL, TRAIN_PATH, (512, 512))


def gaussian(image_path):
    image = imread(image_path)

    # label = np.array(Image.open(label_path))
    label = imread(image_path)
    label = 100.0 * (label[:, :, 0] > 0)
    label = gaussian_filter(label, sigma=(1, 1), order=0)

    plt.imshow(label, cmap='gray')
    plt.show()


# gaussian(SAMPLE_LABEL)
