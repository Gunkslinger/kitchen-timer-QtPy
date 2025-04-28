#MIT License

# Copyright (c) 2024 GunkSlinger

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

''' custom style confuguration code
'''

# This file is in the public domain -- author Gunkslinger@github.com 2024

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
