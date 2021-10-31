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

from adafruit_hid.mouse import Mouse
from adafruit_hid.keycode import Keycode
import board

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


# Tiny 2040   SW0       SW1       SW2       SW3        SW4        SW5       SW6        SW7        SW8        SW9      #
board_pins = (board.A1, board.A2, board.A3, board.GP6, board.GP7, board.A0, board.GP3, board.GP4, board.GP5, board.GP2)

# Add as many macros to the variable below as the number
# of buttons/switches in the same order you would like the
# buttons to be organized in. "macros" array index 0 will 
# be triggered by btn_0, index 1 by btn_1,...
# If a button shouldn't do anything, add the 'nothing' macro
# to its position

# Use the Keycode reference link below to edit the macros.
# There is no limit in how many key strokes to send at once but
# but keep in mind your computer might not be able to process all
# at once.
# https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/master/adafruit_hid/keycode.py

# Refer to README.md on how to edit the code block below.

configvar = [{"name":"Culling",
            "color":"red",
            "macros":
                    [
                    {"Name":"grid", "keycomb":[Keycode.G]},
                    {"Name":"oneToOneZoom", "keycomb":[Mouse.LEFT_BUTTON]},
                    {"Name":"crop", "keycomb":[Keycode.R]},
                    {"Name":"loupe", "keycomb":[Keycode.E]},
                    {"Name":"increaseFlag", "keycomb":[Keycode.CONTROL, Keycode.UP_ARROW]},
                    {"Name":"toggleFilters", "keycomb":[Keycode.CONTROL, Keycode.L]},
                    {"Name":"goPrevious", "keycomb":[Keycode.LEFT_ARROW]},
                    {"Name":"decreaseFlag", "keycomb":[Keycode.CONTROL, Keycode.DOWN_ARROW]},
                    {"Name":"goNext", "keycomb":[Keycode.RIGHT_ARROW]}
                    ]
            },
            {"name":"Library",
            "color":"blue",
            "macros":
                    [
                    {"Name":"grid", "keycomb":[Keycode.G]},
                    {"Name":"oneToOneZoom", "keycomb":[Mouse.LEFT_BUTTON]},
                    {"Name":"crop", "keycomb":[Keycode.R]},
                    {"Name":"loupe", "keycomb":[Keycode.E]},
                    {"Name":"increaseFlag", "keycomb":[Keycode.CONTROL, Keycode.UP_ARROW]},
                    {"Name":"toggleFilters", "keycomb":[Keycode.CONTROL, Keycode.L]},
                    {"Name":"goPrevious", "keycomb":[Keycode.LEFT_ARROW]},
                    {"Name":"decreaseFlag", "keycomb":[Keycode.CONTROL, Keycode.DOWN_ARROW]},
                    {"Name":"goNext", "keycomb":[Keycode.RIGHT_ARROW]}
                    ]
            }]