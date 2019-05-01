# Dependencies
from inputs import get_gamepad
import keyboard

# Config settings
import config


def main():
    print('Running main mode')
    while True:
        events = get_gamepad()
        for event in events:
            """
            Function allows character to move
            It is necessary here to rotate character
            """
            if event.code == "ABS_HAT0X" and event.state == 1:
                keyboard.press(config.right)
            if event.code == "ABS_HAT0X" and event.state == 0:
                keyboard.release(config.right)
            if event.code == "ABS_HAT0X" and event.state == -1:
                keyboard.press(config.left)
            if event.code == "ABS_HAT0X" and event.state == 0:
                keyboard.release(config.left)
            if event.code == "ABS_HAT0Y" and event.state == -1:
                keyboard.press(config.up)
            if event.code == "ABS_HAT0Y" and event.state == 0:
                keyboard.release(config.up)
            if event.code == "ABS_HAT0Y" and event.state == 1:
                keyboard.press(config.down)
            if event.code == "ABS_HAT0Y" and event.state == 0:
                keyboard.release(config.down)
            """
            Rotating character by holding left ctrl -
            you can change "config.[button]" for your own preferences
            """
            if event.code == config.y and event.state == 1:
                keyboard.press(config.left_ctrl)
            if event.code == config.y and event.state == 0:
                keyboard.release(config.left_ctrl)
            """
            triggers - numpad walking - you can change "config.[button]" 
            for your own preferences
            """
            if event.code == config.lb and event.state == 1:
                keyboard.send(config.numpad_7)
            if event.code == config.rb and event.state == 1:
                keyboard.send(config.numpad_9)
            if event.code == config.rt and event.state > config.trigger_power:
                keyboard.send(config.numpad_3)
            if event.code == config.lt and event.state > config.trigger_power:
                keyboard.send(config.numpad_1)
            """
            buttons - you can change "config.[button]" 
            for your own preferences (y does rotating and b change mode)
            """
            if event.code == config.x and event.state == 1:
                keyboard.send(config.f1)
            if event.code == config.a and event.state == 1:
                keyboard.send(config.f2)
            """
            Changing modes
            """
            if event.code == config.select and event.state == 1:
                custom()
            if event.code == config.start and event.state == 1:
                main()
            if event.code == config.b and event.state == 1:
                battle()


def battle():
    print('Running battle mode')
    while True:
        events = get_gamepad()
        for event in events:
            """
            Function allows character to move
            It is necessary here to rotate character
            """
            if event.code == "ABS_HAT0X" and event.state == 1:
                keyboard.press(config.right)
            if event.code == "ABS_HAT0X" and event.state == 0:
                keyboard.release(config.right)
            if event.code == "ABS_HAT0X" and event.state == -1:
                keyboard.press(config.left)
            if event.code == "ABS_HAT0X" and event.state == 0:
                keyboard.release(config.left)
            if event.code == "ABS_HAT0Y" and event.state == -1:
                keyboard.press(config.up)
            if event.code == "ABS_HAT0Y" and event.state == 0:
                keyboard.release(config.up)
            if event.code == "ABS_HAT0Y" and event.state == 1:
                keyboard.press(config.down)
            if event.code == "ABS_HAT0Y" and event.state == 0:
                keyboard.release(config.down)
            """
            triggers - you can change "config.[button]" 
            for your own preferences
            """
            if event.code == config.lb and event.state == 1:
                keyboard.send(config.f3)
            if event.code == config.rb and event.state == 1:
                keyboard.send(config.f4)
            if event.code == config.rt and event.state > config.trigger_power:
                keyboard.send(config.f5)
            if event.code == config.lt and event.state > config.trigger_power:
                keyboard.send(config.f6)
            """
            buttons - you can change "config.[button]" 
            for your own preferences
            """
            if event.code == config.y and event.state == 1:
                keyboard.send(config.f7)
            if event.code == config.x and event.state == 1:
                keyboard.send(config.f8)
            if event.code == config.a and event.state == 1:
                keyboard.send(config.f9)
            """
            Changing modes
            """
            if event.code == config.select and event.state == 1:
                custom()
            if event.code == config.start and event.state == 1:
                main()
            if event.code == config.b and event.state == 1:
                main()


def custom():
    print('Running custom mode')
    while True:
        events = get_gamepad()
        for event in events:
            """
            Function allows character to move
            It is necessary here to rotate character
            """
            if event.code == "ABS_HAT0X" and event.state == 1:
                keyboard.press(config.right)
            if event.code == "ABS_HAT0X" and event.state == 0:
                keyboard.release(config.right)
            if event.code == "ABS_HAT0X" and event.state == -1:
                keyboard.press(config.left)
            if event.code == "ABS_HAT0X" and event.state == 0:
                keyboard.release(config.left)
            if event.code == "ABS_HAT0Y" and event.state == -1:
                keyboard.press(config.up)
            if event.code == "ABS_HAT0Y" and event.state == 0:
                keyboard.release(config.up)
            if event.code == "ABS_HAT0Y" and event.state == 1:
                keyboard.press(config.down)
            if event.code == "ABS_HAT0Y" and event.state == 0:
                keyboard.release(config.down)
            """
            triggers - you can change "config.[button]" 
            for your own preferences
            """
            if event.code == config.lb and event.state == 1:
                keyboard.send(config.cf1)
            if event.code == config.rb and event.state == 1:
                keyboard.send(config.cf2)
            if event.code == config.rt and event.state > config.trigger_power:
                keyboard.send(config.cf3)
            if event.code == config.lt and event.state > config.trigger_power:
                keyboard.send(config.cf4)
            """
            buttons - you can change "config.[button]" 
            for your own preferences
            """
            if event.code == config.y and event.state == 1:
                keyboard.send(config.cf5)
            if event.code == config.x and event.state == 1:
                keyboard.send(config.cf6)
            if event.code == config.a and event.state == 1:
                keyboard.send(config.cf7)
            if event.code == config.b and event.state == 1:
                keyboard.send(config.cf8)
            """
            Changing modes
            """
            if event.code == config.select and event.state == 1:
                custom()
            if event.code == config.start and event.state == 1:
                main()


"""
Prints the scan code of all currently pressed keys.
Updates on every keyboard event.
"""


# import sys
#
# sys.path.append('..')
# import keyboard
#
#
# def print_pressed_keys(e):
#     line = ', '.join(str(code) for code in keyboard._pressed_events)
#     # '\r' and end='' overwrites the previous line.
#     # ' '*40 prints 40 spaces at the end to ensure the previous line is cleared.
#     print('\r' + line + ' ' * 40, end='')
#
#
# keyboard.hook(print_pressed_keys)
# keyboard.wait()

def controller_status():
    """
    function checks for controller inputs
    """
    while True:
        events = get_gamepad()
        for event in events:
            print("code")
            print(event.code)
            print('-------------')
            print("state")
            print(event.state)


if __name__ == "__main__":
    main()
