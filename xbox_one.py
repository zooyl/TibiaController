from inputs import get_gamepad
import keyboard


def controller_status():
    """
    check for controller inputs
    """
    while True:
        events = get_gamepad()
        for event in events:
            print("code")
            print(event.code)
            print('-------------')
            print("state")
            print(event.state)


def main():
    while True:
        events = get_gamepad()
        for event in events:
            """
            Walking function
            D-pad buttons in order: right, left, up, down
            It allows character to move
            Player can hold button down to run straight forward
            """
            if event.code == "ABS_HAT0X" and event.state == 1:
                keyboard.press(106)
            if event.code == "ABS_HAT0X" and event.state == 0:
                keyboard.release(106)
            if event.code == "ABS_HAT0X" and event.state == -1:
                keyboard.press(105)
            if event.code == "ABS_HAT0X" and event.state == 0:
                keyboard.release(105)
            if event.code == "ABS_HAT0Y" and event.state == -1:
                keyboard.press(103)
            if event.code == "ABS_HAT0Y" and event.state == 0:
                keyboard.release(103)
            if event.code == "ABS_HAT0Y" and event.state == 1:
                keyboard.press(108)
            if event.code == "ABS_HAT0Y" and event.state == 0:
                keyboard.release(108)
            """
            Rotating character by holding left ctrl
            """
            if event.code == "BTN_WEST" and event.state == 1:
                keyboard.press(29)
            if event.code == "BTN_WEST" and event.state == 0:
                keyboard.release(29)
            """
            numpad walking
            """
            if event.code == "BTN_TL" and event.state == 1:
                keyboard.send(71)
            if event.code == "BTN_TR" and event.state == 1:
                keyboard.send(73)
            if event.code == "ABS_RZ" and event.state > 1000:
                keyboard.press_and_release(81)
            if event.code == "ABS_Z" and event.state > 1000:
                keyboard.press_and_release(79)
            """
            Change to combat mode
            """
            if event.code == "BTN_EAST" and event.state == 1:
                combat()


def combat():
    while True:
        events = get_gamepad()
        for event in events:
            """
            D-pad buttons in order: right, left, up, down
            It allows character to move
            Player can hold button down to run straight forward
            """
            if event.code == "ABS_HAT0X" and event.state == 1:
                keyboard.press(106)
            if event.code == "ABS_HAT0X" and event.state == 0:
                keyboard.release(106)
            if event.code == "ABS_HAT0X" and event.state == -1:
                keyboard.press(105)
            if event.code == "ABS_HAT0X" and event.state == 0:
                keyboard.release(105)
            if event.code == "ABS_HAT0Y" and event.state == -1:
                keyboard.press(103)
            if event.code == "ABS_HAT0Y" and event.state == 0:
                keyboard.release(103)
            if event.code == "ABS_HAT0Y" and event.state == 1:
                keyboard.press(108)
            if event.code == "ABS_HAT0Y" and event.state == 0:
                keyboard.release(108)
            """
            test
            """
            if event.code == "BTN_WEST" and event.state == 1:
                keyboard.send('f1')
            if event.code == "BTN_NORTH" and event.state == 1:
                keyboard.send('f2')
            if event.code == "BTN_SOUTH" and event.state == 1:
                keyboard.send('f3')
            # if event.code == "BTN_EAST" and event.state == 1:
            #     keyboard.send('f4')
            """
            change to walking mode
            """
            if event.code == "BTN_EAST" and event.state == 1:
                main()


if __name__ == "__main__":
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

"""
Shortcuts for keys

left ctrl = 29
left shift = 42
left alt = 56

BTN_START = start
BTN_SELECT = select

up - 103
left - 105
down - 108
right - 106
numpad 1 = 79
numpad 3 = 81
numpad 7 - 71
numpad 9 = 73

BTN_WEST = y
BTN_NORTH = x
BTN_SOUTH = a 
BTN_EAST = b

ABS_Z = lt
ABS_RZ = rt
BTN_TL = lb
BTN_TR = rb
"""
