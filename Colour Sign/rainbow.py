from microbit import *
import neopixel
from random import randint


def shift_up(np):
    for pixel_id in range(len(np) - 1, 0, -1):
        np[pixel_id] = np[pixel_id - 1]
    return 0


def rotate_up(np):
    tmp = np[-1]
    shift_up(np)
    np[0] = tmp


def for_each_pixel(np, fn):
    for pixel_id in range(0, len(np)):
        np[pixel_id] = fn()


def off():
    return 0, 0, 0


def sleep_or_button(time):
    for _ in range(time / 10):
        if pin1.read_digital() or button_a.is_pressed() or button_b.is_pressed():
            return True
        sleep(10)
    return False


def run(np, fn):
    fn.init(np)
    while True:
        np.show()
        if sleep_or_button(500):
            break
        fn.step(np)

    for_each_pixel(np, off)
    np.show()
    sleep(500)


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


modes = []


def register(cls):
    modes.append(cls)
    return cls


@register
class RainbowScrollUp:
    @staticmethod
    def init(np):
        step = 360 // len(np)
        for pixel_index in range(len(np)):
            np[pixel_index] = hsv_to_rgb(pixel_index * step, 1, 0.5)
    
    @staticmethod
    def step(np):
        rotate_up(np)


@register
class RainbowFade:
    @classmethod
    def init(cls, np):
        cls.h = 0
        for_each_pixel(np, lambda: hsv_to_rgb(cls.h, 1, 0.5))

    @classmethod
    def step(cls, np):
        for_each_pixel(np, lambda: hsv_to_rgb(cls.h, 1, 0.5))
        cls.h = (cls.h + 1) % 360


@register
class RainbowRoller:
    @classmethod
    def init(cls, np):
        cls.h = 0
        for pixel_id in range(0, len(np)):
            np[pixel_id] = hsv_to_rgb(cls.h, 1, 0.5)
            cls.h = (cls.h + 15) % 360

    @classmethod
    def step(cls, np):
        np[shift_down(np)] = hsv_to_rgb(cls.h, 1, 0.5)
        cls.h = (cls.h + 15) % 360


if __name__ == "__main__":
    # Setup the Neopixel strip on pin0 with a length of pixels
    np = neopixel.NeoPixel(pin0, 5)

    while True:
        for mode in modes:
            run(np, mode)
