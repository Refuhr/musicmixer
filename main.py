import os
from pygame import mixer
import keyboard
import time



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
    print("Press:\n'n' to play the next song\n'l' to play the last song\n'm' to manually jump to a specific song\n'p' to pause/play the music\n'r' to restart the current song\n'v' to change the volume") 
    print("'e' to exit the program\n") 

help()
files = os.listdir(path)
files.sort()
print(f"{files}\n")
index=0
paused=False
starting=False
mixer.init()
mixer.music.set_volume(volume)

def play_song(fade_in):
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
print("Press enter to start the music script, e to exit.")
while not starting:
    try:
        if keyboard.is_pressed('e'):
            mixer.music.stop()
            print("Exiting...")
            exit()
        elif keyboard.is_pressed('enter'):
            starting=True
            play_song(fade_in)
    except:
        break

print("\nPress h for Help, e for exit.")
while True:
    try:
        if keyboard.is_pressed('n'): 
            # Playing next song
            if index+1 >= len(files):
                print("Reached the end!")
            else:
                mixer.music.fadeout(fade_out)
                index += 1
                print(f"About to play: {files[index]}\n")
                print("Press any key to start the next song.")
                input()
                play_song(fade_in)
            time.sleep(0.5)
        elif keyboard.is_pressed('l'): 
            # Playing the last song
            if index-1 < 0:
                print("There is no song before that!")
            else:
                mixer.music.fadeout(500)
                index -= 1
                play_song(fade_in)
            time.sleep(0.5)
        elif keyboard.is_pressed('m'): 
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
                play_song(fade_in)
            time.sleep(0.5)
        elif keyboard.is_pressed('e'):
            # Stop the mixer 
            mixer.music.stop()
            print("Exiting...")
            exit()
            break
        elif keyboard.is_pressed('p'): 
            # Pause/resume the music 
            if mixer.music.get_busy():
                mixer.music.pause()
                print("Pausing the music.")
            else:
                mixer.music.unpause()
                print("Resuming the music.")
            time.sleep(0.5)
        elif keyboard.is_pressed('v'): 
            # Change the volume
            time.sleep(0.5)
            print("Type a number from 0.0 to 1.0")
            time.sleep(0.5)
            check_float(input())
        elif keyboard.is_pressed('h'):
            # Print out help
            help()
            time.sleep(0.5)
        elif keyboard.is_pressed('r'):
            # Restarting the song
            play_song(fade_in)
            time.sleep(0.5)
    except:
        print("Function could not be found, try 'h' for help.")
        break
    time.sleep(0.05)
            