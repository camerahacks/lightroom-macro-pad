# Adobe Lightroom Macro Pad

This is a Raspberry Pi Pico Lightroom Macro Pad based on CircuitPython. It's designed to work with 7 buttons or mechanical switches. One switch for choosing the mode and 6 switches to execute the macros/shortcuts. You can modify the code and create your own shortcuts/macros.

![Lightroom Macro Pad - Raspberry Pi Pico](https://dphacks.com/wp-content/uploads/2021/06/Lightroom_Macro_Pad_Mechanical_Switch-2.jpg "Pi Pico Macro Pad for Lightroom Classic")

Although the firmware for this project is functional, this is a work in progress.

It can be easily ported to other microcontrollers by modifying a few variables.

More pictures and details once the project moves along.

## Lightroom Classic Shortcut Reference

<a href="https://helpx.adobe.com/lightroom-classic/help/keyboard-shortcuts.html" target="_blank">https://helpx.adobe.com/lightroom-classic/help/keyboard-shortcuts.html</a>

## Libraries/Dependencies
Make sure you have these in the lib folder on your board:
* <a href="https://github.com/adafruit/Adafruit_CircuitPython_HID" target="_blank">Adafruit_HID</a>


### Keycode Reference

<a href="https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/master/adafruit_hid/keycode.py" target="_blank">https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/master/adafruit_hid/keycode.py</a>


## Switch Layout

This micro pad has 7 buttons. Buttons 0-5 are used for macros and button 6 is used for switching modes.

```
|     |   0   |   1   |   2   |
|  6  |   3   |   4   |   5   |
```

## 3D Printing

Print the case in any material you choose. The bottom part is just pressure fit into the top piece using a 0.1mm tolerance. The bottom also has stand-offs for fitting the Pico. STL files can be found in the ```case``` folder.

## Keycaps

I'm using relegendable keycaps from X-keys (affiliate link: https://amzn.to/3gmbBYO) but you can use any keycap you'd like. I created a few icons so I can remember what each switch is mapped to.

## Wiring the Macro Pad

![Lightroom Macro Pad - Raspberry Pi Pico](https://dphacks.com/wp-content/uploads/2021/06/Lightroom_Macro_Pad_Mechanical_Switch-6.jpg "Pi Pico Macro Pad for Lightroom Classic Wiring")

Connect one of the pins on the switches to one of the ground (GND) pins on the Raspberry Pi Pico. The switches don't have a polarity, so you can choose which pin is connected to GND. There is no right or wrong.

Connect the other free pin on the switches to a corresponding GPIO pin on the Pico. Take note of which switch is connected to which GPIO pin so you can edit the firmware code accordingly. Again, there is no right or wrong here, you can pick any of them.

## How to edit ```code.py```

Make changes to the code block below if you will be using different pins on your board.

```python
btn_0_pin = board.GP17
btn_1_pin = board.GP4
btn_2_pin = board.GP6
btn_3_pin = board.GP10
btn_4_pin = board.GP27
btn_5_pin = board.GP21
btn_6_pin = board.GP0
```

You can also add more macros/shortcuts. Each shortcut is its own class, just make sure to structure the class like the example below.

```python
class increaseFlag:
    
    def macroName():
        return 'Increase Flag Status'
    
    def macro():
        kbd.send(Keycode.CONTROL, Keycode.UP_ARROW) # Shortcut key combination
```

Once you have all the shortcut classes created, you can edit existing ```modes``` by altering or creating new classes following the format below.

```python
class Culling:
    
    def name():
        return 'Culling Shortcuts'
    
    def color():
        return ''

    def macros():
        # This is where you add the list of macros for this mode
        # add as many macros as the number of buttons/switches
        return [grid, increaseFlag, oneToOneZoom, goPrevious, decreaseFlag, goNext]
```

The ```macros()``` method is a list of ```macro``` classes. List position 0 is triggered by button 0, list position 1 by button 1, and so on...

Finally, add the list of ```modes``` to the ```init()``` function.

```python
def init():
    global modes
    global curr_mode
    global mode_macros

    modes = [LibraryModule, Culling] # Edit this list
    curr_mode = modes[0]
    mode_macros = curr_mode.macros()
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
A soft reset through REPL does not execute the ```boot.py``` file, you have to either bridge the RUN and GND pins or disconnect and connect the USB cable to make your board run the boot code.

### Disable REPL

Disable the console USB device, which means you won't be able to connect a serial monitor and enter REPL. If you disable REPL and USB Device (option above), you can lock yourself out of the board. So, make sure you know what you are doing before enabling both options

```boot.py``` has a built-in failsafe option to push the Mode switch during boot so you can regain console/REPL access. Make sure to test the Mode key on your macro pad before enabling this option.
```python
_DISABLEREPL = 1
```
