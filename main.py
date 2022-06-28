import os
from pygame import mixer
path="music"
files = os.listdir(path)
print(files)
index=0
mixer.init()
mixer.music.load('music/' + files[index])
print(f"About to play: {files[index]}")
print("Press any key to start the music script")
os.system("pause >nul")
print(f"Now playing: {files[index]}")
mixer.music.play(start=int(files[index][:len(files[index])-4].split("-")[1]))

while True: 
  
    print("Press 'n' to play the next song, 'p' to play previous song, 'o' to manually overwrite to a specific song") 
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
    elif query == 'o': 
        # Jump to specific song
        print("Type in the lastname: ")
        overwrite = input()
        #print(override)
        try:
            for i in files:
                if i[4:-1].split("_")[0] == overwrite:
                    print(i)
                    index = files.index(i)
        except :
            print("Name could not be found!")
            stop = True
        if stop:
            mixer.music.fadeout(500)
            mixer.music.load('music/' + files[index])
            print(f"Now playing: {files[index]}")
            mixer.music.play(start=int(files[index][:len(files[index])-4].split("-")[1]))
    elif query == 'e': 
        # Stop the mixer 
        mixer.music.stop() 
        exit()