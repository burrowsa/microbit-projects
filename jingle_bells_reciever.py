import radio
import music


radio.on()



JINGLE_BELLS = ["E:2","E:2","E:4","E:2","E:2","E:4","E:2","G:2","C:2","D:1","E:8",
                "F:2","F:2","F:4","F:1","F:2","E:2","E:2",
                "E:1","E:1","E:2","D:2","D:2","E:2","D:4","G:4",
                "E:2","E:2","E:4","E:2","E:2","E:4","E:2","G:2","C:2","D:1","E:8",
                "F:2","F:2","F:4","F:1","F:2","E:2","E:2",
                "E:1","E:1","G:2","G:2","F:2","D:2","C:8"]


while True:
    incoming = radio.receive()
    if incoming == 'play':
        music.play(JINGLE_BELLS)
