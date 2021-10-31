# ------------------------------------------------------------ #
# Raspberry Pi Pico Lithroom Macro Pad
# @author André Costa dphacks.com
# @website dphacks.com

#
# Refer to the License file for permissions to use and distribute
# this software
# Refer to the README file how to edit the macros in this code
# This version of the code only runs on CircuitPython 7.0.0 and above
# ------------------------------------------------------------ #

# ------------------------
# Standard Libraries
# ------------------------

import time
import keypad
import board
import usb_hid

# ------------------------
# Additional Libraries
# These will have to be installed separately
# ------------------------

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# ------------------------
# Edit config.py to make changes to macros
# DO NOT edit the line in this file.
# ------------------------

import config

# ------------------------
# Definitions
# ------------------------

# LED - Pico's onboard lED is GP25
# led = digitalio.DigitalInOut(board.GP25)
# led.direction = digitalio.Direction.OUTPUT

# Keyboard device.
m = Mouse(usb_hid.devices)
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

# ------------------------
# Global Variables
# ------------------------

_VERSION = 'v0.7'
_DEBOUNCE = 0.020


# ------------------------
# Mode and Shortcut/Macro Classes
# ------------------------

class Macro:
    def __init__(self, name, keycomb):
        self.name = name
        self.keycomb = keycomb
    
    def macroName(self):
        return self.name

    def macroCall(self):
        kbd.send(*self.keycomb) #Expand keycode as parameters


class Mode:
    def __init__(self, name, color, macros):
        self.name = name
        self.color = color
        self.macros = macros

    def modeName(self):
        return self.name

    def modeColor(self):
        return self.color

    def modeMacros(self):
        mmacros = []
        for macros in self.macros:
            mmacros.append(Macro(macros['Name'], macros['keycomb']))
        
        return mmacros


modes = []
for mmodes in config.configvar:
    modes.append(Mode(mmodes['name'], mmodes['color'], mmodes['macros']))

curr_mode = modes[0]
mode_macros = curr_mode.modeMacros()
mode_color = curr_mode.modeColor()

# ------------------------
# Pin and Keypad configuration
# ------------------------

# 7-Switch Layout
# -------------------------------#
# |     |   0   |   1   |   2   |
# -------------------------------#
# | 6   |   3   |   4   |   5   |
# -------------------------------#

# 10-Switch Layout
# -------------------------------#
# |     |   0   |   1   |   2   |
# -------------------------------#
# |     |   3   |   4   |   5   |
# -------------------------------#
# | 9   |   6   |   7   |   8   |

# This part is commented for now. Only used if a diode matrix is in use

#km = keypad.KeyMatrix(
#    row_pins=(board.GP17, board.GP4, board.GP6),
#    col_pins=(board.GP10, board.GP8))

board_pins = config.board_pins

k = keypad.Keys(pins=board_pins, value_when_pressed=False, pull=True, interval=_DEBOUNCE)

# Mode switch/pin
#MODE_SW = keypad.Event(6, True) # 7-switch layout

MODE_SW = keypad.Event(9, True) # 10-switch layout

while True:
    # This part is commented for now. Only used if a diode matrix is in use
    #km_event = km.events.next()
    #if km_event:
        #print(len(km.events), "events queued")
        #print("matrix", km_event)

    k_event = k.events.get()

    if k_event == MODE_SW:
        # Change mode
        curr_mode = modes[(modes.index(curr_mode)+1) % len(modes)]
        # Load up the mode macros
        mode_macros = curr_mode.modeMacros()
        print(curr_mode.name) #DELETE
    
    elif k_event and k_event.pressed:
        #print("keys", k_event.key_number, k_event.pressed) #DELETE
        mode_macros[k_event.key_number].macroCall()
        print(mode_macros[k_event.key_number].macroName()) #DELETE