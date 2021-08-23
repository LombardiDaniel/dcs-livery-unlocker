import os

def check_saved_games(saved_games_dir):
    for folder_name in os.listdir(saved_games_dir):
        if folder_name in ('DCS', 'DCS.openbeta'):
            return True
            
    return False

class Utils:
    def __init__(self):
        self.dcs_dir = ''
        self.saved_games_dir = ''
        # self.window = ui_window

    def ready(self):
        return self.dcs_dir != '' and self.saved_games_dir != ''

    def fix_default_liveries(self):

        aircrafts_dir = os.path.join(self.dcs_dir, 'CoreMods', 'aircraft')

        for aircraft_name in os.listdir(aircrafts_dir):
            if not aircraft_name.endswith('Pack'):
                aircraft_liveries_dir = os.path.join(aircrafts_dir, aircraft_name, 'Liveries')

                if os.path.isdir(aircraft_liveries_dir):
                    for arcraft_var_name in os.listdir(aircraft_liveries_dir):
                        arcraft_var_dir = os.path.join(aircraft_liveries_dir, arcraft_var_name)

                        if os.path.isdir(arcraft_var_dir):
                            for livery_name in os.listdir(arcraft_var_dir):
                                description_lua_path = os.path.join(arcraft_var_dir, livery_name, 'description.lua')
                                if os.path.isfile(description_lua_path):
                                    lines = []

                                    print(description_lua_path)

                                    with open(description_lua_path, 'r', encoding='utf-8') as f:
                                        lines = f.readlines()

                                    for i, line in enumerate(lines):
                                        if 'countries = {' in line:
                                            print('BINGO')
                                            lines[i] = line.replace('countries = {', '-- countries = {')

                                    with open(description_lua_path, 'w', encoding='utf-8') as f:
                                        f.writelines(lines)


    def fix_mods_liveries(self, openbeta):

        dcs_folder_name = 'DCS.openbeta' if openbeta else 'DCS'

        aircrafts_dir = os.path.join(self.saved_games_dir, dcs_folder_name, 'mods', 'aircraft')

        if os.path.isdir(aircrafts_dir):
            for aircraft_name in os.listdir(aircrafts_dir):
                if not aircraft_name.endswith('Pack'):
                    aircraft_liveries_dir = os.path.join(aircrafts_dir, aircraft_name, 'Liveries')

                    if os.path.isdir(aircraft_liveries_dir):
                        for arcraft_var_name in os.listdir(aircraft_liveries_dir):
                            arcraft_var_dir = os.path.join(aircraft_liveries_dir, arcraft_var_name)

                            if os.path.isdir(arcraft_var_dir):
                                for livery_name in os.listdir(arcraft_var_dir):
                                    description_lua_path = os.path.join(arcraft_var_dir, livery_name, 'description.lua')
                                    if os.path.isfile(description_lua_path):
                                        lines = []

                                        print(description_lua_path)

                                        with open(description_lua_path, 'r', encoding='utf-8') as f:
                                            lines = f.readlines()

                                        for i, line in enumerate(lines):
                                            if 'countries = {' in line:
                                                print('BINGO')
                                                lines[i] = line.replace('countries = {', '-- countries = {')

                                        with open(description_lua_path, 'w') as f:
                                            f.writelines(lines)

    def fix_downloaded_liveries(self, openbeta):

        dcs_folder_name = 'DCS.openbeta' if openbeta else 'DCS'

        liveries_dir = os.path.join(self.saved_games_dir, dcs_folder_name, 'Liveries')

        if os.path.isdir(liveries_dir):
            for aircraft_name in os.listdir(liveries_dir):
                if not aircraft_name.endswith('Pack'):
                    aircraft_liveries_dir = os.path.join(liveries_dir, aircraft_name)

                    if os.path.isdir(aircraft_liveries_dir):
                        if os.path.isdir(aircraft_liveries_dir):
                            for livery_name in os.listdir(aircraft_liveries_dir):
                                description_lua_path = os.path.join(aircraft_liveries_dir, livery_name, 'description.lua')
                                if os.path.isfile(description_lua_path):
                                    lines = []

                                    print(description_lua_path)

                                    with open(description_lua_path, 'r', encoding='utf-8') as f:
                                        lines = f.readlines()

                                    for i, line in enumerate(lines):
                                        if 'countries = {' in line and '--' not in line:
                                            print('BINGO')
                                            lines[i] = line.replace('countries = {', '-- countries = {')
                                            print(lines[i])

                                    with open(description_lua_path, 'w') as f:
                                        f.writelines(lines)


class Notifier:
    '''
    Notifications wrapper
    '''
    def __init__(self, window):
        self.window = window
        self.buffer = ''

    def notify(self, msg):
        '''
        Writes notification to the notifications area.
        '''
        self.window['-NOTIFICATIONS-'].update(visible=True)
        self.window['-NOTIFICATIONS-'].update(value=msg)
        self.buffer = msg

    def add(self, msg):
        '''
        Adds a notification to the notifications area.
        '''
        self.window['-NOTIFICATIONS-'].update(visible=True)
        self.window['-NOTIFICATIONS-'].update(value=self.buffer + msg)
        self.buffer += msg

    def clear(self):
        '''
        Clears the notifications area.
        '''
        self.window['-NOTIFICATIONS-'].update(value='')
        self.window['-NOTIFICATIONS-'].update(visible=False)
        self.buffer = ''
