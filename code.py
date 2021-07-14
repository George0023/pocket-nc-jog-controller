# MIT License

# Copyright (c) 2021 George0023

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time
import board
import digitalio
import rotaryio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.mouse import Mouse

OUT = digitalio.Direction.OUTPUT
DOWN = digitalio.Pull.DOWN

# setups:
kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)
# keys that will be sent when button is pressed
keymap = (          
    (Keycode.GUI, Keycode.ALT, Keycode.CONTROL, Keycode.SHIFT, Keycode.ONE),
    (Keycode.GUI, Keycode.ALT, Keycode.CONTROL, Keycode.SHIFT, Keycode.TWO),
    (Keycode.GUI, Keycode.ALT, Keycode.CONTROL, Keycode.SHIFT, Keycode.THREE),
    (Keycode.GUI, Keycode.ALT, Keycode.CONTROL, Keycode.SHIFT, Keycode.FOUR),
    (Keycode.GUI, Keycode.ALT, Keycode.CONTROL, Keycode.SHIFT, Keycode.FIVE),
)
mouse = Mouse(usb_hid.devices)

# encoder
encoder = rotaryio.IncrementalEncoder(board.GP12, board.GP13)

# keys:
key_states = [False, False, False, False, False]
button_states = [0, 0, 0, 0, 0]

# buttons:
b1 = digitalio.DigitalInOut(board.GP2)
b2 = digitalio.DigitalInOut(board.GP3)
b3 = digitalio.DigitalInOut(board.GP4)
b4 = digitalio.DigitalInOut(board.GP5)
b5 = digitalio.DigitalInOut(board.GP6)

b1.switch_to_input(pull=DOWN)
b2.switch_to_input(pull=DOWN)
b3.switch_to_input(pull=DOWN)
b4.switch_to_input(pull=DOWN)
b5.switch_to_input(pull=DOWN)

buttons = [b1, b2, b3, b4, b5]

# leds:
l1 = digitalio.DigitalInOut(board.GP7)
l2 = digitalio.DigitalInOut(board.GP8)
l3 = digitalio.DigitalInOut(board.GP9)
l4 = digitalio.DigitalInOut(board.GP10)
l5 = digitalio.DigitalInOut(board.GP11)

l1.direction = OUT
l2.direction = OUT
l3.direction = OUT
l4.direction = OUT
l5.direction = OUT

leds = [l1, l2, l3, l4, l5]

# detect key presses
def pessAndRelease():
    global button_states
    global key_states
    global buttons
    global leds
    i = 0
    for key in buttons:
        # 1 if for the first press
        button_states[i] = key.value
        i += 1
    i = 0
    # wait 0.05 sec for better key press reliability
    time.sleep(0.05)
    for key in buttons:
        if button_states[i] == 1 and button_states[i] != key.value:  # check for release
            key_states[i] = not key_states[i]
            button_states[i] = 0
            # send key press
            kbd.press(*keymap[i])
            time.sleep(0.05)
            kbd.release(*keymap[i])
        i += 1
    i = 0
    for led in leds:
        if key_states[i]:
            led.value = True
        else:
            led.value = False
        i += 1


last_position = 0
while True:
    pessAndRelease()
    # mouse wheel
    position = encoder.position
    if last_position is None or position != last_position:
        if position > last_position:
            mouse.move(wheel = 1)
        elif position < last_position:
            mouse.move(wheel = -1)
    last_position = position

