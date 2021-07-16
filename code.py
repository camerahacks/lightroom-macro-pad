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

_VERSION = 'v0.5'
_DEBOUNCE = 0.020

# ------------------------
# Mode Classes
# ------------------------

# Add as many macros to the 'macros' function as the number
# of buttons/switches in the same order you would like the
# buttons to be organized in. Array index 0 will be triggered
# by btn_0, index 1 by btn_1,...
# If a button shouldn't do anything, add the 'nothing' macro
# to its position

class TestMode:
    def name():
        return 'Test Mode'

    def color():
        return ''

    def macros():
        # This is where you add the list of macros for this mode
        # add as many macros as the number of buttons/switches.
        return [nothing, nothing, nothing, nothing, nothing, nothing]

class Culling:
    
    def name():
        return 'Culling Shortcuts'
    
    def color():
        return 'red'

    def macros():
        # This is where you add the list of macros for this mode
        # add as many macros as the number of buttons/switches
        return [grid, increaseFlag, oneToOneZoom, goPrevious, decreaseFlag, goNext]

class LibraryModule:
    def name():
        return 'Library Module Shortcuts'

    def color():
        return 'green'

    def macros():
        return [grid, increaseFlag, editKeywords, loupe, decreaseFlag, virtualCopy]

class Photoshop:

    def name():
        return 'Photoshop Shortcuts'

    def color():
        return 'blue'

    def macros():
        return [nothing, nothing, nothing, nothing, nothing, nothing]


# ------------------------
# Shortcut/Macro Classes
# ------------------------

### Shortcuts for all modules ###
class nothing:

    def macroName():
        return 'Do Nothing'

    def macro():
        print('Do Nothing')

class goNext:

    def macroName():
        return 'Next Picture'

    def macro():
        kbd.send(Keycode.RIGHT_ARROW)

class goPrevious:

    def macroName():
        return 'Previous Picture'

    def macro():
        kbd.send(Keycode.LEFT_ARROW)

class increaseFlag:
    
    def macroName():
        return 'Increase Flag Status'
    
    def macro():
        kbd.send(Keycode.CONTROL, Keycode.UP_ARROW)

class decreaseFlag:
    
    def macroName():
        return 'Decrease Flag Status'
    
    def macro():
        kbd.send(Keycode.CONTROL, Keycode.DOWN_ARROW)

class virtualCopy:

    def macroName():
        return 'Create Virtual Copy'

    def macro():
        kbd.send(Keycode.CONTROL, Keycode.QUOTE)

class toggleFilters:

    def macroName():
        return 'Toggle Filters On/Off'

    def macro():
        kbd.send(Keycode.CONTROL, Keycode.L)

### Module Specific Shortcuts ###

### Library Module ###

class editKeywords:

    def macroName():
        return 'Edit Keywords'

    def macro():
        kbd.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.K)

class oneToOneZoom:

    def macroName():
        return 'Toggle Loupe and 1:1 Zoom'

    def macro():
        m.click(Mouse.LEFT_BUTTON)

class loupe:

    def macroName():
        return "Loupe View"

    def macro():
        kbd.send(Keycode.E)

class grid:

    def macroName():
        return "Grid View"

    def macro():
        kbd.send(Keycode.G)

class compare:

    def macroName():
        return "Compare View"

    def macro():
        kbd.send(Keycode.C)

class survey:

    def macroName():
        return "Survey View"

    def macro():
        kbd.send(Keycode.N)

class selectFlagged:

    def macroName():
        return "Select Flagged Photos"

    def macro():
        kbd.send(Keycode.CONTROL, Keycode.ALT, Keycode.A)

### Develop Module ###

class whiteBalance:

    def macroName():
        return "Auto White Balance"

    def macro():
        kbd.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.U)


class copySettings:

    def macroName():
        return "Copy Develop Settings"

    def macro():
        kbd.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.C)

class pasteSettings:

    def macroName():
        return "Paste Develop Settings"

    def macro():
        kbd.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.V)

### Non-lightroom Macros ###
# Mainly used for testing but can also be used inside Lightroom

class copy:
    
    def macroName():
        return "Copy"

    def macro():
        kbd.send(Keycode.CONTROL, Keycode.C)

class paste:

    def macroName():
        return "Paste"

    def macro():
        kbd.send(Keycode.CONTROL, Keycode.V)

class chrome:

    def macroName():
        return "Launch Chrome Browser"

    def macro():
        kbd.send(Keycode.GUI, Keycode.R)
        time.sleep(0.05)
        layout.write('chrome\n')

class explorer:

    def macroName():
        return "Launch Chrome Browser"

    def macro():
        kbd.send(Keycode.GUI, Keycode.R)
        time.sleep(0.05)
        layout.write('explorer\n')

# Define Macro Classes to load 

modes = [Culling,LibraryModule,Photoshop]
curr_mode = modes[0]
mode_macros = curr_mode.macros()
mode_color = curr_mode.color()


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

# Pi Pico     SW0        SW1        SW2        SW3        SW4        SW5        SW6         SW7         SW8         SW9       #
board_pins = (board.GP0, board.GP1, board.GP2, board.GP6, board.GP8, board.GP7, board.GP11, board.GP13, board.GP12, board.GP16)

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
        mode_macros = curr_mode.macros()
        print(curr_mode) #DELETE
    
    elif k_event and k_event.pressed:
        #print("keys", k_event.key_number, k_event.pressed) #DELETE
        mode_macros[k_event.key_number].macro()
        print(mode_macros[k_event.key_number].macroName()) #DELETE