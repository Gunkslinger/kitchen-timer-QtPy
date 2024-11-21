''' custom style confuguration code
'''
from pathlib import Path
from config import config_from_json

class KitchenTimerConfig():
    '''Kitchen timer config class
    '''

    def __init__(self):
        self.p = Path.home()
        self.home = f"{self.p}/"
        self.conf = config_from_json(self.home + ".QtTimer", read_from_file=True)

    def get_chime_wav(self) -> str:
        '''get alert wav file from the conf file
        '''
        chimewav = self.home + self.conf.file
        return chimewav

    def get_timer_qss(self) -> str:
        ''' get the style sheet from the conf file
        '''
        qss = self.home + self.conf.qss
        return qss

    def get_timer_presets(self) -> str:
        ''' get the presets file path from the conf file
        '''
        presets = self.home + self.conf.presets
        return presets
