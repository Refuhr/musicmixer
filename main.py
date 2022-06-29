import os
from pygame import mixer



path="music"                #path/directory where the songs are located
fade_in=1000                #fade in time in ms
fade_out=3000               #fade out time in ms
volume=0.1                  #change the volume from 0.0 to 1.0
def help():
    print("""
    
███    ███ ██    ██ ███████ ██  ██████ ███    ███ ██ ██   ██ ███████ ██████  
████  ████ ██    ██ ██      ██ ██      ████  ████ ██  ██ ██  ██      ██   ██ 
██ ████ ██ ██    ██ ███████ ██ ██      ██ ████ ██ ██   ███   █████   ██████  
██  ██  ██ ██    ██      ██ ██ ██      ██  ██  ██ ██  ██ ██  ██      ██   ██ 
██      ██  ██████  ███████ ██  ██████ ██      ██ ██ ██   ██ ███████ ██   ██ 
    """)
    print("Press:\n'n' or 'enter' to play the next song\n'l' to play the last song\n'm' to manually jump to a specific song\n'p' to pause/play the music\n'r' to restart the current song\n'v' to change the volume") 
    print("'e' to exit the program\n") 

help()
files = os.listdir(path)
files.sort()
print(f"{files}\n")
index=0
exists = False
mixer.init()
mixer.music.set_volume(volume)

def play_song():
    mixer.music.unpause()
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
print(f"Press 'enter' to start the first song: {files[index]}, 'c' to continue without playing a song (start after that with 'l'), e to exit.")
start= input()
if start == "e":
    mixer.music.stop()
    print("Exiting...")
    exit()
elif start == "":
    play_song()
elif start == "c":
    help()

while True: 
    print("\nPress h for Help, e for exit.")
    if index+1 >= len(files):
        y = ""
    else:
        y = "Next song: " + files[index+1]
    if index > 0 and y != "":
        x = ", previous song: " + files[index-1]
    elif index > 0 and y == "":
        x = "Previous song: " + files[index-1]
    elif index == 0 and not exists:
        x = " Press 'l' to start with the first song: " + files[index] + " 'enter' to start with second one."
        exists = True
    else:
        x = ""
    print(f"{y}{x}")
    query = input() 
  
    if query == 'n' or query == '': 
        # Playing next song
        if index+1 >= len(files):
            print("Reached the end!")
            mixer.music.fadeout(fade_out)
        else:
            mixer.music.fadeout(fade_out)
            index += 1
            print(f"About to play: {files[index]}\n")
            print("Press enter to start the next song.")
            input()
            play_song()       
    elif query == 'l': 
        # Playing the last song
        if index-1 < 0:
            print("There is no song before that! Restarting current song...")
            play_song()
        else:
            mixer.music.fadeout(500)
            index -= 1
            play_song()
    elif query == 'm': 
        # manually jump to specific song
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
        print("Exiting...")
        exit()
    elif query == 'p': 
        # Pause/resume the music 
        if mixer.music.get_busy():
            mixer.music.pause()
            print("Pausing the music.")
        else:
            mixer.music.unpause()
            print("Resuming the music.")
    elif query == 'v': 
        # Change the volume
        print("Type a number from 0.0 to 1.0")
        check_float(input())
    elif query == 'h':
        # Print out help
        help()
    elif query == 'r':
        # Restarting the song
        play_song()
    else:
        print("Function could not be found, try 'h' for help.")