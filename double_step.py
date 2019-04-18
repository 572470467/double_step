import RPi.GPIO as GPIO
import threading
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
a=[4,17,27,18]
b=[22,23,24,25]
for t in a,b:
    GPIO.setup(t,GPIO.OUT)
def step_a(nsa,dia,t):
    arr_a=[0,1,2,3];
    if dia!=1:
        arr_a=[3,2,1,0];
    for i in range(0,int(nsa/100)):
        for x in arr_a:
            time.sleep((t/4)/nsa)
            for j in range(0,4):
                if j==x:
                    GPIO.output(a[j],True)
                else:
                    GPIO.output(a[j],False)
def step_b(nsb,dib,t):
    arr_b=[0,1,2,3];
    if dib!=1:
        arr_b=[3,2,1,0];
    for i in range(0,int(nsb/100)):
        for v in arr_b:
            time.sleep((t/4)/nsb)
            for j in range(0,4):
                if j==v:
                    GPIO.output(b[j],True)
                else:
                    GPIO.output(b[j],False)
def double_step(nsa,dia,nsb,dib,t):
    count=0
    while True:
        step_a(nsa,dia,t)
        step_b(nsb,dib,t)
        count+=int(nsa/100)
        if count>=nsa:
            break
if __name__ == '__main__':
    double_step(256,1,128,1,5)

