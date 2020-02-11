import time

def print_one_line(hours,minutes,seconds,fraction):
    if hours<10:
        hours=('0'+str(hours))
    if minutes<10:
        minutes=('0'+str(minutes))
    if seconds<10:
         seconds=('0'+str(seconds))
    clock=(str(hours)+':'+str(minutes)+':'+str(seconds)+'.'+str(fraction))
    print(clock)


def clock(hours,minutes,seconds,fraction):
    while True:
        print_one_line(hours,minutes,seconds,fraction)
        fraction+=1
        time.sleep(.1)
        if fraction==10:
            fraction=0
            seconds+=1
        if seconds==60:
            seconds=0
            minutes+=1
        if minutes==60:
            minutes=0
            hours+=1
def question4():
    clock(0,1,2,3)
    
