from microbit import *


display.show(Image.HAPPY)

while True:
    if button_a.is_pressed():
        display.scroll("Hello, AHL")
    elif button_b.is_pressed():
        display.show(Image.HEART)
    elif accelerometer.is_gesture("shake"):
        display.show(Image.SKULL)
