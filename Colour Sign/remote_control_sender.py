import radio
from microbit import *

radio.on()

# Event loop.
while True:
    if button_a.was_pressed():
        radio.send('decrement')
    elif button_b.was_pressed():
        radio.send('increment')
