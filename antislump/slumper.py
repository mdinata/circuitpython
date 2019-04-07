from adafruit_circuitplayground.express import cpx
import time

cpx.pixels.brightness=0.02
count=2
flag=1

def press():
    global count, flag
    if cpx.button_a:
        count +=1
        flag=1
    elif cpx.button_b  :
        count -= 1
        flag=0
    neopix(count,flag)
    return count

def neopix(cnt,flg):
    
    if (6 >= cnt >= 2) and flg == 1:
        if cnt ==2:
            cpx.pixels[0]=(0,255,255)
            cpx.pixels[9]=(0,255,255)        
        if cnt == 3:
            cpx.pixels[1]=(255,255,0)
            cpx.pixels[8]=(255,255,0)
        if cnt == 4:
            cpx.pixels[2]=(0,0,255)
            cpx.pixels[7]=(0,0,255)        
        if cnt == 5:
            cpx.pixels[3]=(0,255,0)
            cpx.pixels[6]=(0,255,0)         
        if cnt == 6:
            cpx.pixels[4]=(255,0,0)
            cpx.pixels[5]=(255,0,0)
    
    if (6 >= cnt >= 1) and flg == 0:
        if cnt == 1:
            cpx.pixels[0]=(0,0,0)
            cpx.pixels[9]=(0,0,0) 
        if cnt == 2:
            cpx.pixels[1]=(0,0,0)
            cpx.pixels[8]=(0,0,0)              
        if cnt == 3:
            cpx.pixels[2]=(0,0,0)
            cpx.pixels[7]=(0,0,0)       
        if cnt == 4:
            cpx.pixels[3]=(0,0,0)
            cpx.pixels[6]=(0,0,0)        
        if cnt == 5:
            cpx.pixels[4]=(0,0,0)
            cpx.pixels[5]=(0,0,0)
    
    return cnt
    

def beep():
    for i in range(2):
        cpx.start_tone(888)
        time.sleep(0.1)
        cpx.stop_tone()
        time.sleep(0.1)

while True:
    sensitivity=press()
    x,y,z=cpx.acceleration
    print(sensitivity,z)
    if z >= sensitivity:
        beep()
    time.sleep(0.1)
