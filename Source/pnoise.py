import playsound
import threading
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def play_sound():  # plays the noise.mp3 sound on repeat
    while True:
        playsound.playsound("noise.mp3", True)


x = threading.Thread(target=play_sound)
x.start()
# starts thread to play the sound

while True:  # loops continuously setting the system volume to maximum
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(-0.0, None)
    time.sleep(1)