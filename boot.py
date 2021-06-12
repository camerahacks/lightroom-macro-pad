# ------------------------------------------------------------ #
# Raspberry Pi Pico Lithroom Macro Pad
# @author André Costa dphacks.com
# @link dphacks.com
#
# Refer to the License file for permissions to use and distribute
# this software
# Refer to the README file how to edit the boot file
# ------------------------------------------------------------ #

# ------------------------
# Standard Libraries
# ------------------------

import os
import storage
import board, digitalio
try:
    import usb_cdc # usb_cdc is not available in all boards and CP versions
    importCDC = 1
except ImportError:
    importCDC = 0

# ------------------------
# Definitions
# ------------------------

button = digitalio.DigitalInOut(board.GP0) #
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# CircuitPython Version
CPVersion = tuple(map(int, os.uname().release.split('.')))

# Disabling USB drive and REPL can lock you out of your board.
# These settings will prevent your board from showing as a USB
# drive and REPL will be disabled.
# Make sure your "fail safe" button is working before
# disabling REPL. Do this at your own risk.

_DISABLEUSB = 0 # Set to 1 to disable USB drive
_DISABLEREPL = 0 # Set to 1 to disable REPL

# The commands below only work in CP version 7.0 and up
if CPVersion >= (7, 0):
    
    # Turn off CIRCUITPY drive.
    if _DISABLEUSB:
        storage.disable_usb_drive()
        print('USB Drive CIRCUITPY disabled')
    
    # Turn off REPL if button is not pressed.
    # Failsafe in case USB drive is also disabled
    if _DISABLEREPL:
        if button.value and importCDC:
            usb_cdc.disable()
            print('REPL disabled')