from gpiozero import Angularsevo
from time import sleep

servo = Angularsevo(3,  min_pulse_width=0.0006, max_pulse_width=0.0023, )

while (True):
    servo.angle = 90
    sleep(2)
    servo.angle = 0
    sleep(2)
    servo.angle = -90
    