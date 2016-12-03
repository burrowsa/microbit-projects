from microbit import button_a
import music


JINGLE_BELLS = ["E:2","E:2","E:4","E:2","E:2","E:4","E:2","G:2","C:2","D:1","E:8",
                "F:2","F:2","F:4","F:1","F:2","E:2","E:2",
                "E:1","E:1","E:2","D:2","D:2","E:2","D:4","G:4",
                "E:2","E:2","E:4","E:2","E:2","E:4","E:2","G:2","C:2","D:1","E:8",
                "F:2","F:2","F:4","F:1","F:2","E:2","E:2",
                "E:1","E:1","G:2","G:2","F:2","D:2","C:8"]


def wait_for_button_a():
    while True:
        if button_a.is_pressed():
            break


while True:
    music.play(JINGLE_BELLS)
    wait_for_button_a()
