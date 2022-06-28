import os
from pygame import mixer
path="music"
files = os.listdir(path)
print(files)
index=0
os.system("pause")
mixer.init()
mixer.music.load('music/' + files[index])
mixer.music.play(start=31)
os.system("pause")
mixer.music.fadeout(3000)
index += 1
mixer.music.load('music/' + files[index])
mixer.music.play()
os.system("pause")