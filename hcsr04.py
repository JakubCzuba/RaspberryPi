from gpiozero import DistanceSensor
from time import sleep

hcsr04 = DistanceSensor(echo= 5, trigger= 7)

try:
    while True:
        distance = hcsr04.distance * 100
        sleep(0.5)
        if distance >= 50:
            print("Pozostała karma: 100%")
        elif distance >= 45:
            print("Pozostała karma: 90%")
        elif distance >= 40:
            print("Pozostała karma: 80%")
        elif distance >= 35:
            print("Pozostała karma: 70%")
        elif distance >= 30:
            print("Pozostała karma: 60%")
        elif distance >= 25:
            print("Pozostała karma: 50%")
        elif distance >= 20:
            print("Pozostała karma: 40%")
        elif distance >= 15:
            print("Pozostała karma: 30%")
        elif distance >= 10:
            print("Pozostała karma: 20%")
        elif distance >= 5:
            print("Pozostała karma: 10%")
        else:
            print("Pusty pojemnik!!!")
except Exception:
    print("Error XD", Exception)

