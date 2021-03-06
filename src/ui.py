import PySimpleGUI as sg


layout = [
    [
        sg.Text("", size=(52, 1), key="-NOTIFICATIONS-", visible=False)
    ],
    [
        sg.Text('DCS Install Folder           '),
        sg.In(size=(30, 1), enable_events=True, key="-DCSDIR-"),
        sg.FolderBrowse()
    ],
    [
        sg.Text('SavedGames/DCS Folder'),
        sg.In(size=(30, 1), enable_events=True, key="-SAVEDGAMESDIR-"),
        sg.FolderBrowse()
    ],
    [
        sg.Button("UNLOCK LIVERIES", enable_events=True, key="-START-", visible=True),
    ],
]


class UI:

    sg.theme('Dark Teal 4')

    def __init__(self):
        self.window = sg.Window('DCS Liveries Nation Unlocker - v1.2.1', layout, icon='logo.ico')
