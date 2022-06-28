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
print(f"Now playing: {files[index]}")
mixer.music.play(start=int(files[index][:len(files[index])-4].split("-")[1]))

while True: 
  
    print("Press 'n' to play the next song, 'p' to play previous song") 
    print("Press 'e' to exit the program") 
    query = input("  ") 
  
    if query == 'n': 
        # Playing next song
        mixer.music.fadeout(3000)
        index += 1
        mixer.music.load('music/' + files[index])
        print(f"Now playing: {files[index]}")
        mixer.music.play(start=int(files[index][:len(files[index])-4].split("-")[1]))        
    elif query == 'p': 
        # Playing previous song
        mixer.music.stop()
        index -= 1
        mixer.music.load('music/' + files[index])
        print(f"Now playing: {files[index]}")
        mixer.music.play(start=int(files[index][:len(files[index])-4].split("-")[1])) 
    elif query == 'e': 
        # Stop the mixer 
        mixer.music.stop() 
        exit()