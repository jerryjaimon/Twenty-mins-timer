#!/usr/bin/env python3  
import time
import sys
import notify2
from playsound import playsound
from beepy import beep
notify2.init('foo')
print("Start(Y/N):")

str=input()
mins=0
if str[0]=='Y':
    n=notify2.Notification("Started!")
    n.show()
    while mins!=20:      
        time.sleep(60)
        mins+=1
    n=notify2.Notification("Take Break.20 mins up!")
    n.show()
    beep(sound=4)
    sys.exit(0)

else:
    sys.exit(0)
