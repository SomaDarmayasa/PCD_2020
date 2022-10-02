import PySimpleGUI as sg

# membuat kolom area 1 : membuka folder dan memilih image


# definisi masing-masing kolom area
# key = membutuhkan data sudah diinputkan dikomponen tersebut
sg.theme("DarkPurple1")
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
    [sg.Button("Image Negative", size=(20, 1), key="ImgNegative")],
    [sg.Button("Image Rotate", size=(20, 1), key="ImgRotate")],
    [sg.Button("Image Brightness", size=(20, 1), key="ImgBrightness")],
    [sg.Button("Image Blending", size=(20, 1), key="ImgBlending")],
    [sg.Button("Image Logaritmic", size=(20, 1), key="ImgLogaritmic")],
    [sg.Button("Image Power law", size=(20, 1), key="ImgPowerLaw")],

    [sg.HSeparator()],
    [sg.Text("Image Brightness Slider:"),




     ],
    [  # slider brightness
        sg.Slider(range=(-255, 255), size=(19, 20),
                  orientation='h',
                  key="SliderBrightness",
                  default_value=0), ],
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
