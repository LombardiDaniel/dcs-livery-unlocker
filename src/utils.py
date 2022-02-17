import os

from glob import glob

def check_saved_games(saved_games_dcs_dir):
    for folder_name in os.listdir(saved_games_dcs_dir):
        if folder_name in ('DCS', 'DCS.openbeta'):
            return True

    return False

class Utils:
    def __init__(self):
        self.dcs_dir = ''
        self.saved_games_dcs_dir = ''
        # self.window = ui_window

    @staticmethod
    def comment_out_countries_restriction(file_path):
        '''
        '''

        print(f'Unlocking: {file_path}')

        lines = []
        with open(file_path, 'r', encoding='UTF-8') as file:
            lines = file.readlines()

        open_flag = False
        for i, line in enumerate(lines):
            if 'countries = {' in line and '}' in line: # Single-line comment
                lines[i] = f'-- {line}'

            if 'countries = {' in line and '}' not in line: # Opening Line of block
                open_flag = True
                print(f'Unlocking: {file_path}')
                lines[i] = f'-- {line}'

            if open_flag and '}' not in line: # Center of block
                lines[i] = f'-- {line}'

            if open_flag and '}' in line: # End of block
                open_flag = False
                lines[i] = f'-- {line}'

        with open(file_path, 'w', encoding='UTF-8') as f:
            f.writelines(lines)


    def ready(self):
        return self.dcs_dir != '' and self.saved_games_dcs_dir != ''


    def fix_default_liveries(self):

        CORE_MODS_GLOB_STR = os.path.join(self.dcs_dir, 'CoreMods/aircraft/**/Liveries/**/**/*.lua')

        for file_path in glob(CORE_MODS_GLOB_STR):
            if 'Pack\Liveries' not in file_path:
                self.comment_out_countries_restriction(file_path)


    def fix_downloaded_liveries(self):

        SAVED_GAMES_LIVERIES = os.path.join(self.saved_games_dcs_dir, '?iveries/**/*.lua')

        for file_path in glob(SAVED_GAMES_LIVERIES):
            self.comment_out_countries_restriction(file_path)


    def fix_mods_liveries(self):

        SAVED_GAMES_MODS_LIVERIES = os.path.join(self.saved_games_dcs_dir, '?ods/aircraft/**/Liveries/**/*.lua')

        for file_path in glob(SAVED_GAMES_LIVERIES):
            if 'Pack\Liveries' not in file_path:
                self.comment_out_countries_restriction(file_path)


    def fix_bazar_liveries(self):

        CORE_MODS_GLOB_STR = os.path.join(self.dcs_dir, 'Bazar/Liveries/**/**/*.lua')

        for file_path in glob(CORE_MODS_GLOB_STR):
            self.comment_out_countries_restriction(file_path)


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
