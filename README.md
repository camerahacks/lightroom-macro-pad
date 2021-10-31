More camera and photography related hacks @ [{DPHacks}](https://dphacks.com/) Blog

# Adobe Lightroom Macro Pad

This project started as a Raspberry Pi Pico Lightroom Macro Pad based on CircuitPython but it is growing to include other controllers. It's designed to work with 7 or 10 mechanical switches. One switch for choosing the mode and the other switches to execute the macros/shortcuts. You can modify the code and create your own shortcuts/macros.

![Lightroom Macro Pad - Raspberry Pi Pico](https://dphacks.com/wp-content/uploads/2021/09/10_Switch_LR_Macro_Pad-1.jpg "Pi Pico Macro Pad for Lightroom Classic")

Although the firmware for this project is functional, this is a work in progress. If you find any bugs or issues, please let me know.

It can be easily ported to other microcontrollers by modifying a few variables in ```config.py```. For example, I've since created a macro pad to be used with Pimoroni's Tiny 2040 board.

I periodically add more pictures and details so it is easier for other folks to create their own macro pad.

## Lightroom Classic Shortcut Reference

<a href="https://helpx.adobe.com/lightroom-classic/help/keyboard-shortcuts.html" target="_blank">https://helpx.adobe.com/lightroom-classic/help/keyboard-shortcuts.html</a>

## Libraries/Dependencies
Make sure you have these in the lib folder on your board:
* <a href="https://github.com/adafruit/Adafruit_CircuitPython_HID" target="_blank">Adafruit_HID</a>


### Keycode Reference

<a href="https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/master/adafruit_hid/keycode.py" target="_blank">https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/master/adafruit_hid/keycode.py</a>

## Versions (READ THIS)

V0.7 Complete rework of the macro setup. It's much easier to edit and create macros. Macro configuration now lives in ```config.py```

V0.5 (in progress/main branch) transitions to Circuit Python's new Keypad API that allows key pin and matrix scans. This feature is only available in Circuit Python 7.0.0.

V0.1 works on CircuitPython 6.2.0 and above

## Coming Soon - Wishlist

* ~~Support 10-Switch layout~~ (done)
* Ability to scan a diode matrix (WIP)
* ~~Pimoroni Tiny 2020 Case~~ (done)

## Switch Layout

3D printable files are available for both layouts. 

7-switch: Switches 0-5 are used for macros and switch 6 is used for switching modes.

```
|     |   0   |   1   |   2   |
|  6  |   3   |   4   |   5   |
```

10-switch: Switches 0-8 are used for macros and switch 9 is used for switching modes.
```
|     |   0   |   1   |   2   |
|     |   3   |   4   |   5   |
|  9  |   6   |   7   |   8   |
```

## 3D Printing/ Case

Print the case in any material you choose. The bottom part on the 7-switch layout is just pressure fitted into the top piece using a 0.1mm tolerance. The bottom also has stand-offs for fitting the Pico.

The 10-switch case uses round magnets to snap the case parts together. Here is a link to the magnets I used: https://amzn.to/3CPtB5V (affiliate link), they are 5x2mm (diameter x thickness) magnets.

The case uses standard MX spacing, meaning you can use any MX compatible switches and keycaps.

STL and 3mf files can be found in the ```case``` folder.

## Keycaps

I'm using relegendable keycaps from X-keys (affiliate link: https://amzn.to/3gmbBYO) but you can use any keycap you'd like. I created a few icons so I can remember what each switch is mapped to. The legend SVG file can be found in the ```/keycaps``` folder.

## PCB

I created a simple PCB that makes the whole process a lot more plug and play. Creating these things actually takes a lot of time so I'm not releasing the PCB as open source just yet. If you are interested, you can head over to the <a href="https://www.etsy.com/shop/DPHacks" target="_blank">Etsy store</a> I setup to sell some electronic related items.

Just like the case, the PCB has MX spacing. I'll be releasing a 3D model of the PCB so you can design your own case if needed.

![Lightroom Macro Pad - PCB](https://dphacks.com/wp-content/uploads/2021/09/10_Switch_LR_Macro_Pad-2.jpg "Lightroom Macro Pad - PCB")

![Lightroom Macro Pad - PCB](https://dphacks.com/wp-content/uploads/2021/09/10_Switch_LR_Macro_Pad-3.jpg "Lightroom Macro Pad - PCB")

## Wiring the Macro Pad (Handwire version)

![Lightroom Macro Pad - Raspberry Pi Pico](https://dphacks.com/wp-content/uploads/2021/06/Lightroom_Macro_Pad_Mechanical_Switch-6.jpg "Pi Pico Macro Pad for Lightroom Classic Wiring")

Connect one of the pins on the switches to one of the ground (GND) pins on the Raspberry Pi Pico. The switches don't have a polarity, so you can choose which pin is connected to GND. There is no right or wrong. You can see in the picture above that all of the GND pins on the switches are connected with the white wire. The white wire is then connected to a GND pin on the Pico.

Connect the other free pin on the switches to a corresponding GPIO pin on the Pico. Take note of which switch is connected to which GPIO pin so you can edit the firmware code accordingly. Again, there is no right or wrong here, you can pick any of them.

## How to edit ```config.py```

### Starting with v0.7

Starting with version 0.7 the board pin and macro configuration are done in ```config.py```. You shouldn't have to make any changes to ```code.py```

Make changes to the code block below if you will be using different pins on your board.

```python
# Pi Pico     SW0        SW1        SW2        SW3        SW4        SW5        SW6         SW7         SW8         SW9       #
board_pins = (board.GP0, board.GP1, board.GP2, board.GP6, board.GP8, board.GP7, board.GP11, board.GP13, board.GP12, board.GP16)
```

Next, edit the code block below. (I'm working on creating a web based tool that will create ```config.py``` for you)

The example below has two modes: Culling and Library. Each mode has 9 macros configured since the keypad has 9 switches.

```python
configvar = [{"name":"Culling", # Mode Name
            "color":"red", # Mode Color, only used on devices with RGB led
            "macros":
                    [
                    {"Name":"grid", "keycomb":[Keycode.G]}, # Each macro has a name and a key combination. Keycode reference linked above
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
            {"name":"Library", # Second mode starts here
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
```

## How to edit ```boot.py```

The options below only work on CircuitPython 7.0.0 or higher, if you have a lower version, these settings will just be ignored.

### Disabe CIRCUITPY drive

Disable the Raspberry Pi Pico mass storage device. This will prevent the Raspberry Pi Pico from showing as an additional drive on your computer.
```python
_DISABLEUSB = 1
```

The most graceful way to enable the CIRCUITPY mass storage device again is to enter REPL and run the code below. The extra line returns match the carriage returns needed to run this code block in REPL with the correct python indentation.

```python
import storage
storage.remount("/", readonly=False)
with open('boot.py') as f:
    newText=f.read().replace('_DISABLEUSB = 1', '_DISABLEUSB = 0')



with open('boot.py', 'w') as f:
    f.write(newText)




```
Another option is to nuke the ```boot.py``` file altogether. Enter REPL and run the code below. Easier to run and to remember but definitely not as graceful.

```python
import os
os.remove('boot.py')
```
A soft reset through REPL does not execute the ```boot.py``` file, you have to either bridge the RUN and GND pins OR disconnect and reconnect the USB cable to make your board run the boot code.

### Disable REPL

Disable the console USB device, which means you won't be able to connect a serial monitor and enter REPL. If you disable REPL and USB Device (option above), you can lock yourself out of the board. So, make sure you know what you are doing before enabling both options

```boot.py``` has a built-in failsafe option to push the Mode switch during boot so you can regain console/REPL access. Make sure to test the Mode key on your macro pad before enabling this option.
```python
_DISABLEREPL = 1
```
