def on_gesture_shake():
    music.stop_all_sounds()
    led.stop_animation()
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_sound_loud():
    music.ring_tone(262)
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
    """)
    basic.clear_screen()
    basic.show_string("Stop Prosim")
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_forever():
    pass
basic.forever(on_forever)
