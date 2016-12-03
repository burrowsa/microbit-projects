import radio
from microbit import button_a, sleep


radio.on()


def wait_for_button_a():
    while True:
        if button_a.is_pressed():
            break


while True:
    wait_for_button_a()
    radio.send("play")
    sleep(500)
