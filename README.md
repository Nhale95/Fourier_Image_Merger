# Fourier Image Splicing

This Python project focuses on image processing using Fourier transformations to splice two images together. It includes functions for Fourier transformations, image filtering, and combining images into a single spliced image.

## Functions

### Fourier Transformation

The `fourier` function takes a PIL image object and resizes it to a square with `n` by `n` pixels. It then performs a Fourier transformation on the image.

### Image Filtering

The `filter` function generates a mask for filtering high and low-frequency features in an image. The mask is created based on the size of the square image (`n`) and a filtering parameter (`p`).

### Image Splicing

The `splice` function takes two PIL images (near field and far field), along with the image resizing value `n` and filtering parameter `p`. It applies Fourier transformations and filtering to both images and then combines them using inverse Fourier transformation.

### Image Combination

The `combine` function splices images for the red, green, and blue color channels, creating a color image. It uses the splicing functions for each color channel.

### Main Application

A GUI is started upon running the file "Fourier_Image_Splicing.py". This will then prompt you to upload a near and far field image from the directory "images". You are also promted to input a merged image parameter between 0 and 0.5. 0.4 is suggested. This will then save an output image named "spliced.png"

## Usage

To use this project
Install the required libraries using:
   ```bash
   pip install numpy pillow matplotlib


## Example

To see the example images and their spliced result, please navigate to the [images folder](https://github.com/Nhale95/Fourier_Image_Merger/tree/main/images) in this repository.

The filenames include:
- `near_field_image.png`
- `far_field_image.png`
- `spliced_example.png`

You can view the images directly by clicking on the filenames in the `images` folder.

