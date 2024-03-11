"""PyAudio Example: Play a wave file."""

import wave
import sys
import os
from config import config_from_json

import pyaudio

HOME = os.getenv("HOME")
chime = config_from_json(HOME + "/.QtTimer", read_from_file=True)
CHUNK = 1024

def play_chime():

    with wave.open(HOME + chime.file, 'rb') as wf:
        # Instantiate PyAudio and initialize PortAudio system resources (1)
        p = pyaudio.PyAudio()

        # Open stream (2)
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        # Play samples from the wave file (3)
        while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
            stream.write(data)

        # Close stream (4)
        stream.close()

        # Release PortAudio system resources (5)
        p.terminate()
