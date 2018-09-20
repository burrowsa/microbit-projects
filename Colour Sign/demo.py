from microbit import *
import neopixel
from random import randint


def shift_up(np):
    for pixel_id in range(len(np) - 1, 0, -1):
        np[pixel_id] = np[pixel_id - 1]
    return 0


def shift_down(np):
    for pixel_id in range(0, len(np) - 1, +1):
        np[pixel_id] = np[pixel_id + 1]
    return -1


def rotate_up(np):
    tmp = np[-1]
    shift_up(np)
    np[0] = tmp


def random_pixel():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return (red, green, blue)


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


modes = []


def register(cls):
    modes.append(cls)
    return cls


@register
class Random:
    @staticmethod
    def init(np):
        for_each_pixel(np, random_pixel)
    
    @staticmethod
    def step(np):
        for_each_pixel(np, random_pixel)


class RandomShiftUp(Random):
    @classmethod
    def step(cls, np):
        np[cls.shift(np)] = random_pixel()

    @staticmethod
    def shift(np):
        return shift_up(np)
        

@register
class RandomShiftDown(RandomShiftUp):
    @staticmethod
    def shift(np):
        return shift_down(np)


@register
class ScrollRed:
    @staticmethod
    def init(np):
        for_each_pixel(np, off)
        np[0] = (255, 0, 0)
    
    @staticmethod
    def step(np):
        rotate_up(np)


if __name__ == "__main__":
    # Setup the Neopixel strip on pin0 with a length of pixels
    np = neopixel.NeoPixel(pin0, 5)

    while True:
        for mode in modes:
            run(np, mode)
