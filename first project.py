#alarm can be ring in this you give a second to be start
from playsound import playsound
import time
clear="\033[2J"
clearandreturn="\033[H"
def alarm(second):
    timer=0
    print(clear)
    while(timer<second):
        time.sleep(1)
        timer+=1
        timeleft=second-timer
        minuteleft=timeleft//60
        secondleft=timeleft%60
        print(f"{clearandreturn}{minuteleft:02d}:{secondleft:02d}")
    playsound("www.mp3")
min=int(input("enter the minute  "))
sec=int(input("enter the second to set timer  "))
allsec=(min*60)+sec
alarm(allsec)

