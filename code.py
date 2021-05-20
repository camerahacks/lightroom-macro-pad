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
from adafruit_hid.keycode import Keycode

# ------------------------
# Definitions
# ------------------------

# LED - Pico's onboard lED is GP25
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

btn_0_pin = board.GP17
btn_1_pin = board.GP4
btn_2_pin = board.GP6
btn_3_pin = board.GP10
btn_4_pin = board.GP27
btn_5_pin = board.GP21
btn_6_pin = board.GP0


# Keyboard device.
kbd = Keyboard(usb_hid.devices)

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

_FREQUENCY = 0.1
_DEBOUNCE = 0.05


# ------------------------
# Mode Classes
# ------------------------

# Add as many macros to the 'macros' function as the number
# of buttons/switches in the same order you would like the
# buttons to be organized in. Array index 0 will be trggered
# by btn_0, index 1 by btn_1,...
# If a button shouldn't do anything, add the 'nothing' macro
# to its position


class LibraryModule:
    def name():
        return 'Library Module Shortcuts'

    def color():
        return '' 
    def macros():
        # This is where you add the list of macros for this mode
        # add as many macros as the number of buttons/switches.
        return [
                grid,
                editKeywords,
                increaseFlag,
                decreaseFlag,
                virtualCopy,
                nothing
                ]

class Culling:
    
    def name():
        return 'Culling Shortcuts'
    
    def color():
        return ''

    def macros():
        # This is where you add the list of macros for this mode
        # add as many macros as the number of buttons/switches
        return [
                oneToOneZoom,
                goPrevious,
                increaseFlag,
                decreaseFlag,
                goNext,
                nothing
                ]

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
        return 'Create Vitual Copy'

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
        kbd.send(Keycode.SPACE)

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
        return "Select Flagged Photos"

    def macro():
        kbd.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.U)


# ------------------------
# Functions
# ------------------------

def init():
    global modes
    global curr_mode
    global mode_macros

    modes = [LibraryModule,Culling]
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

print('Ready') # DELETE

# ------------------------
# Main Loop
# ------------------------

while True:
    # If Mode button is pressed, get the next mode
    # Modulo operation makes sure we loop aound the list
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