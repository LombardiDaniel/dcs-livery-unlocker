import os

import PySimpleGUI as sg

from ui import UI
from utils import Utils, Notifier, check_saved_games


def main():

    DEBUG = True

    ui = UI()
    utils = Utils()
    notifications = Notifier(ui.window)

    while True:
        menu_event, menu_values = ui.window.read(timeout=100)

        if menu_event != "__TIMEOUT__":
            notifications.clear()
            if DEBUG:
                print(f"LOG - MENU_ENVENT: {menu_event}")
                print(f"LOG - MENU_VALUES: {menu_values}")

        if menu_event == sg.WIN_CLOSED:
            break

        if menu_event == '-DCSDIR-':
            dcs_dir = menu_values['-DCSDIR-']
            if os.path.exists(dcs_dir) and (
                dcs_dir.endswith('DCS World') or dcs_dir.endswith('DCS World OpenBeta')
            ):
                utils.dcs_dir = dcs_dir
            else:
                notifications.add('DCS directory not found.')

        if menu_event == '-SAVEDGAMESDIR-':
            saved_games_dir = menu_values['-SAVEDGAMESDIR-']
            if os.path.exists(saved_games_dir) and check_saved_games(saved_games_dir):
                utils.saved_games_dir = saved_games_dir
            else:
                notifications.add('SavedGames directory not found.')

        if menu_event == '-START-':
            if utils.ready():
                notifications.clear()
                ui.window['-START-'].update(disabled=True)
                notifications.add('Working on it... ')

                print(utils.saved_games_dir, utils.dcs_dir)

                try:
                    utils.fix_default_liveries()
                    utils.fix_mods_liveries(openbeta=False)
                    utils.fix_mods_liveries(openbeta=True)
                    utils.fix_downloaded_liveries(openbeta=False)
                    utils.fix_downloaded_liveries(openbeta=True)

                    notifications.add('Done! You may close the program.')
                    ui.window['-START-'].update(disabled=False)
                except Exception as e:
                    notifications.add('Something went wrong.')
                    with open('dcs_nation_skin_unlocker.log', 'a+') as f:
                        f.write(e, encoding='utf-8')

            else:
                notifications.add('Paths not set.')


    ui.window.close()


if __name__ == '__main__':
    main()
