from PIL import Image, ImageOps
import math
from math import floor


def ImgNegative(img_input, coldepth):
    # solusi 1
    # img_output=ImageOps.invert(img_input)

    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            pixels[i, j] = (255-r, 255-g, 255-b)

    if coldepth == 1:
        img_output = img_output.convert("1")

    elif coldepth == 8:
        img_output = img_output.convert("L")

    else:
        img_output = img_output.convert("RGB")

    return img_output


def clipping(intensity):
    if intensity < 0:
        return 0
    if intensity > 255:
        return 255
    return intensity


def ImgBrightness(img_input, coldepth, brightness):
    if coldepth != 24:
        img_input = img_input.convert('RGB')
    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            pixels[i, j] = (clipping(r+brightness),
                            clipping(g+brightness), clipping(b+brightness))

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgBlending(img_input, imgInput2, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')
        imgInput2 = imgInput2.convert('RGB')
        # print(img_input, imgInput2)
    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r1, g1, b1 = img_input.getpixel((i, j))
            r2, g2, b2 = imgInput2.getpixel((i, j))
            Rblend, Gblend, Bblend = r1+r2, g1+g2, b1+b2
            pixels[i, j] = (Rblend, Gblend, Bblend)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgLogaritmic(img_input, coldepth, c):
    # solusi 1
    #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)

    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            pixels[i, j] = (int(c*math.log(1+r)),
                            int(c*math.log(1+g)), int(c*math.log(1+b)))

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgPowerLaw(img_input, coldepth, gamma):
    # solusi 1
    #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)

    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))

            pixels[i, j] = (int(255*(r/255)**gamma),
                            int(255*(g/255)**gamma), int(255*(b/255)**gamma))

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgThreshold(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()
    PIXEL = img_input.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if PIXEL[i, j] < (128, 128, 128):
                pixels[i, j] = (0, 0, 0)
            elif PIXEL[i, j] >= (128, 128, 128):
                pixels[i, j] = (255, 255, 255)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgRotate90(img_input, coldepth, deg, direction):
    # solusi 1
    # img_output=img_input.rotate(deg)

    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if direction == "C":
                r, g, b = img_input.getpixel((j, img_output.size[0]-i-1))

            else:
                r, g, b = img_input.getpixel((img_input.size[1]-j-1, i))

            pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")

    elif coldepth == 8:
        img_output = img_output.convert("L")

    else:
        img_output = img_output.convert("RGB")

    return img_output


# def ImgRotate180(img_input, coldepth, deg, direction):
#     if coldepth != 24:
#         img_input = img_input.convert('RGB')

#     img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
#     pixels = img_output.load()
#     for i in range(img_output.size[0]):
#         for j in range(img_output.size[1]):
#             if direction == "C":
#                 r, g, b = img_input.getpixel(
#                     (img_output.size[1]-i-1, img_output.size[0]-j-1))
#             else:
#                 r, g, b = img_input.getpixel((img_output.size[0]-j-1, i))
#             pixels[i, j] = (r, g, b)

#     if coldepth == 1:
#         img_output = img_output.convert("1")
#     elif coldepth == 8:
#         img_output = img_output.convert("L")
#     else:
#         img_output = img_output.convert("RGB")
#     return img_output


# def ImgRotate270(img_input, coldepth, deg, direction):
#     if coldepth != 24:
#         img_input = img_input.convert('RGB')

#     img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
#     pixels = img_output.load()
#     for i in range(img_output.size[0]):
#         for j in range(img_output.size[1]):
#             if direction == "C":
#                 r, g, b = img_input.getpixel((img_output.size[1]-j-1, i))
#             else:
#                 r, g, b = img_input.getpixel((img_input.size[1]-j-1, i))
#             pixels[i, j] = (r, g, b)

#     if coldepth == 1:
#         img_output = img_output.convert("1")
#     elif coldepth == 8:
#         img_output = img_output.convert("L")
#     else:
#         img_output = img_output.convert("RGB")
#     return img_output


def ImgFlippingVertikal(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    PIXEL = img_input.load()

    ukuran_horizontal = img_input.size[0]
    ukuran_vertikal = img_input.size[1]

    img_output = Image.new("RGB", (ukuran_horizontal, ukuran_vertikal))
    PIXEL_BARU = img_output.load()

    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertikal):
            PIXEL_BARU[x, y] = PIXEL[x, ukuran_vertikal - 1 - y]

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgFlippingHorizontal(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    PIXEL = img_input.load()

    ukuran_horizontal = img_input.size[0]
    ukuran_vertikal = img_input.size[1]

    img_output = Image.new("RGB", (ukuran_horizontal, ukuran_vertikal))
    PIXEL_BARU = img_output.load()

    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertikal):
            PIXEL_BARU[x, y] = PIXEL[ukuran_horizontal - 1 - x, y]

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgFlippingVerHor(img_input, coldepth):
    #img_output = img_input.transpose(Image.FLIP_LEFT_RIGHT)

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[0]):
            r, g, b = img_input.getpixel(
                ((img_output.size[0]-1)-i, (img_output.size[1]-1)-j))
            pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgTranslasi(img_input, coldepth, sumbuTransform):
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixel = img_input.load()
    pixels = img_output.load()

    n = 50

    for i in range(img_input.size[0]):
        for j in range(img_input.size[1]):

            r, g, b = img_input.getpixel((i, j))
            r = 0
            g = 0
            b = 0

            if sumbuTransform == "x":
                if i <= n:
                    pixels[i, j] = (r, g, b)
                else:
                    pixels[i, j] = pixel[i - n, j]
            elif sumbuTransform == "y":
                if j <= n:
                    pixels[i, j] = (r, g, b)
                else:
                    pixels[i, j] = pixel[i, j - n]

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

# def TranslasiXY(img_input, coldepth, x, y):
#     if coldepth != 24:
#         img_input = img_input.convert('RGB')
#     img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
#     pixels = img_output.load()

#     for i in range(img_output.size[0]):
#         for j in range(img_output.size[1]):
#             r, g, b = img_input.getpixel((i, j))
#             if i+x < img_output.size[0] and j+y < img_output.size[1]:
#                 pixels[i, j] = (r, g, b)
#             else:
#                 pixels[i, j] = (0, 0, 0)
#     if coldepth == 1:
#         img_output = img_output.convert("1")
#     elif coldepth == 8:
#         img_output = img_output.convert("L")
#     else:
#         img_output = img_output.convert("RGB")

#     return img_output


def ImgZoom(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    N = 2
    rowOut, colOut = int(img_input.size[0]*N), int(img_input.size[1]*N)

    img_output = Image.new('RGB', (rowOut, colOut))
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((floor(i/N), floor(j/N)))
            pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgShrinking(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    N = 2
    rowOut, colOut = int(img_input.size[0]/N), int(img_input.size[1]/N)

    img_output = Image.new('RGB', (rowOut, colOut))
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((floor(i*N), floor(j*N)))
            pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

# make a function to make eclipse shape in input image


def ImgEclipse(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')
    pixel = img_input.load()
    # make a new image with same size as input image
    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    # load the pixels
    pixels = img_output.load()

    # make a variable to store the center of the image
    center_x = img_input.size[0]//2
    center_y = img_input.size[1]//2

    # make a variable to store the radius of the image
    radius_x = img_input.size[0]//2
    radius_y = img_input.size[1]//2

    # make a variable to store the color of the image
    color = (255, 255, 255)

    # make a loop to make the eclipse shape
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            if (i-center_x)**2/radius_x**2 + (j-center_y)**2/radius_y**2 <= 1:
                r, g, b = img_input.getpixel((i, j))
                pixels[i, j] = (255-r, 255-g, 255-b)
            else:
                pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgTest(img_input, coldepth):
    # solusi 1
    # img_output=ImageOps.invert(img_input)

    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if i < int(img_output.size[0]/2):
                r, g, b = img_input.getpixel((i, j))
                pixels[i, j] = (r, g, b)
            else:
                r, g, b = img_input.getpixel((i, j))
                gray = (r+g+b)//3

                pixels[i, j] = (gray, gray, gray)

    if coldepth == 1:
        img_output = img_output.convert("1")

    elif coldepth == 8:
        img_output = img_output.convert("L")

    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgTest2(img_input, coldepth):
    # solusi 1
    # img_output=ImageOps.invert(img_input)

    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if i < j:
                # r, g, b = img_input.getpixel((i, j))
                # gray = (r+g+b)//3
                # pixels[i, j] = (gray, gray, gray)
                r, g, b = img_input.getpixel((i, j))
                pixels[i, j] = (255-r, 255-g, 255-b)

            else:
                r, g, b = img_input.getpixel((i, j))
                pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")

    elif coldepth == 8:
        img_output = img_output.convert("L")

    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgTest3(img_input, coldepth):
    # solusi 1
    # img_output=ImageOps.invert(img_input)

    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if i+j <= img_output.size[0]:
                r, g, b = img_input.getpixel((i, j))
                gray = (r+g+b)//3
                pixels[i, j] = (gray, gray, gray)
                # r, g, b = img_input.getpixel((i, j))
                # pixels[i, j] = (255-r, 255-g, 255-b)

            else:
                r, g, b = img_input.getpixel((i, j))
                pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")

    elif coldepth == 8:
        img_output = img_output.convert("L")

    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgTest4(img_input, coldepth, gamma=4):
    # solusi 1
    # img_output=ImageOps.invert(img_input)

    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    PIXEL = img_input.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):

            if j < int((img_output.size[1]/2)):
                if i > (img_output.size[1]/2):
                    # r, g, b = img_input.getpixel((i, j))
                    # gray = (r+g+b)//3
                    # pixels[i, j] = (gray, gray, gray)
                    r, g, b = img_input.getpixel((i, j))
                    pixels[i, j] = (255-r, 255-g, 255-b)

                else:
                    if PIXEL[i, j] < (128, 128, 128):
                        pixels[i, j] = (0, 0, 0)
                    elif PIXEL[i, j] >= (128, 128, 128):
                        pixels[i, j] = (255, 255, 255)

            else:
                if i > (img_output.size[1]/2):
                    r, g, b = img_input.getpixel((i, j))
                    pixels[i, j] = (r, g, b)
                else:
                    r, g, b = img_input.getpixel((i, j))
                    pixels[i, j] = (int(255*(r/255)**gamma),
                                    int(255*(g/255)**gamma), int(255*(b/255)**gamma))

    if coldepth == 1:
        img_output = img_output.convert("1")

    elif coldepth == 8:
        img_output = img_output.convert("L")

    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgTest5(img_input, coldepth, gamma=3):
    # solusi 1
    # img_output=ImageOps.invert(img_input)

    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    PIXEL = img_input.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if i+j <= img_output.size[0]:
                if i < j:
                    # r, g, b = img_input.getpixel((i, j))
                    # gray = (r+g+b)//3
                    # pixels[i, j] = (gray, gray, gray)
                    r, g, b = img_input.getpixel((i, j))
                    pixels[i, j] = (255-r, 255-g, 255-b)
                else:
                    r, g, b = img_input.getpixel((i, j))
                    pixels[i, j] = (int(255*(r/255)**gamma),
                                    int(255*(g/255)**gamma), int(255*(b/255)**gamma))

            elif i < j:
                if PIXEL[i, j] < (128, 128, 128):
                    pixels[i, j] = (0, 0, 0)
                elif PIXEL[i, j] >= (128, 128, 128):
                    pixels[i, j] = (255, 255, 255)
            else:
                r, g, b = img_input.getpixel((i, j))
                pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")

    elif coldepth == 8:
        img_output = img_output.convert("L")

    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgFlip2image(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new("RGB", (horizontalSize*2, verticalSize*2))
    newPixels = img_output.load()
    for i in range(horizontalSize):
        for j in range(verticalSize):
            r, g, b = pixels[i, j]
            newPixels[i, j] = (r, g, b)
            newPixels[i, verticalSize*2-1-j] = (r, g, b)
            newPixels[horizontalSize*2-1-i, j] = (r, g, b)
            newPixels[horizontalSize*2-1-i, verticalSize*2-1-j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output


def ImgBlendsmall(img_input, imgInput2, coldepth):
    if coldepth != 24:
        imgInput2 = ImgShrinking(imgInput2, coldepth)
        img_input = img_input.convert('RGB')
        imgInput2 = imgInput2.convert('RGB')

    pixels = img_input.load()
    pixels2 = imgInput2.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    horizontalSize2 = imgInput2.size[0]
    verticalSize2 = imgInput2.size[1]
    img_output = Image.new('RGB', (horizontalSize, verticalSize))
    pixelsbaru = img_output.load()
    for i in range(horizontalSize):
        for j in range(verticalSize):
            if i < horizontalSize2 and j < verticalSize2:
                r1, g1, b1 = pixels[i, j]
                r2, g2, b2 = pixels2[i, j]
                pixelsbaru[i, j] = (r1//2+r2//2, g1//2+g2//2, b1//2+b2//2)

            else:
                pixelsbaru[i, j] = pixels[i, j]

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgRotate270coba(img_input, coldepth, direction=270):
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new("RGB", (verticalSize, horizontalSize))
    newPixels = img_output.load()
    if direction == 270:
        for i in range(horizontalSize):
            for j in range(verticalSize):
                r, g, b = pixels[i, j]
                newPixels[j, horizontalSize-1-i] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output


def ImgBlendsmall270(img_input, imgInput2, coldepth):
    if coldepth != 24:

        imgInput2 = ImgShrinking(imgInput2, coldepth)
        imgInput2 = ImgRotate270coba(imgInput2, coldepth, direction=270)
        img_input = ImgFlippingHorizontal(img_input, coldepth)
        img_input = img_input.convert('RGB')
        imgInput2 = imgInput2.convert('RGB')

    pixels = img_input.load()
    pixels2 = imgInput2.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    horizontalSize2 = imgInput2.size[0]
    verticalSize2 = imgInput2.size[1]
    img_output = Image.new('RGB', (horizontalSize, verticalSize))
    pixelsbaru = img_output.load()
    for i in range(horizontalSize):
        for j in range(verticalSize):
            if i < horizontalSize2 and j < verticalSize2:
                r1, g1, b1 = pixels[i, j]
                r2, g2, b2 = pixels2[i, j]
                pixelsbaru[i, j] = (r1//2+r2//2, g1//2+g2//2, b1//2+b2//2)

            else:
                pixelsbaru[i, j] = pixels[i, j]

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgBlendsmall270flip(img_input, imgInput2, coldepth):
    if coldepth != 24:

        imgInput2 = ImgShrinking(imgInput2, coldepth)
        # imgInput2 = ImgRotate270coba(imgInput2, coldepth, direction=270)
        imgInput2 = ImgFlippingHorizontal(imgInput2, coldepth)
        img_input = ImgRotate180(img_input, coldepth, direction=180)
        img_input = img_input.convert('RGB')
        imgInput2 = imgInput2.convert('RGB')

    pixels = img_input.load()
    pixels2 = imgInput2.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    horizontalSize2 = imgInput2.size[0]
    verticalSize2 = imgInput2.size[1]
    img_output = Image.new('RGB', (horizontalSize, verticalSize))
    pixelsbaru = img_output.load()
    for i in range(horizontalSize):
        for j in range(verticalSize):
            if i < horizontalSize2 and j < verticalSize2:
                r1, g1, b1 = pixels[i, j]
                r2, g2, b2 = pixels2[i, j]
                pixelsbaru[i, j] = (r1//2+r2//2, g1//2+g2//2, b1//2+b2//2)

            else:
                pixelsbaru[i, j] = pixels[i, j]

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output
    # return ImgFlippingVertikal(img_output, coldepth)
    # return ImgFlippingVerHor(img_output, coldepth)
    # return ImgRotate180(img_output, coldepth, direction=180)

# def ImgBlendsmall270flip(img_input, imgInput2, coldepth):
#     if coldepth != 24:

#         imgInput2 = ImgShrinking(imgInput2, coldepth)
#         # imgInput2 = ImgRotate270coba(imgInput2, coldepth, direction=270)
#         imgInput2 = ImgFlippingHorizontal(imgInput2, coldepth)
#         img_input = ImgRotate180(img_input, coldepth, direction=180)
#         img_input = img_input.convert('RGB')
#         imgInput2 = imgInput2.convert('RGB')

#     pixels = img_input.load()
#     pixels2 = imgInput2.load()
#     horizontalSize = img_input.size[0]
#     verticalSize = img_input.size[1]
#     horizontalSize2 = imgInput2.size[0]
#     verticalSize2 = imgInput2.size[1]
#     img_output = Image.new('RGB', (horizontalSize, verticalSize))
#     pixelsbaru = img_output.load()
#     for i in range(horizontalSize):
#         for j in range(verticalSize):
#             if j < verticalSize/2:
#                 if i > verticalSize/2:
#                     pixelsbaru[i, j] = pixels[i, j]

#                 else:
#                     pixelsbaru[i, j] = pixels[i, j]
#             else:
#                 if i > verticalSize/2:
#                     pixelsbaru[i, j] = pixels[i, j]
#                 else:
#                     if i < horizontalSize2 and j < verticalSize2:
#                         r1, g1, b1 = pixels[i, j]
#                         r2, g2, b2 = pixels2[i, j]
#                         pixelsbaru[i, j] = (
#                             r1//2+r2//2, g1//2+g2//2, b1//2+b2//2)
#                     else:
#                         pixelsbaru[i, j] = pixels[i, j]

#     if coldepth == 1:
#         img_output = img_output.convert("1")
#     elif coldepth == 8:
#         img_output = img_output.convert("L")
#     else:
#         img_output = img_output.convert("RGB")

#     return img_output
#     # return ImgFlippingVertikal(img_output, coldepth)
#     # return ImgFlippingVerHor(img_output, coldepth)
#     # return ImgRotate180(img_output, coldepth, direction=180)


def ImgRotate180(img_input, coldepth, direction=180):
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new("RGB", (horizontalSize, verticalSize))
    newPixels = img_output.load()
    if direction == 180:
        for i in range(horizontalSize):
            for j in range(verticalSize):
                r, g, b = pixels[i, j]
                newPixels[horizontalSize-1-i, verticalSize-1-j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output
