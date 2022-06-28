import os
from pygame import mixer
path="music"
files = os.listdir(path)
print(files)
index=0
mixer.init()
mixer.music.load('music/' + files[index])
print("Press any key to start the music script")
os.system("pause >nul")
mixer.music.play(start=31)

while True: 
  
    print("Press 'n' to play the next song, 'p' to play previous song") 
    print("Press 'e' to exit the program") 
    query = input("  ") 
  
    if query == 'n': 
        # Playing next song
        mixer.music.fadeout(3000)
        index += 1
        mixer.music.load('music/' + files[index])
        mixer.music.play()        
    elif query == 'p': 
        # Playing previous song
        mixer.music.stop()
        index -= 1
        mixer.music.load('music/' + files[index])
        mixer.music.play() 
    elif query == 'e': 
        # Stop the mixer 
        mixer.music.stop() 
        exit()