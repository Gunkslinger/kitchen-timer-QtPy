from pathlib import Path
from config import config_from_json


class KitchenTimerConfig():

    def __init__(self):
        self.p = Path.home()
        self.HOME = f"{self.p}"
        self.conf = config_from_json(self.HOME + "/.QtTimer", read_from_file=True)

    def get_chime_wav(self) -> str:

        self.chimeWav = self.HOME + self.conf.file
        #print(self.chimeWav)
        return(self.chimeWav)

    def get_timer_qss(self) -> str:
        
        self.qss = self.HOME + self.conf.qss
        #print(self.qss)
        return(self.qss)

k = KitchenTimerConfig()
k.get_chime_wav()
k.get_timer_qss()