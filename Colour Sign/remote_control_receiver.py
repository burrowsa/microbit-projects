from microbit import *
import neopixel
import radio


def hsv_to_rgb(h, s, v):
    """Taken from https://github.com/python/cpython/blob/3.7/Lib/colorsys.py and tweaked a bit"""
    h = (h % 360) / 360
    if s == 0.0:
        return int(v * 255), int(v * 255), int(v * 255)
    i = int(h*6.0)
    f = (h*6.0) - i
    p = v*(1.0 - s)
    q = v*(1.0 - s*f)
    t = v*(1.0 - s*(1.0-f))
    i = i%6
    if i == 0:
        return int(v * 255), int(t * 255), int(p * 255)
    if i == 1:
        return int(q * 255), int(v * 255), int(p * 255)
    if i == 2:
        return int(p * 255), int(v * 255), int(t * 255)
    if i == 3:
        return int(p * 255), int(q * 255), int(v * 255)
    if i == 4:
        return int(t * 255), int(p * 255), int(v * 255)
    if i == 5:
        return int(v * 255), int(p * 255), int(q * 255)
    # Cannot get here


def set_colour(h):
    rgb = hsv_to_rgb(h, 1, 0.5)
    for i in range(len(np)):
        np[i] = rgb
    np.show()


if __name__ == "__main__":
    # Setup the Neopixel strip on pin0 with a length of pixels
    np = neopixel.NeoPixel(pin0, 5)

    radio.on()

    h = 180
    set_colour(h)
    while True:
        incoming = radio.receive()
        if incoming == 'increment':
            h = (h + 5) % 360
        elif incoming == 'decrement':
            h = (h - 5) % 360
        
        if incoming is not None:
             set_colour(h)
