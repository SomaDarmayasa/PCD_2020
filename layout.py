import PySimpleGUI as sg

# membuat kolom area 1 : membuka folder dan memilih image


# definisi masing-masing kolom area
# key = membutuhkan data sudah diinputkan dikomponen tersebut
sg.theme("LightPurple")
file_list_column = [  # struktur data list
    [
        # komponen text menampilkan tampilan buka folder gambar
        sg.Text("Open Image Folder :")
    ],
    [
        # komponen input (properti size,enable events, key=imgfolder artinya untuk mengakses object(folder) yang diletakkan dalam komponen In input)
        sg.In(size=(20, 1), enable_events=True, key="ImgFolder"),
        sg.FolderBrowse(),
    ],
    [
        # menampilkan text masukkan gambar
        sg.Text("Choose an image from list : "),
    ],
    [
        # komponen listbox(properti size,enable events, key=imgfList artinya untuk mengakses object(citra/file gambar) yang diletakkan dalam komponen listbox)
        sg.Listbox(values=[], enable_events=True, size=(18, 10), key="ImgList")
    ],

    # menampilkan text
    [sg.Text("Information Image:"), ],

    # ukuran citra perlu akses sehingga butuh key
    [sg.Text(size=(20, 1), key="ImgSize")],

    # color depth berapa jumlah bit yang digunakan untuk menyimpan citra
    [sg.Text(size=(20, 1), key="ImgColorDepth")],
    [sg.HSeparator()],
    [sg.Text("Open folder image 2"), ],
    [
        sg.Text("to Image Blending : "),
        sg.In(size=(15, 1), enable_events=True, key="inputImage2"),
        sg.FileBrowse(),
    ],
]


# membuat kolom area 2 : area viewer image input

image_viewer_column = [
    # menampilkan text masukkan gambar
    [sg.Text("Image Input : ")],

    # mengakses path dimana citra itu berada,
    # akan berubah2 tergantung path yang dipilih oleh citranya
    [sg.Text(size=(40, 1), key="FilepathImgInput")],

    # menampung dan menampilkan citra
    [sg.Image(key="ImgInputViewer")],
]

# membuat kolom area 3 : Area image info dan tombol list of processing

list_processing = [

    [sg.Text("Feature :")],
    # [sg.Button("Negative", size=(9, 1), key="ImgNegative"), sg.Button(
    #     "Logaritmic", size=(9, 1), key="ImgLogaritmic")],
    # [sg.Button("Blending", size=(9, 1), key="ImgBlending"), sg.Button(
    #     "Power law", size=(9, 1), key="ImgPowerLaw")],
    # [sg.Button("Threshold", size=(9, 1), key="ImgThreshold")],
    # [sg.HSeparator()],
    # [sg.Text("Image Brightness Slider:"), ],
    # [  # slider brightness
    #     sg.Slider(range=(-255, 255), size=(19, 20),
    #               orientation='h',
    #               key="SliderBrightness",
    #               default_value=0), ],
    # [sg.Button("Image Brightness", size=(20, 1), key="ImgBrightness")],
    # [sg.HSeparator()],
    # [sg.Text("Image Rotate:"), ],
    # [sg.Button("90°", size=(9, 1), key="ImgRotate90"),
    #  sg.Button("180°", size=(9, 1), key="ImgRotate180")],
    # [sg.Button("270°", size=(9, 1), key="ImgRotate270")],
    # [sg.HSeparator()],
    # [sg.Text("Image Flipping:"), ],
    # [sg.Button("Vertikal", size=(9, 1), key="ImgFlippingVertikal"),
    #  sg.Button("Horizontal", size=(9, 1), key="ImgFlippingHorizontal")],
    # [sg.Button("Vertikal Horizontal  ", size=(
    #     9, 2), key="ImgFlippingVerHor")],
    [sg.HSeparator()],
    # [sg.Text("Image Translation:"), ],
    # [sg.Button("thd sb.X", size=(9, 1), key="ImgTranslasiX"),
    #  sg.Button("thd sb.Y", size=(9, 1), key=("ImgTranslasiY"))],
    # [sg.HSeparator()],
    # [sg.Text("Image Scalling:"), ],
    # [sg.Button("Zoom", size=(9, 1), key="ImgZoom"), sg.Button(
    #     "Shrinking", size=(9, 1), key="ImgShrinking")],
    # [],
    # [sg.HSeparator()],
    # [sg.Button("Test ", size=(9, 1), key="ImgTest"),
    #  sg.Button("Tes2", size=(9, 1), key="ImgTest2"),
    #  sg.Button("Tes3", size=(9, 1), key="ImgTest3"),
    #  sg.Button("Tes4", size=(9, 1), key="ImgTest4"),],
    [sg.Button("ImgMean", size=(
        12, 1), key="ImgMean"), sg.Button("ImgMedianFilter", size=(
            12, 1), key="ImgMedianFilter"), ],
    [sg.Button("ImgMinFillter", size=(9, 1), key="ImgMinFilter"),
     sg.Button("ImgMaxFillter", size=(9, 1), key="ImgMaxFilter"), ],

    # [sg.Button("ImgEclipse", size=(12, 1), key="ImgEclipse"),
    #  sg.Button("ImgDiamond", size=(
    #      12, 1), key="ImgDiamond"),
    #  ],
    # [sg.Button("ImgSoalWajib", size=(12, 1), key="ImgEclipse"),
    #  sg.Button("ImgSoalBonus", size=(
    #      12, 1), key="ImgDiamond"),
    #  ],
    [

    ],
    # [sg.Button("Flip2Image", size=(12, 1), key="ImgFlip2Image"),
    #  sg.Button("Negative Triangle", size=(12, 1), key="ImgTest5"), ],
    # [

    #     sg.Button("Blendsmall", size=(12, 1), key="ImgBlendsmall"),
    #     sg.Button("Blendsmall270", size=(12, 1), key="ImgBlendsmall270"), ],

    # [sg.Button("Blendsmall270flip", size=(
    #     12, 1), key="ImgBlendsmall270flip"),
    #     sg.Button("Flip2Imagerotate", size=(
    #         12, 1), key="ImgFlip2Imagerotate"),
    #     sg.Button("TmgTriangle", size=(
    #         12, 1), key="ImgTriangle"),
    #  ],
    # [sg.Text("x : "), sg.In(size=(9, 1),
    #                         enable_events=True, key="inputAxisX"), ],
    # [sg.Text("y : "), sg.In(size=(9, 1),
    #                         enable_events=True, key="inputAxisY"), ],
    # [sg.Button("Submit", size=(20, 1), key="ImgTranslation")],

    [sg.HSeparator()],
    [sg.Button("WeightMeanF", size=(10, 1), key="WeightMeanFilter"),
     sg.Button("GradientF", size=(10, 1), key="GradienFilter"),
     sg.Button("CenterDifF", size=(10, 1), key="CenterDifFilter"),
     ],
    [sg.HSeparator()],
    [sg.Button("SobelF", size=(10, 1), key="SobelFilter"),
     sg.Button("PrewittF", size=(10, 1), key="PrewittFilter"),
     sg.Button("RobertF", size=(10, 1), key="RobertFilter"),
     ],
    [sg.Button("LaplacianF", size=(10, 1), key="LaplacianFilter"),

     ],
    [sg.HSeparator()],
    [sg.Button("ErosionF", size=(10, 1), key="ErosionFilter"),
     sg.Button("DilationF", size=(10, 1), key="DilationFilter"),

     ],
    [sg.Button("OpeningF", size=(10, 1), key="OpeningFilter"),
     sg.Button("ClosingF", size=(10, 1), key="ClosingFilter"),

     ],
    [sg.Button("WhiteTopHatF", size=(10, 1), key="WhiteTopHatFilter"),
     sg.Button("BlackTopHatF", size=(10, 1), key="BlackTopHatFilter"),

     ],



]

# membuat kolom area 4 : area viewer image output
image_viewer_column2 = [
    [sg.Text("Image Output:")],
    [sg.Text(size=(40, 1), key="ImgProcessingType")],
    [sg.Image(key="ImgOutputViewer")],
]

# menggabungkan keempat kolom area
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(image_viewer_column),
        sg.VSeparator(),
        sg.Column(list_processing),
        sg.VSeparator(),
        sg.Column(image_viewer_column2),
    ]
]


# run windows atau tampilan ui
window = sg.Window("Mini Image Editor", layout)
# nama image file temporary setiap kali processing output
filename_out = "out.png"
