def on_gesture_wave():
    basic.show_number(0)
grove.on_gesture(GroveGesture.WAVE, on_gesture_wave)

def on_gesture_right():
    basic.show_number(2)
grove.on_gesture(GroveGesture.RIGHT, on_gesture_right)

def on_gesture_backward():
    basic.show_number(4)
grove.on_gesture(GroveGesture.BACKWARD, on_gesture_backward)

def on_gesture_clockwise():
    basic.show_number(5)
grove.on_gesture(GroveGesture.CLOCKWISE, on_gesture_clockwise)

def on_gesture_forward():
    basic.show_number(3)
grove.on_gesture(GroveGesture.FORWARD, on_gesture_forward)

def on_gesture_left():
    basic.show_number(1)
grove.on_gesture(GroveGesture.LEFT, on_gesture_left)

def on_gesture_anticlockwise():
    basic.show_number(6)
grove.on_gesture(GroveGesture.ANTICLOCKWISE, on_gesture_anticlockwise)

basic.show_icon(IconNames.ASLEEP)
basic.pause(1000)
basic.clear_screen()

def on_forever():
    pass
basic.forever(on_forever)
