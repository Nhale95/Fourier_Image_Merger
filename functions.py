import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Function to perform Fourier transformation on an image
# Input: PIL image object, n - size of square image to resize to
# Output: 2D Fourier-transformed array
def fourier(image, n):
    im1 = Image.fromarray(image)
    im2 = im1.resize([n, n])
    array1 = np.mean(im2, axis=2)
    return np.fft.fft2(array1)

# Function to create a mask for filtering high and low-frequency features in an image
# Input: n - size of square image, p - filtering parameter
# Output: Binary mask for filtering
def filter(n, p):
    mask = np.zeros([n, n])
    for j in range(0, n, 1):
        for i in range(0, n, 1):
            if (j >= n / 2 - (np.round(p * n)) and j <= n / 2 + (np.round(p * n))):
                mask[i, j] = 1
            if (i >= n / 2 - (np.round(p * n)) and i <= n / 2 + (np.round(p * n))):
                mask[i, j] = 1
    return mask

# Function to splice two images in the Fourier domain
# Input: near - PIL image for near field, far - PIL image for far field,
#        n - size of square image, p - filtering parameter
# Output: Spliced image in the spatial domain
def splice(near, far, n, p):
    f = fourier(near, n) * filter(n, p)
    g = fourier(far, n) * (1 - filter(n, p))
    h = f + g
    return (np.abs(np.fft.ifft2(h))).astype(np.uint8)

# Function to combine RGB images into a color image
# Input: image_1 - path to the first image, image_2 - path to the second image,
#        size - size of the square image, near_field_far_field_factor - filtering parameter
# Output: Saves the combined image as 'images/spliced.png'
def combine(image_1, image_2, size, near_field_far_field_factor):
    img = cv2.imread(image_1)
    r = img.copy()
    r[:, :, 0] = r[:, :, 1] = 0
    g = img.copy()
    g[:, :, 0] = g[:, :, 2] = 0
    b = img.copy()
    b[:, :, 1] = b[:, :, 2] = 0

    img2 = cv2.imread(image_2)
    r2 = img2.copy()
    r2[:, :, 0] = r2[:, :, 1] = 0
    g2 = img2.copy()
    g2[:, :, 0] = g2[:, :, 2] = 0
    b2 = img2.copy()
    b2[:, :, 1] = b2[:, :, 2] = 0

    print("Splicing red images")
    R = splice(r, r2, size, near_field_far_field_factor)

    print("Splicing blue images")
    B = splice(b, b2, size, near_field_far_field_factor)

    print("Splicing green images")
    G = splice(g, g2, size, near_field_far_field_factor)

    print("Combining color images into JPEG")
    rgbArray = np.zeros((size, size, 3), 'uint8')
    rgbArray[..., 0] = R * 1.5
    rgbArray[..., 1] = G * 1.5
    rgbArray[..., 2] = B * 1.5
    img = Image.fromarray(rgbArray)
    img = img.resize([1000, 600])
    img.save('images/spliced.png')

# Function to initiate the image splicing process
# Input: near_field_image - path to the near field image, far_field_image - path to the far field image,
#        fourier_factor - filtering parameter for Fourier transform
# Output: Saves the spliced image as 'images/spliced.png'
def Image_mesh(near_field_image, far_field_image, fourier_factor):
    try:
        combine("images/{}".format(near_field_image), "images/{}".format(far_field_image), 200, fourier_factor)
    except:
        print("Please make sure image files are inputted correctly (with the file type extension)")
