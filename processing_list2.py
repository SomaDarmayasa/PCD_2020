from PIL import Image, ImageOps
import math
from math import floor


# uts
# soal wajib
def ImgEclipse(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')
    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new('RGB', (horizontalSize, verticalSize))
    npixels = img_output.load()
    for i in range(horizontalSize):
        for j in range(verticalSize):
            r, g, b = pixels[i, j]
            if ((i - horizontalSize//2)**2 + (j - verticalSize//2)**2) < horizontalSize**2/4:
                npixels[i, j] = (255-r, 255-g, 255-b)
                if abs(i - horizontalSize//2) + abs(j - verticalSize//2) < horizontalSize//2:
                    npixels[i, j] = (r, g, b)
            else:
                npixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


# soal bonus

def ImgDiamond(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]

    img_output = Image.new('RGB', (horizontalSize, verticalSize))

    pixels = img_output.load()
    for i in range(horizontalSize):
        for j in range(verticalSize):
            r, g, b = img_input.getpixel((i, j))
            if i <= j:
                if i+j < verticalSize:
                    if (i-horizontalSize/2)**2 + (j-verticalSize/2)**2 < (horizontalSize/2)**2:
                        pixels[i, j] = (r, g, b)
                        if abs(i-horizontalSize/2)+abs(j-verticalSize/2) < horizontalSize/2:
                            pixels[i, j] = (255-r, 255-g, 255-b)
                    else:
                        pixels[i, j] = (255-r, 255-g, 255-b)
                else:
                    if (i-horizontalSize/2)**2 + (j-verticalSize/2)**2 < (horizontalSize/2)**2:
                        pixels[i, j] = (255-r, 255-g, 255-b)
                        if abs(i-horizontalSize/2)+abs(j-verticalSize/2) < horizontalSize/2:
                            pixels[i, j] = (r, g, b)
                    else:
                        pixels[i, j] = (r, g, b)
            else:
                if i+j < horizontalSize:
                    if (i-horizontalSize/2)**2 + (j-verticalSize/2)**2 < (horizontalSize/2)**2:
                        pixels[i, j] = (255-r, 255-g, 255-b)
                        if abs(i-horizontalSize/2)+abs(j-verticalSize/2) < horizontalSize/2:
                            pixels[i, j] = (r, g, b)
                    else:
                        pixels[i, j] = (r, g, b)
                else:

                    if (i-horizontalSize/2)**2 + (j-verticalSize/2)**2 < (horizontalSize/2)**2:
                        pixels[i, j] = (r, g, b)
                        if abs(i-horizontalSize/2)+abs(j-verticalSize/2) < horizontalSize/2:
                            pixels[i, j] = (255-r, 255-g, 255-b)
                    else:
                        pixels[i, j] = (255-r, 255-g, 255-b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output
