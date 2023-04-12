# run "pip install pysimplegui" command in terminal/console or command-line app
# run "python python_img_viewer.py" command

import PySimpleGUI as sg
import os.path

# window layout of two columns

# first column
file_list_column = [
    [
        sg.Text("Image Folder"),
        # "key" acts as id does in html/css, specific identifier to call back to.
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20),
            key="-FILE LIST-"
        )
    ],
]

# for now will only show the name of the chosen file

# second column
image_viewer_column = [
    [sg.Text("Choose an image from the list on the left:")],
    [sg.Text(size=(60, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

# ----- full layout ----- (controls how elements are laid out on screen)
layout = [
    [
        sg.Column(file_list_column),  # first column
        sg.VSeperator(),  # vertical separator
        sg.Column(image_viewer_column),  # second column
    ]
]

# creates window named "Image Viewer" with the layout defined in "layout"
window = sg.Window("Image Viewer", layout)

# event loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:  # if "Exit" button clicked or window closed, exit program
        break

    # Folder name fills in when selected, so now make a list of files
    if event == "-FOLDER-":  # call back to "sg.In" (selected folder)
        folder = values["-FOLDER-"]  # get values of images in selected folder
        try:
            # add values to list
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list

            # if the path is a file, add it to list
            if os.path.isfile(os.path.join(folder, f))

            # make sure the file extensions are lowercase, and search for png and gif files only.
            # PySimpleGUI only works with png and gif files.
            and f.lower().endswith((".png", ".gif"))
        ]

        # update file list in window
        window["-FILE LIST-"].update(fnames)

    elif event == "-FILE LIST-":  # if a file was chosen on left side of window
        try:
            # get chosen file
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )

            # display file path on right side
            window["-TOUT-"].update(filename)

            # display image on right side
            window["-IMAGE-"].update(filename=filename)
        except:
            pass

window.close()
