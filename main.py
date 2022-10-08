from layout import *
import PySimpleGUI as sg  # import library pysimplegui
import os.path  # import library os
from PIL import Image, ImageOps
from processing_list import *


# melooping event atau window nya
while True:
    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    # folder name was filled in, make a list of files in the folder
    if event == "ImgFolder":
        folder = values["ImgFolder"]

        try:
            # get list of the files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif",))
        ]

        window["ImgList"].update(fnames)

    elif event == "ImgList":  # A file wa choosen from the  listbox
        try:
            filename = os.path.join(
                values["ImgFolder"], values["ImgList"][0]
            )
            window["FilepathImgInput"].update(filename)
            window["ImgInputViewer"].update(filename)
            window["ImgProcessingType"].update(filename)
            window["ImgOutputViewer"].update(filename)
            img_input = Image.open(filename)
            # img_input.show()

            # Size
            img_width, img_height = img_input.size
            window["ImgSize"].update(
                # "Image Size : "+str(img_width)+" x "+str(img_height))
                "Image Size : "+str(img_height)+" x "+str(img_width))

            # Color depth
            mode_to_coldepth = {"1": 1, "L": 8, "P": 8, "RGB": 24, "RGBA": 32, "CMYK": 32, "YCbCr": 24, "LAB":
                                24, "HSV": 24, "I": 32, "F": 32}
            coldepth = mode_to_coldepth[img_input.mode]
            window["ImgColorDepth"].update("Color Depth : "+str(coldepth))

        except:
            pass

    elif event == "ImgNegative":

        try:
            window["ImgProcessingType"].update("Image Negative")
            img_output = ImgNegative(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

        except:
            pass

    elif event == "ImgRotate90":

        try:
            window["ImgProcessingType"].update("Image Rotate 90°")
            img_output = ImgRotate90(img_input, coldepth, 90, "C")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

        except:
            pass

    elif event == "ImgRotate180":
        try:
            window["ImgProcessingType"].update("Image Rotate 180°")
            img_output = ImgRotate180(img_input, coldepth, 180, "C")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

        except:
            pass

    elif event == "ImgRotate270":
        try:
            window["ImgProcessingType"].update("Image Rotate 270°")
            img_output = ImgRotate270(img_input, coldepth, 270, "C")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

        except:
            pass

    elif event == "ImgBrightness":

        try:
            value = int(values["SliderBrightness"])
            window["ImgProcessingType"].update("Image Brightness")
            img_output = ImgBrightness(img_input, coldepth, value)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgBlending":

        try:
            filename = values['inputImage2']
            input_image2 = Image.open(filename)
            window["ImgProcessingType"].update("Image  Blending")
            img_output = ImgBlending(img_input, input_image2, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgLogaritmic":

        try:
            window["ImgProcessingType"].update("Image Logaritmic")
            img_output = ImgLogaritmic(img_input, coldepth, 30)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgPowerLaw":

        try:
            window["ImgProcessingType"].update("Image Power Law")
            img_output = ImgPowerLaw(img_input, coldepth, 4)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgFlippingVertikal":

        try:
            window["ImgProcessingType"].update("Image Flip Vertikal")
            img_output = ImgFlippingVertikal(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgFlippingHorizontal":

        try:
            window["ImgProcessingType"].update("Image Flip Horizontal")
            img_output = ImgFlippingHorizontal(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgFlippingVerHor":

        try:
            window["ImgProcessingType"].update("Image Flip ")
            img_output = ImgFlippingVerHor(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass


window.close()
