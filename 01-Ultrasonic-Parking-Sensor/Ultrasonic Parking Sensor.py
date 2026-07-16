from machine import Pin,PWM,time_pulse_us
import time

rl = Pin(4, Pin.OUT)
yl = Pin(2, Pin.OUT)
gl = Pin(15, Pin.OUT)

buzzer = PWM(Pin(5))
buzzer.freq(1000)

trig = Pin(19, Pin.OUT)
echo = Pin(18, Pin.IN)

def dist():
    trig.off()
    time.sleep_us(2)
    trig.on()
    time.sleep_us(10)
    trig.off()

    duration = time_pulse_us(echo, 1)

    distance = (duration * 0.0343) / 2

    if distance == 0:
        return None
    
    return distance


while True:
    distance = dist()

    if distance is None:
        continue
    
    rl.off()
    yl.off()
    gl.off()
    buzzer.duty(0)

    if distance >= 50 :
        gl.on()

    elif 20 <= distance < 50:
        yl.on()

        buzzer.duty(512)
        time.sleep(0.3)
        buzzer.duty(0)
        time.sleep(0.3)
        

    elif distance < 20 and distance >= 0:
        rl.on()
        buzzer.duty(512)

    else:
        print("!!!!!")


