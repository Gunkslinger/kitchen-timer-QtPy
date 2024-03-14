"""From: PyAudio Example: Play a wave file.
Gets audio file.wav to be played from user 
config file .QtTimer (JSON) in their home
directory and plays it.
"""

import wave
import pyaudio
from kitchen_timer_config import KitchenTimerConfig

CHUNK = 1024


def play_chime():
    """
    Get the chime filename for the user's config file and play it
    """
    k = KitchenTimerConfig()
    kchime = k.get_chime_wav() # location

    with wave.open(kchime, "rb") as wf:
        # Instantiate PyAudio and initialize PortAudio system resources (1)
        pa = pyaudio.PyAudio()

        # Open stream (2)
        stream = pa.open(
            format=pa.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True,
        )

        # Play samples from the wave file (3)
        while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
            stream.write(data)

        # Close stream (4)
        stream.close()

        # Release PortAudio system resources (5)
        pa.terminate()


#play_chime() # for testing
