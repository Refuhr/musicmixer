import os
from pygame import mixer



path="music"                #path/directory where the songs are located
fade_in=1000                #fade in time in ms
fade_out=3000               #fade out time in ms
volume=0.2                  #change the volume from 0.0 to 1.0

files = os.listdir(path)
files.sort()
print(f"{files}\n")
index=0
mixer.init()
mixer.music.set_volume(volume)

def play_song():
    mixer.music.load('music/' + files[index])
    print(f"Now playing: {files[index]}")
    mixer.music.play(start=int(files[index][:len(files[index])-4].split("-")[1]), fade_ms=fade_in)

def check_float(num):
    try:
        float(num)
        volume=float(num)
        mixer.music.set_volume(volume)
        print(f"Setting volume to: {mixer.music.get_volume()}.")
    except ValueError:
        print("Not a float try again!")

print(f"About to play: {files[index]}\n")
print("Press any key to start the music script")
input()
play_song()


while True: 
    print("""\
    
███    ███ ██    ██ ███████ ██  ██████ ███    ███ ██ ██   ██ ███████ ██████  
████  ████ ██    ██ ██      ██ ██      ████  ████ ██  ██ ██  ██      ██   ██ 
██ ████ ██ ██    ██ ███████ ██ ██      ██ ████ ██ ██   ███   █████   ██████  
██  ██  ██ ██    ██      ██ ██ ██      ██  ██  ██ ██  ██ ██  ██      ██   ██ 
██      ██  ██████  ███████ ██  ██████ ██      ██ ██ ██   ██ ███████ ██   ██ 
""")
    print("Press 'n' to play the next song, 'p' to play previous song, 'o' to manually overwrite to a specific song, 's' to stop/pause the music, 'r' to resume the music, v to change the volume") 
    print("Press 'e' to exit the program") 
    query = input("  ") 
  
    if query == 'n': 
        # Playing next song
        if index+1 >= len(files):
            print("Reached the end!")
        else:
            mixer.music.fadeout(fade_out)
            index += 1
            print(f"About to play: {files[index]}\n")
            print("Press any key to continue...")
            input()
            play_song()       
    elif query == 'p': 
        # Playing previous song
        if index-1 < 0:
            print("There is no song before that!")
        else:
            mixer.music.fadeout(500)
            index -= 1
            play_song()
    elif query == 'o': 
        # Jump to specific song
        print("Type in the lastname: ")
        overwrite = input()
        index_old = index
        for i in files:
            if i[4:-1].split("_")[0] == overwrite:
                print(i)
                index = files.index(i)
        if index_old == index:
            print(f"The name: '{overwrite}' could not be found!")
            
        else:
            print(f"Switching to '{files[index]}'.")
            mixer.music.fadeout(500)
            play_song()
    elif query == 'e': 
        # Stop the mixer 
        mixer.music.stop() 
        exit()
    elif query == 's': 
        # Pause the music 
        mixer.music.pause() 
    elif query == 'r': 
        # Resume the music
        mixer.music.unpause()
    elif query == 'v': 
        # Change the volume
        print("Type a number from 0.0 to 1.0")
        check_float(input())