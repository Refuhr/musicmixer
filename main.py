import os
from pygame import mixer
mixer.init()
mixer.music.load('music/test.mp3')
mixer.music.play(start=31)
print("End")
os.system("pause")
mixer.music.fadeout(3000)
os.system("pause")