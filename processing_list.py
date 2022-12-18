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


# def ImgTest5(img_input, coldepth, gamma=3):
#     # solusi 1
#     # img_output=ImageOps.invert(img_input)

#     # solusi 2
#     if coldepth != 24:
#         img_input = img_input.convert('RGB')

#     img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
#     pixels = img_output.load()
#     PIXEL = img_input.load()
#     for i in range(img_output.size[0]):
#         for j in range(img_output.size[1]):
#             if i+j <= img_output.size[0]:
#                 if i < j:
#                     # r, g, b = img_input.getpixel((i, j))
#                     # gray = (r+g+b)//3
#                     # pixels[i, j] = (gray, gray, gray)
#                     r, g, b = img_input.getpixel((i, j))
#                     pixels[i, j] = (255-r, 255-g, 255-b)
#                 else:
#                     r, g, b = img_input.getpixel((i, j))
#                     pixels[i, j] = (int(255*(r/255)**gamma),
#                                     int(255*(g/255)**gamma), int(255*(b/255)**gamma))

#             elif i < j:
#                 if PIXEL[i, j] < (128, 128, 128):
#                     pixels[i, j] = (0, 0, 0)
#                 elif PIXEL[i, j] >= (128, 128, 128):
#                     pixels[i, j] = (255, 255, 255)
#             else:
#                 r, g, b = img_input.getpixel((i, j))
#                 pixels[i, j] = (r, g, b)

#     if coldepth == 1:
#         img_output = img_output.convert("1")

#     elif coldepth == 8:
#         img_output = img_output.convert("L")

#     else:
#         img_output = img_output.convert("RGB")

#     return img_output

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
                    # r, g, b = img_input.getpixel((i, j))
                    # pixels[i, j] = (int(255*(r/255)**gamma),
                    #                 int(255*(g/255)**gamma), int(255*(b/255)**gamma))
                    r, g, b = img_input.getpixel((i, j))
                    pixels[i, j] = (r, g, b)

            elif i < j:
                # if PIXEL[i, j] < (128, 128, 128):
                #     pixels[i, j] = (0, 0, 0)
                # elif PIXEL[i, j] >= (128, 128, 128):
                #     pixels[i, j] = (255, 255, 255)
                r, g, b = img_input.getpixel((i, j))
                pixels[i, j] = (r, g, b)

            else:
                # r, g, b = img_input.getpixel((i, j))
                # pixels[i, j] = (r, g, b)
                r, g, b = img_input.getpixel((i, j))
                pixels[i, j] = (255-r, 255-g, 255-b)

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
        # imgInput2 = ImgFlippingHorizontal(imgInput2, coldepth)
        # img_input = ImgRotate180(img_input, coldepth, direction=180)
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
            # put the image 2 in the middle of image 1
            # if i > horizontalSize//2-horizontalSize2//2 and i < horizontalSize//2+horizontalSize2//2 and j > verticalSize//2-verticalSize2//2 and j < verticalSize//2+verticalSize2//2:
            #     r, g, b = pixels[i, j]
            #     r2, g2, b2 = pixels2[i-horizontalSize//2 +
            #                          horizontalSize2//2, j-verticalSize//2+verticalSize2//2]
            #     pixelsbaru[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            # else:
            #     pixelsbaru[i, j] = pixels[i, j]

            # put the image 2 in the middle right of image 1
            if i > horizontalSize//2 and i < horizontalSize//2+horizontalSize2 and j > verticalSize//2-verticalSize2//2 and j < verticalSize//2+verticalSize2//2:
                r, g, b = pixels[i, j]
                r2, g2, b2 = pixels2[i-horizontalSize//2,
                                     j-verticalSize//2+verticalSize2//2]
                pixelsbaru[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            else:
                pixelsbaru[i, j] = pixels[i, j]

            # put the image 2 in the button right of image 1
            # if i > horizontalSize//2 and i < horizontalSize//2+horizontalSize2 and j > verticalSize//2 and j < verticalSize//2+verticalSize2:
            #     r, g, b = pixels[i, j]
            #     r2, g2, b2 = pixels2[i-horizontalSize//2, j-verticalSize//2]
            #     pixelsbaru[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            # else:
            #     pixelsbaru[i, j] = pixels[i, j]

            # put the image 2 in the up right corner of image 1
            # if i > horizontalSize//2 and i < horizontalSize//2+horizontalSize2 and j > 0 and j < verticalSize2:
            #     r, g, b = pixels[i, j]
            #     r2, g2, b2 = pixels2[i-horizontalSize//2, j]
            #     pixelsbaru[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            # else:
            #     pixelsbaru[i, j] = pixels[i, j]

            # put the image 2 in the corner of image 1
            # if i > horizontalSize//2 and i < horizontalSize//2+horizontalSize2 and j > verticalSize//2 and j < verticalSize//2+verticalSize2:
            #     r, g, b = pixels[i, j]
            #     r2, g2, b2 = pixels2[i-horizontalSize//2, j-verticalSize//2]
            #     pixelsbaru[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            # else:
            #     pixelsbaru[i, j] = pixels[i, j]

            # put the image 2 in right corner up of image 1 ???????
            # if i > horizontalSize//2 and i < horizontalSize//2+horizontalSize2 and j > verticalSize//2-verticalSize2 and j < verticalSize//2:
            #     r1, g1, b1 = pixels[i, j]
            #     r2, g2, b2 = pixels2[i-horizontalSize //
            #                          2, j-verticalSize//2+verticalSize2]
            #     pixelsbaru[i, j] = (r1//2+r2//2, g1//2+g2//2, b1//2+b2//2)

            # else:
            #     pixelsbaru[i, j] = pixels[i, j]

            # if i > horizontalSize//2 and i < horizontalSize//2+horizontalSize2 and j > verticalSize//2 and j < verticalSize//2+verticalSize2:
            #     r, g, b = pixels[i, j]
            #     r2, g2, b2 = pixels2[i-horizontalSize//2, j-verticalSize//2]
            #     pixelsbaru[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            # else:
            #     pixelsbaru[i, j] = pixels[i, j]

            # if i > horizontalSize//2 and i < horizontalSize//2+horizontalSize2 and j > 0 and j < verticalSize2:
            #     r, g, b = pixels[i, j]
            #     r2, g2, b2 = pixels2[i-horizontalSize//2, j]
            #     pixelsbaru[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            # else:
            #     pixelsbaru[i, j] = pixels[i, j]

            # if i< horizontalSize2 and j < verticalSize2:
            #     r, g, b = pixels[i, j]
            #     r2, g2, b2 = pixels2[i, j]
            #     pixelsbaru[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
            # else:
                # pixelsbaru[i, j] = pixels[i, j]

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    # return img_output
    # return ImgFlippingVertikal(img_output, coldepth)
    # return ImgFlippingVerHor(img_output, coldepth)
    return ImgRotate180(img_output, coldepth, direction=180)

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

# make function to rotate 90 degree in image


# def ImgRotate90(img_input, coldepth, direction=90):
#     if coldepth != 24:
#         img_input = img_input.convert('RGB')

#     pixels = img_input.load()
#     horizontalSize = img_input.size[0]
#     verticalSize = img_input.size[1]
#     img_output = Image.new("RGB", (verticalSize, horizontalSize))
#     newPixels = img_output.load()
#     if direction == 90:
#         for i in range(horizontalSize):
#             for j in range(verticalSize):
#                 r, g, b = pixels[i, j]
#                 newPixels[j, horizontalSize-1-i] = (r, g, b)

#     if coldepth == 1:
#         img_output = img_output.convert("1")
#     elif coldepth == 8:
#         img_output = img_output.convert("L")
#     else:
#         img_output = img_output.convert("RGB")
#     return img_output


# def ImgKotakkecil(img_input, coldepth):
#     if coldepth != 24:
#         img_input = img_input.convert('RGB')

#     pixels = img_input.load()
#     horizontalSize = img_input.size[0]
#     verticalSize = img_input.size[1]
#     img_output = Image.new("RGB", (horizontalSize, verticalSize))
#     newPixels = img_output.load()
#     for i in range(horizontalSize):
#         for j in range(verticalSize):
#             r, g, b = pixels[i, j]
#             if i > horizontalSize/2-50 and i < horizontalSize/2+50 and j > verticalSize/2-50 and j < verticalSize/2+50:
#                 newPixels[i, j] = (r, g, b)
#             else:
#                 newPixels[i, j] = (255, 255, 255)

#     if coldepth == 1:
#         img_output = img_output.convert("1")
#     elif coldepth == 8:
#         img_output = img_output.convert("L")
#     else:
#         img_output = img_output.convert("RGB")
#     return img_output


# def Imgkotak4(img_input, coldepth):
#     if coldepth != 24:
#         img_input = img_input.convert('RGB')

#     pixels = img_input.load()
#     horizontalSize = img_input.size[0]
#     verticalSize = img_input.size[1]
#     img_output = Image.new("RGB", (horizontalSize, verticalSize))
#     newPixels = img_output.load()
#     for i in range(horizontalSize):
#         for j in range(verticalSize):
#             r, g, b = pixels[i, j]
#             if i > horizontalSize/2 and j > verticalSize/2:
#                 newPixels[i, j] = (r, g, b)
#             elif i < horizontalSize/2 and j < verticalSize/2:
#                 newPixels[i, j] = (r, g, b)
#             elif i > horizontalSize/2 and j < verticalSize/2:
#                 newPixels[i, j] = (r, g, b)
#             elif i < horizontalSize/2 and j > verticalSize/2:
#                 newPixels[i, j] = (r, g, b)
#             else:
#                 newPixels[i, j] = (255-r, 255-g, 255-b)

#     if coldepth == 1:
#         img_output = img_output.convert("1")
#     elif coldepth == 8:
#         img_output = img_output.convert("L")
#     else:
#         img_output = img_output.convert("RGB")
#     return img_output


# def ImgTest5(img_input, coldepth):
#     if coldepth != 24:
#         img_input = img_input.convert('RGB')

#     pixels = img_input.load()
#     horizontalSize = img_input.size[0]
#     verticalSize = img_input.size[1]
#     img_output = Image.new("RGB", (horizontalSize, verticalSize))
#     newPixels = img_output.load()
#     for i in range(horizontalSize):
#         for j in range(verticalSize):
#             r, g, b = pixels[i, j]
#             if i < horizontalSize/2:
#                 if j < verticalSize/2:
#                     if i < j:
#                         newPixels[i, j] = (r, g, b)
#                     else:
#                         newPixels[i, j] = (0, 0, 0)
#                 else:
#                     if i < verticalSize-j:
#                         newPixels[i, j] = (r, g, b)
#                     else:
#                         newPixels[i, j] = (0, 0, 0)
#             else:
#                 if j < verticalSize/2:
#                     if horizontalSize-i < j:
#                         newPixels[i, j] = (r, g, b)
#                     else:
#                         newPixels[i, j] = (0, 0, 0)
#                 else:
#                     if horizontalSize-i < verticalSize-j:
#                         newPixels[i, j] = (r, g, b)
#                     else:
#                         newPixels[i, j] = (0, 0, 0)

#     if coldepth == 1:
#         img_output = img_output.convert("1")
#     elif coldepth == 8:
#         img_output = img_output.convert("L")
#     else:
#         img_output = img_output.convert("RGB")
#     return img_output


# def ImgDiamond(img_input, coldepth):
#     if coldepth != 24:
#         img_input = img_input.convert('RGB')

#     pixels = img_input.load()
#     horizontalSize = img_input.size[0]
#     verticalSize = img_input.size[1]
#     img_output = Image.new("RGB", (horizontalSize, verticalSize))
#     newPixels = img_output.load()
#     for i in range(horizontalSize):
#         for j in range(verticalSize):
#             r, g, b = pixels[i, j]
#             if i < horizontalSize/2:
#                 if j < verticalSize/2:
#                     if i+j < horizontalSize/2:
#                         newPixels[i, j] = (r, g, b)
#                     else:
#                         newPixels[i, j] = (255, 255, 255)
#                 else:
#                     if i+j < horizontalSize/2+verticalSize/2:
#                         newPixels[i, j] = (r, g, b)
#                     else:
#                         newPixels[i, j] = (255, 255, 255)
#             else:
#                 if j < verticalSize/2:
#                     if i+j < horizontalSize/2+verticalSize/2:
#                         newPixels[i, j] = (r, g, b)
#                     else:
#                         newPixels[i, j] = (255, 255, 255)
#                 else:
#                     if i+j < horizontalSize+verticalSize:
#                         newPixels[i, j] = (r, g, b)
#                     else:
#                         newPixels[i, j] = (255, 255, 255)

#     if coldepth == 1:
#         img_output = img_output.convert("1")
#     elif coldepth == 8:
#         img_output = img_output.convert("L")
#     else:
#         img_output = img_output.convert("RGB")
#     return img_output


# def ImgDiamond(img_input, coldepth):
#     if coldepth != 24:
#         img_input = img_input.convert('RGB')
#     pixels = img_input.load()
#     horizontalSize = img_input.size[0]
#     verticalSize = img_input.size[1]
#     img_output = Image.new('RGB', (horizontalSize, verticalSize))
#     npixels = img_output.load()
#     for i in range(horizontalSize):
#         for j in range(verticalSize):
#             r, g, b = pixels[i, j]
#             if abs(i - horizontalSize//2) + abs(j - verticalSize//2) < horizontalSize//2:
#                 npixels[i, j] = (255-r, 255-g, 255-b)
#             else:
#                 npixels[i, j] = (r, g, b)

#     if coldepth == 1:
#         img_output = img_output.convert("1")
#     elif coldepth == 8:
#         img_output = img_output.convert("L")
#     else:
#         img_output = img_output.convert("RGB")

#     return img_output


def ImgFlip2imagerotate(img_input, coldepth):
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
            r, g, b = img_output.getpixel((j, img_output.size[0]-i-1))
            newPixels[i+img_input.size[0],
                      j+img_input.size[1]] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output


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
# def ImgDiamond(img_input, coldepth):
#     if coldepth != 24:
#         img_input = img_input.convert('RGB')
#     pixels = img_input.load()
#     horizontalSize = img_input.size[0]
#     verticalSize = img_input.size[1]
#     img_output = Image.new('RGB', (horizontalSize, verticalSize))
#     npixels = img_output.load()
#     for i in range(horizontalSize):
#         for j in range(verticalSize):
#             r, g, b = pixels[i, j]
#             if i+j <= img_output.size[0]:
#                 if i < j:

#                     r, g, b = img_input.getpixel((i, j))
#                     pixels[i, j] = (255-r, 255-g, 255-b)
#                 else:

#                     r, g, b = img_input.getpixel((i, j))
#                     pixels[i, j] = (r, g, b)


#             elif i < j:

#                 r, g, b = img_input.getpixel((i, j))
#                 pixels[i, j] = (r, g, b)

#             else:

#                 r, g, b = img_input.getpixel((i, j))
#                 pixels[i, j] = (255-r, 255-g, 255-b)

#             if ((i - horizontalSize//2)**2 + (j - verticalSize//2)**2) < horizontalSize**2/4:
#                 npixels[i, j] = (255-r, 255-g, 255-b)
#                 if abs(i - horizontalSize//2) + abs(j - verticalSize//2) < horizontalSize//2:
#                     npixels[i, j] = (r, g, b)

#             else:
#                 npixels[i, j] = (r, g, b)

#     if coldepth == 1:
#         img_output = img_output.convert("1")
#     elif coldepth == 8:
#         img_output = img_output.convert("L")
#     else:
#         img_output = img_output.convert("RGB")

#     return img_output

# def ImgDiamond(img_input, coldepth):
#     if coldepth != 24:
#         img_input = img_input.convert('RGB')
#     pixels = img_input.load()
#     horizontalSize = img_input.size[0]
#     verticalSize = img_input.size[1]
#     img_output = Image.new('RGB', (horizontalSize, verticalSize))
#     npixels = img_output.load()
#     for i in range(horizontalSize):
#         for j in range(verticalSize):
#             # r, g, b = pixels[i, j]
#             r, g, b = pixels[i, j]
#             if i+j <= img_output.size[0]:
#                 if ((i - horizontalSize//2)**2 + (j - verticalSize//2)**2) < horizontalSize**2/4:
#                     npixels[i, j] = (r, g, b)
#                     if abs(i - horizontalSize//2) + abs(j - verticalSize//2) < horizontalSize//2:
#                         npixels[i, j] = (255-r, 255-g, 255-b)
#                 else:
#                     npixels[i, j] = (255-r, 255-g, 255-b)
#             else :


#             # if ((i - horizontalSize//2)**2 + (j - verticalSize//2)**2) < horizontalSize**2/4:
#             #     npixels[i, j] = (255-r, 255-g, 255-b)
#             #     if abs(i - horizontalSize//2) + abs(j - verticalSize//2) < horizontalSize//2:
#             #         npixels[i, j] = (r, g, b)

#             # else:
#             #     npixels[i, j] = (r, g, b)

#     if coldepth == 1:
#         img_output = img_output.convert("1")
#     elif coldepth == 8:
#         img_output = img_output.convert("L")
#     else:
#         img_output = img_output.convert("RGB")

#     return img_output

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


def ImgMean(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()

    for i in range(1, img_input.size[0]-1):
        for j in range(1, img_input.size[1]-1):
            r, g, b = img_input.getpixel((i, j))
            r2, g2, b2 = img_input.getpixel((i-1, j-1))
            r3, g3, b3 = img_input.getpixel((i-1, j))
            r4, g4, b4 = img_input.getpixel((i-1, j+1))
            r5, g5, b5 = img_input.getpixel((i, j-1))
            r6, g6, b6 = img_input.getpixel((i, j+1))
            r7, g7, b7 = img_input.getpixel((i+1, j-1))
            r8, g8, b8 = img_input.getpixel((i+1, j))
            r9, g9, b9 = img_input.getpixel((i+1, j+1))
            r_list = [r, r2, r3, r4, r5, r6, r7, r8, r9]
            g_list = [g, g2, g3, g4, g5, g6, g7, g8, g9]
            b_list = [b, b2, b3, b4, b5, b6, b7, b8, b9]
            r_mean = sum(r_list)//len(r_list)
            g_mean = sum(g_list)//len(g_list)
            b_mean = sum(b_list)//len(b_list)
            pixels[i, j] = (r_mean, g_mean, b_mean)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgMedianFilter(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()

    print(img_input.size[0])
    print(img_input.size[1])

    for i in range(1, img_input.size[0]-1):
        for j in range(1, img_input.size[1]-1):
            r, g, b = img_input.getpixel((i, j))
            r2, g2, b2 = img_input.getpixel((i-1, j-1))
            r3, g3, b3 = img_input.getpixel((i-1, j))
            r4, g4, b4 = img_input.getpixel((i-1, j+1))
            r5, g5, b5 = img_input.getpixel((i, j-1))
            r6, g6, b6 = img_input.getpixel((i, j+1))
            r7, g7, b7 = img_input.getpixel((i+1, j-1))
            r8, g8, b8 = img_input.getpixel((i+1, j))
            r9, g9, b9 = img_input.getpixel((i+1, j+1))
            r_list = [r, r2, r3, r4, r5, r6, r7, r8, r9]
            g_list = [g, g2, g3, g4, g5, g6, g7, g8, g9]
            b_list = [b, b2, b3, b4, b5, b6, b7, b8, b9]
            r_list.sort()
            g_list.sort()
            b_list.sort()
            pixels[i, j] = (r_list[4], g_list[4], b_list[4])

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgMinFilter(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()

    for i in range(1, img_input.size[0]-1):
        for j in range(1, img_input.size[1]-1):
            r1, g1, b1 = img_input.getpixel((i, j))
            r2, g2, b2 = img_input.getpixel((i-1, j-1))
            r3, g3, b3 = img_input.getpixel((i-1, j))
            r4, g4, b4 = img_input.getpixel((i-1, j+1))
            r5, g5, b5 = img_input.getpixel((i, j-1))
            r6, g6, b6 = img_input.getpixel((i, j+1))
            r7, g7, b7 = img_input.getpixel((i+1, j-1))
            r8, g8, b8 = img_input.getpixel((i+1, j))
            r9, g9, b9 = img_input.getpixel((i+1, j+1))
            r_list = [r1, r2, r3, r4, r5, r6, r7, r8, r9]
            g_list = [g1, g2, g3, g4, g5, g6, g7, g8, g9]
            b_list = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
            r_min = min(r_list)
            g_min = min(g_list)
            b_min = min(b_list)
            pixels[i, j] = (r_min, g_min, b_min)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgMaxFilter(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()

    for i in range(1, img_input.size[0]-1):
        for j in range(1, img_input.size[1]-1):
            r, g, b = img_input.getpixel((i, j))
            r2, g2, b2 = img_input.getpixel((i-1, j-1))
            r3, g3, b3 = img_input.getpixel((i-1, j))
            r4, g4, b4 = img_input.getpixel((i-1, j+1))
            r5, g5, b5 = img_input.getpixel((i, j-1))
            r6, g6, b6 = img_input.getpixel((i, j+1))
            r7, g7, b7 = img_input.getpixel((i+1, j-1))
            r8, g8, b8 = img_input.getpixel((i+1, j))
            r9, g9, b9 = img_input.getpixel((i+1, j+1))
            r_list = [r, r2, r3, r4, r5, r6, r7, r8, r9]
            g_list = [g, g2, g3, g4, g5, g6, g7, g8, g9]
            b_list = [b, b2, b3, b4, b5, b6, b7, b8, b9]
            r_max = max(r_list)
            g_max = max(g_list)
            b_max = max(b_list)
            pixels[i, j] = (r_max, g_max, b_max)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def WeightMeanFilter(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()

    koef1 = 2
    koef2 = 4

    for i in range(1, img_input.size[0]-1):
        for j in range(1, img_input.size[1]-1):
            r, g, b = img_input.getpixel((i, j))  # tengah
            r2, g2, b2 = img_input.getpixel((i-1, j-1))  # kiri atas
            r3, g3, b3 = img_input.getpixel((i-1, j))  # kiri
            r4, g4, b4 = img_input.getpixel((i-1, j+1))  # kiri bawah
            r5, g5, b5 = img_input.getpixel((i, j-1))  # tengah atas
            r6, g6, b6 = img_input.getpixel((i, j+1))  # tengah bawah
            r7, g7, b7 = img_input.getpixel((i+1, j-1))  # kanan atas
            r8, g8, b8 = img_input.getpixel((i+1, j))  # kanan
            r9, g9, b9 = img_input.getpixel((i+1, j+1))  # kanan bawah
            r_list = [r*koef2, r2, r3*koef1, r4,
                      r5*koef1, r6*koef1, r7, r8*koef1, r9]
            g_list = [g*koef2, g2, g3*koef1, g4,
                      g5*koef1, g6*koef1, g7, g8*koef1, g9]
            b_list = [b*koef2, b2, b3*koef1, b4,
                      b5*koef1, b6*koef1, b7, b8*koef1, b9]
            r_mean = sum(r_list)//16
            g_mean = sum(g_list)//16  # karena 16 adalah jumlah koefisien
            b_mean = sum(b_list)//16
            pixels[i, j] = (r_mean, g_mean, b_mean)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def GradientFilter(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

    pixels = img_output.load()
    pixels_x = img_output.load()
    pixels_y = img_output.load()

    # mask = [-1, 1]
    mask2 = [1, -1]

    # for i in range(img_input.size[0]-1):
    # for j in range(img_input.size[1]-1):
    #     r, g, b = img_input.getpixel((i, j))
    #     r2, g2, b2 = img_input.getpixel((i+1, j))  # kanan
    #     r3, g3, b3 = img_input.getpixel((i, j+1))  # bawah

    #     # print(r2)

    #     r_sum_x = (r*mask[0])+(r2*mask[1])
    #     g_sum_x = (g*mask[0])+(g2*mask[1])
    #     b_sum_x = (b*mask[0])+(b2*mask[1])
    #     pixels_x[i, j] = (r_sum_x, g_sum_x, b_sum_x)

    #     r_sum_y = (r*mask[1])+(r3*mask[0])
    #     g_sum_y = (g*mask[1])+(g3*mask[0])
    #     b_sum_y = (b*mask[1])+(b3*mask[0])
    #     pixels_y[i, j] = (r_sum_y, g_sum_y, b_sum_y)

    #     r_sum_xy = (abs(r_sum_x))+(abs(r_sum_y))
    #     g_sum_xy = (abs(g_sum_x))+(abs(g_sum_y))
    #     b_sum_xy = (abs(b_sum_x))+(abs(b_sum_y))
    #     pixels[i, j] = (r_sum_xy, g_sum_xy, b_sum_xy)

    for i in range(img_input.size[0]-1):
        for j in range(img_input.size[1]-1):
            r, g, b = img_input.getpixel((i, j))
            r2, g2, b2 = img_input.getpixel((i+1, j))  # kanan
            r3, g3, b3 = img_input.getpixel((i, j+1))  # bawah

            # print(r2)

            r_sum_x = (r*mask2[0])+(r2*mask2[1])
            g_sum_x = (g*mask2[0])+(g2*mask2[1])
            b_sum_x = (b*mask2[0])+(b2*mask2[1])
            pixels_x[i, j] = (r_sum_x, g_sum_x, b_sum_x)

            r_sum_y = (r*mask2[1])+(r3*mask2[0])
            g_sum_y = (g*mask2[1])+(g3*mask2[0])
            b_sum_y = (b*mask2[1])+(b3*mask2[0])
            pixels_y[i, j] = (r_sum_y, g_sum_y, b_sum_y)

            r_sum_xy = (abs(r_sum_x))+(abs(r_sum_y))
            g_sum_xy = (abs(g_sum_x))+(abs(g_sum_y))
            b_sum_xy = (abs(b_sum_x))+(abs(b_sum_y))
            pixels[i, j] = (r_sum_xy, g_sum_xy, b_sum_xy)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def CenterDifFilter(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

    pixels_x = img_output.load()
    pixels_y = img_output.load()
    pixels = img_output.load()

    mask = [-1, 0, 1]
    # mask2 = [1, 0, -1]

    for i in range(img_input.size[0]-2):
        for j in range(img_input.size[1]-2):
            r, g, b = img_input.getpixel((i, j))
            r2, g2, b2 = img_input.getpixel((i+1, j))  # kanan
            r3, g3, b3 = img_input.getpixel((i+2, j))  # kanan2
            r4, g4, b4 = img_input.getpixel((i, j+1))  # bawah
            r5, g5, b5 = img_input.getpixel((i, j+2))  # bawah2

            # print(r2)
            r_sum_x = (r*mask[0])+(r2*mask[1])+r3*mask[2]
            g_sum_x = (g*mask[0])+(g2*mask[1])+g3*mask[2]
            b_sum_x = (b*mask[0])+(b2*mask[1])+b3*mask[2]
            pixels_x[i, j] = (r_sum_x, g_sum_x, b_sum_x)

            r_sum_y = (r*mask[2])+(r4*mask[1])+r5*mask[0]
            g_sum_y = (g*mask[2])+(g4*mask[1])+g5*mask[0]
            b_sum_y = (b*mask[2])+(b4*mask[1])+b5*mask[0]
            pixels_y[i, j] = (r_sum_y, g_sum_y, b_sum_y)

            r_sum_xy = (abs(r_sum_x))+(abs(r_sum_y))
            g_sum_xy = (abs(g_sum_x))+(abs(g_sum_y))
            b_sum_xy = (abs(b_sum_x))+(abs(b_sum_y))
            pixels[i, j] = (r_sum_xy, g_sum_xy, b_sum_xy)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def SobelFilter(img_input, coldepth):
    if coldepth != 25:
        img_input = img_input.convert("RGB")
        input_pixels = img_input.load()

        output_image = Image.new(
            'RGB', (img_input.size[0], img_input.size[1]))
        output_pixels = output_image.load()

    box_kernel_x = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]]

    box_kernel_y = [
        [1, 2, 1],
        [0, 0, 0],
        [-1, -2, -1]]

    kernel_x = box_kernel_x
    kernel_y = box_kernel_y
    offset = len(kernel_x)//2

    for x in range(offset, img_input.size[0] - offset):
        for y in range(offset, img_input.size[1] - offset):
            pixel_sx = [0, 0, 0]
            pixel_sy = [0, 0, 0]

            for a in range(len(kernel_x)):
                for b in range(len(kernel_x)):
                    xn = x + a - offset
                    yn = y + b - offset
                    pixel = input_pixels[xn, yn]
                    pixel_sx[0] += pixel[0] * kernel_x[a][b]
                    pixel_sx[1] += pixel[1] * kernel_x[a][b]
                    pixel_sx[2] += pixel[2] * kernel_x[a][b]

                    pixel_sy[0] += pixel[0] * kernel_y[a][b]
                    pixel_sy[1] += pixel[1] * kernel_y[a][b]
                    pixel_sy[2] += pixel[2] * kernel_y[a][b]

            r_sum = abs(pixel_sx[0])+abs(pixel_sy[0])
            g_sum = abs(pixel_sx[1])+abs(pixel_sy[1])
            b_sum = abs(pixel_sx[2])+abs(pixel_sy[2])

            output_pixels[x, y] = (r_sum, g_sum, b_sum)

    if coldepth == 1:
        output_image = output_image.convert("1")
    elif coldepth == 8:
        output_image = output_image.convert("L")
    else:
        output_image = output_image.convert("RGB")

    return output_image


def PrewittFilter(img_input, coldepth):
    if coldepth != 25:
        img_input = img_input.convert("RGB")
        input_pixels = img_input.load()

        output_image = Image.new(
            'RGB', (img_input.size[0], img_input.size[1]))
        output_pixels = output_image.load()

    box_kernel_x = [
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]]

    box_kernel_y = [
        [1, 1, 1],
        [0, 0, 0],
        [-1, -1, -1]]

    kernel_x = box_kernel_x
    kernel_y = box_kernel_y
    offset = len(kernel_x)//2

    for x in range(offset, img_input.size[0] - offset):
        for y in range(offset, img_input.size[1] - offset):
            pixel_sx = [0, 0, 0]
            pixel_sy = [0, 0, 0]

            for a in range(len(kernel_x)):
                for b in range(len(kernel_x)):
                    xn = x + a - offset
                    yn = y + b - offset
                    pixel = input_pixels[xn, yn]
                    pixel_sx[0] += pixel[0] * kernel_x[a][b]
                    pixel_sx[1] += pixel[1] * kernel_x[a][b]
                    pixel_sx[2] += pixel[2] * kernel_x[a][b]

                    pixel_sy[0] += pixel[0] * kernel_y[a][b]
                    pixel_sy[1] += pixel[1] * kernel_y[a][b]
                    pixel_sy[2] += pixel[2] * kernel_y[a][b]

            r_sum = abs(pixel_sx[0])+abs(pixel_sy[0])
            g_sum = abs(pixel_sx[1])+abs(pixel_sy[1])
            b_sum = abs(pixel_sx[2])+abs(pixel_sy[2])

            output_pixels[x, y] = (r_sum, g_sum, b_sum)

    if coldepth == 1:
        output_image = output_image.convert("1")
    elif coldepth == 8:
        output_image = output_image.convert("L")
    else:
        output_image = output_image.convert("RGB")

    return output_image


def RobertFilter(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

    pixels = img_output.load()
    pixels_x = img_output.load()
    pixels_y = img_output.load()

    mask = [1, -1]
    # mask2 = [-1, 1]

    for i in range(img_input.size[0]-1):
        for j in range(img_input.size[1]-1):
            r, g, b = img_input.getpixel((i, j))
            r2, g2, b2 = img_input.getpixel((i+1, j))  # kanan
            r3, g3, b3 = img_input.getpixel((i, j+1))  # bawah
            r4, g4, b4 = img_input.getpixel((i+1, j+1))  # kanan bawah

            # print(r2)

            r_sum_x = (r*mask[0])+(r4*mask[1])
            g_sum_x = (g*mask[0])+(g4*mask[1])
            b_sum_x = (b*mask[0])+(b4*mask[1])
            pixels_x[i, j] = (r_sum_x, g_sum_x, b_sum_x)

            r_sum_y = (r2*mask[0])+(r3*mask[1])
            g_sum_y = (g2*mask[0])+(g3*mask[1])
            b_sum_y = (b2*mask[0])+(b3*mask[1])
            pixels_y[i, j] = (r_sum_y, g_sum_y, b_sum_y)

            r_sum_xy = (abs(r_sum_x))+(abs(r_sum_y))
            g_sum_xy = (abs(g_sum_x))+(abs(g_sum_y))
            b_sum_xy = (abs(b_sum_x))+(abs(b_sum_y))
            pixels[i, j] = (r_sum_xy, g_sum_xy, b_sum_xy)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def LaplacianFilter(img_input, coldepth):
    if coldepth != 25:
        img_input = img_input.convert("RGB")
        input_pixels = img_input.load()

        output_image = Image.new(
            'RGB', (img_input.size[0], img_input.size[1]))
        output_pixels = output_image.load()

        # output_image_2 = Image.new(
        #     'RGB', (img_input.size[0], img_input.size[1]))
        # output_pixels_2 = output_image_2.load()

    # laplacian filter memiliki 4 box kernel
    # akan digunakan salah 1 dari box kernel tersebut
    box_kernel = [
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]]

    # box_kernel = [
    #     [-1, -1, -1],
    #     [-1, 8, -1],
    #     [-1, -1, -1]]

    # box_kernel = [
    #     [1, -2, 1],
    #     [-2, 4, -2],
    #     [1, -2, 1]]

    # box_kernel = [
    #     [1, 4, 1],
    #     [4, -20, 4],
    #     [1, 4, 1]]

    kernel = box_kernel
    offset = len(kernel)//2

    for x in range(offset, img_input.size[0] - offset):
        for y in range(offset, img_input.size[1] - offset):
            pixel_sx = [0, 0, 0]

            for a in range(len(kernel)):
                for b in range(len(kernel)):
                    xn = x + a - offset
                    yn = y + b - offset
                    pixel = input_pixels[xn, yn]
                    pixel_sx[0] += pixel[0] * kernel[a][b]
                    pixel_sx[1] += pixel[1] * kernel[a][b]
                    pixel_sx[2] += pixel[2] * kernel[a][b]

            output_pixels[x, y] = (pixel_sx[0], pixel_sx[1], pixel_sx[2])

    # # applying the filter
    # for i in range(offset, img_input.size[0] - offset):
    #     for j in range(offset, img_input.size[1] - offset):
    #         r, g, b = img_input.getpixel((i, j))
    #         r2, g2, b2 = output_image_2.getpixel((i, j))
    #         r_sum = r - r2
    #         g_sum = g - g2
    #         b_sum = b - b2
    #         output_pixels_2[i, j] = (r_sum, g_sum, b_sum)

    if coldepth == 1:
        output_image = output_image.convert("1")
    elif coldepth == 8:
        output_image = output_image.convert("L")
    else:
        output_image = output_image.convert("RGB")

    return output_image


def Erosion(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new('RGB', (horizontalSize, verticalSize))
    newPixels = img_output.load()

    sx = [[0, 1, 0],
          [1, 1, 1],
          [0, 1, 0]]
    offset = len(sx)//2

    for i in range(offset, horizontalSize-offset):
        for j in range(offset, verticalSize-offset):
            xRGB = [0, 0, 0]
            for k in range(len(sx)):
                for l in range(len(sx)):
                    r, g, b = pixels[i+k-offset, j+l-offset]
                    xRGB[0] += r*sx[k][l]
                    xRGB[1] += g*sx[k][l]
                    xRGB[2] += b*sx[k][l]

            for k in range(len(xRGB)):
                xRGB[k] = xRGB[k]//4

            newPixels[i, j] = (xRGB[0], xRGB[1], xRGB[2])

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def Dilation(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new('RGB', (horizontalSize, verticalSize))
    newPixels = img_output.load()

    sx = [[1, 1, 1],
          [1, 1, 1],
          [1, 1, 1]]
    offset = len(sx)//2

    for i in range(offset, horizontalSize-offset):
        for j in range(offset, verticalSize-offset):
            xRGB = [0, 0, 0]
            for k in range(len(sx)):
                for l in range(len(sx)):
                    r, g, b = pixels[i+k-offset, j+l-offset]
                    xRGB[0] += r*sx[k][l]
                    xRGB[1] += g*sx[k][l]
                    xRGB[2] += b*sx[k][l]

            for k in range(len(xRGB)):
                xRGB[k] = xRGB[k]//9

            newPixels[i, j] = (xRGB[0], xRGB[1], xRGB[2])

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def Opening(img_input, coldepth):
    img_output = Erosion(img_input, coldepth)
    img_output = Dilation(img_output, coldepth)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def Closing(img_input, coldepth):
    img_output = Dilation(img_input, coldepth)
    img_output = Erosion(img_output, coldepth)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return


def WhiteTopHat(img_input, coldepth):
    img_output = Opening(img_input, coldepth)
    # buat canvas kosong
    canvas = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    canvasPixels = canvas.load()
    # perulangan untuk mengurangi nilai pixel input dengan output
    for i in range(img_input.size[0]):
        for j in range(img_input.size[1]):
            r, g, b = img_input.getpixel((i, j))
            r2, g2, b2 = img_output.getpixel((i, j))
            r_new = r-r2
            g_new = g-g2
            b_new = b-b2
            # cek jika melebihi 255 maka di set 255
            # cek jika kurang dari 0 maka di set 0
            if r_new > 255:
                r_new = 255
            elif r_new < 0:
                r_new = 0
            if g_new > 255:
                g_new = 255
            elif g_new < 0:
                g_new = 0
            if b_new > 255:
                b_new = 255
            elif b_new < 0:
                b_new = 0

            # lakukan thresholding
            # if r_new > 127:
            #     r_new = 255
            # else:
            #     r_new = 0
            # if g_new > 127:
            #     g_new = 255
            # else:
            #     g_new = 0
            # if b_new > 127:
            #     b_new = 255
            # else:
            #     b_new = 0

            canvasPixels[i, j] = (r_new, g_new, b_new)

    if coldepth == 1:
        canvas = canvas.convert("1")
    elif coldepth == 8:
        canvas = canvas.convert("L")
    else:
        canvas = canvas.convert("RGB")

    return canvas

# BlackTopHat filter
# BELUM MAU BINARY


def BlackTopHat(img_input, coldepth):
    img_output = Closing(img_input, coldepth)
    # buat canvas kosong
    canvas = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    canvasPixels = canvas.load()
    # perulangan untuk mengurangi nilai pixel input dengan output
    for i in range(img_input.size[0]):
        for j in range(img_input.size[1]):
            r, g, b = img_input.getpixel((i, j))
            r2, g2, b2 = img_output.getpixel((i, j))
            r_new = r-r2
            g_new = g-g2
            b_new = b-b2
            # cek jika melebihi 255 maka di set 255
            # cek jika kurang dari 0 maka di set 0
            if r_new > 255:
                r_new = 255
            elif r_new < 0:
                r_new = 0
            if g_new > 255:
                g_new = 255
            elif g_new < 0:
                g_new = 0
            if b_new > 255:
                b_new = 255
            elif b_new < 0:
                b_new = 0

            # lakukan thresholding
            # if r_new > 127:
            #     r_new = 255
            # else:
            #     r_new = 0
            # if g_new > 127:
            #     g_new = 255
            # else:
            #     g_new = 0
            # if b_new > 127:
            #     b_new = 255
            # else:
            #     b_new = 0

            canvasPixels[i, j] = (r_new, g_new, b_new)

    if coldepth == 1:
        canvas = canvas.convert("1")
    elif coldepth == 8:
        canvas = canvas.convert("L")
    else:
        canvas = canvas.convert("RGB")

    return canvas
