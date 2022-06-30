# musicmixer  
This application is used to play small clips of music for an event. The songs fade out at command and the next song for the next person can be started. 
# Usage
```
python3 main.py
```
or:  
```
python main.py
```
put the files to be played in a directory of your choice (default:music). Can be changed in main.py in line 6.
files should be named: \[number]\_\[lastname]\_\[firstname]-\[start time(in seconds)].[music file extension (ogg recommended)] example: 002_Mustermann_Max-21.ogg  
The rest of the program is self explanatory.  
# Features  
-pause/play  
-previous song  
-next song  
-jump to specific song by lastname  
-change volume
