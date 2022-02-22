from microbit import *
import music

while True:
    display.show('RICKROLL')
    music.play(['c#5:6','d#5:4','g#4:4',
                'd#5:6','f5:4','g#5:1','f#5:1','f5:2',
                'c#5:6','d#5:4','g#4:8',])
