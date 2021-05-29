# Adobe Lightroom Macro Pad

Although this firmware is functional, this project is a work in progress.

This is a Raspberry Pi Pico Lightroom Macro Pad based on CircuitPython. It's designed to work with 7 buttons or mechanical switches. One switch for choosing the mode and 6 switches to execute the macros/shortcuts.

It can be easily ported to other microcontrollers by modifying some variables

More pictures and details once the project moves along.

## Lightroom Classic Shortcut Reference

<a href="https://helpx.adobe.com/lightroom-classic/help/keyboard-shortcuts.html" target="_blank">https://helpx.adobe.com/lightroom-classic/help/keyboard-shortcuts.html</a>

## Libraries/Dependencies
Make sure you have these in the lib folder on your board:
* <a href="https://github.com/adafruit/Adafruit_CircuitPython_HID" target="_blank">Adafruit_HID</a>


### Keycode Reference

<a href="https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/master/adafruit_hid/keycode.py" target="_blank">https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/master/adafruit_hid/keycode.py</a>


## Layout

More info coming

## 3D Printing

More info coming

## How to edit the code

Make changes to the code block below if you will be using different pins on your board

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
        # add as many macros as the number of macro buttons/switches
        return [
                oneToOneZoom,
                goPrevious,
                increaseFlag,
                decreaseFlag,
                goNext,
                nothing
                ]
```

The ```macros()``` method is a list of ```macro``` classes. List position 0 is triggered by button 0, list position 1 by button 1, and so on...

Finally, add the list of ```modes``` to the ```init()``` function.

```python
def init():
    global modes
    global curr_mode
    global mode_macros

    modes = [LibraryModule,Culling] # Edit this list
    curr_mode = modes[0]
    mode_macros = curr_mode.macros()
```

