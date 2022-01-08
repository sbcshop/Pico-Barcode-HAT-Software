# run motor from here
from machine import Pin,PWM

led = Pin(25,Pin.OUT)#pico inbuilt led 
pwm = PWM(Pin(14))#connect motor to GPIO pin 14
pwm.freq(50)#frequency of pwm signal in which servo motor operate , not change this
pwm.duty_ns(600000)#initially mmotor at 0 degree

def on_servo():
    pwm.duty_ns(1500000)#motor at 180 degree
    led.value(1)#led on
    
def off_servo():
    pwm.duty_ns(600000)
    led.value(0)#led off