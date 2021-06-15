# ------------------------------------------------------------ #
# Raspberry Pi Pico Lithroom Macro Pad
# @author André Costa dphacks.com
# @link dphacks.com
#
# Refer to the License file for permissions to use and distribute
# this software
# Refer to the README file how to edit the macros in this code
# ------------------------------------------------------------ #

# ------------------------
# Standard Libraries
# ------------------------

import time
import board
import digitalio

# ------------------------
# Additional Libraries
# These will have to be installed separately
# ------------------------

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# ------------------------
# Definitions
# ------------------------

# LED - Pico's onboard lED is GP25
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

# Layout
# -------------------------------#
# |     |   0   |   1   |   2   |
# -------------------------------#
# | 6   |   3   |   4   |   5   |
# -------------------------------#

btn_0_pin = board.GP17
btn_1_pin = board.GP4
btn_2_pin = board.GP6
btn_3_pin = board.GP10
btn_4_pin = board.GP8
btn_5_pin = board.GP14
btn_6_pin = board.GP1


# Keyboard device.
m = Mouse(usb_hid.devices)
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

# Buttons/Switches
btn_0 = digitalio.DigitalInOut(btn_0_pin)
btn_0.direction = digitalio.Direction.INPUT
btn_0.pull = digitalio.Pull.UP

btn_1 = digitalio.DigitalInOut(btn_1_pin)
btn_1.direction = digitalio.Direction.INPUT
btn_1.pull = digitalio.Pull.UP

btn_2 = digitalio.DigitalInOut(btn_2_pin)
btn_2.direction = digitalio.Direction.INPUT
btn_2.pull = digitalio.Pull.UP

btn_3 = digitalio.DigitalInOut(btn_3_pin)
btn_3.direction = digitalio.Direction.INPUT
btn_3.pull = digitalio.Pull.UP

btn_4 = digitalio.DigitalInOut(btn_4_pin)
btn_4.direction = digitalio.Direction.INPUT
btn_4.pull = digitalio.Pull.UP

btn_5 = digitalio.DigitalInOut(btn_5_pin)
btn_5.direction = digitalio.Direction.INPUT
btn_5.pull = digitalio.Pull.UP

btn_6 = digitalio.DigitalInOut(btn_6_pin)
btn_6.direction = digitalio.Direction.INPUT
btn_6.pull = digitalio.Pull.UP

mode_btn = btn_6

# ------------------------
# Global Variables
# ------------------------

_VERSION = 'v0.1'

_FREQUENCY = 0.1
_DEBOUNCE = 0.05

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
        return ''

    def macros():
        # This is where you add the list of macros for this mode
        # add as many macros as the number of buttons/switches
        return [grid, increaseFlag, oneToOneZoom, goPrevious, decreaseFlag, goNext]

class LibraryModule:
    def name():
        return 'Library Module Shortcuts'

    def color():
        return ''

    def macros():
        return [grid, increaseFlag, editKeywords, loupe, decreaseFlag, virtualCopy]

class Photoshop:

    def name():
        return 'Photoshop Shortcuts'

    def color():
        return ''

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

# ------------------------
# Functions
# ------------------------

def init():
    global modes
    global curr_mode
    global mode_macros

    modes = [Culling,LibraryModule]
    curr_mode = modes[0]
    mode_macros = curr_mode.macros()

def debounce():
    time.sleep(_DEBOUNCE)

# ------------------------
# Boot Sequence
# ------------------------

init()

# Flash the LED when boot is complete
for x in range(0, 5):

	led.value = False
	time.sleep(0.2)
	led.value = True
	time.sleep(0.2)

led.value = False

print('Ready') # DELETE

# ------------------------
# Main Loop
# ------------------------

while True:
    # If Mode button is pressed, get the next mode
    # Modulo operation makes sure we loop around the list
    if not mode_btn.value:
        curr_mode = modes[(modes.index(curr_mode)+1) % len(modes)]

        # Load up the mode macros
        mode_macros = curr_mode.macros()
        
        print(curr_mode) #DELETE
        debounce()

    if not btn_0.value:
        mode_macros[0].macro()
        debounce()

    if not btn_1.value:
        mode_macros[1].macro()
        debounce()

    if not btn_2.value:
        mode_macros[2].macro()
        debounce()

    if not btn_3.value:
        mode_macros[3].macro()
        debounce()

    if not btn_4.value:
        mode_macros[4].macro()
        debounce()

    if not btn_5.value:
        mode_macros[5].macro()
        debounce()

    time.sleep(_FREQUENCY)