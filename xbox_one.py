from inputs import get_gamepad
import keyboard
import config_linux


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
            Function allows character to move
            It is necessary here to rotate character
            """
            if event.code == "ABS_HAT0X" and event.state == 1:
                keyboard.press(config_linux.right)
            if event.code == "ABS_HAT0X" and event.state == 0:
                keyboard.release(config_linux.right)
            if event.code == "ABS_HAT0X" and event.state == -1:
                keyboard.press(config_linux.left)
            if event.code == "ABS_HAT0X" and event.state == 0:
                keyboard.release(config_linux.left)
            if event.code == "ABS_HAT0Y" and event.state == -1:
                keyboard.press(config_linux.up)
            if event.code == "ABS_HAT0Y" and event.state == 0:
                keyboard.release(config_linux.up)
            if event.code == "ABS_HAT0Y" and event.state == 1:
                keyboard.press(config_linux.down)
            if event.code == "ABS_HAT0Y" and event.state == 0:
                keyboard.release(config_linux.down)
            """
            Rotating character by holding left ctrl
            """
            if event.code == config_linux.y and event.state == 1:
                keyboard.press(config_linux.left_ctrl)
            if event.code == config_linux.y and event.state == 0:
                keyboard.release(config_linux.left_ctrl)
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
            Changing modes
            """
            if event.code == "BTN_SELECT" and event.state == 1:
                casual()
            if event.code == "BTN_START" and event.state == 1:
                main()
            if event.code == "BTN_EAST" and event.state == 1:
                combat()


def combat():
    while True:
        events = get_gamepad()
        for event in events:
            """
            Function allows character to move
            It is necessary here to rotate character
            """
            if event.code == "ABS_HAT0X" and event.state == 1:
                keyboard.press(config_linux.right)
            if event.code == "ABS_HAT0X" and event.state == 0:
                keyboard.release(config_linux.right)
            if event.code == "ABS_HAT0X" and event.state == -1:
                keyboard.press(config_linux.left)
            if event.code == "ABS_HAT0X" and event.state == 0:
                keyboard.release(config_linux.left)
            if event.code == "ABS_HAT0Y" and event.state == -1:
                keyboard.press(config_linux.up)
            if event.code == "ABS_HAT0Y" and event.state == 0:
                keyboard.release(config_linux.up)
            if event.code == "ABS_HAT0Y" and event.state == 1:
                keyboard.press(config_linux.down)
            if event.code == "ABS_HAT0Y" and event.state == 0:
                keyboard.release(config_linux.down)
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
            Changing modes
            """
            if event.code == "BTN_SELECT" and event.state == 1:
                casual()
            if event.code == "BTN_START" and event.state == 1:
                main()
            if event.code == "BTN_EAST" and event.state == 1:
                main()


def casual():
    while True:
        events = get_gamepad()
        for event in events:
            """
            Function allows character to move
            It is necessary here to rotate character
            """
            if event.code == "ABS_HAT0X" and event.state == 1:
                keyboard.press(config_linux.right)
            if event.code == "ABS_HAT0X" and event.state == 0:
                keyboard.release(config_linux.right)
            if event.code == "ABS_HAT0X" and event.state == -1:
                keyboard.press(config_linux.left)
            if event.code == "ABS_HAT0X" and event.state == 0:
                keyboard.release(config_linux.left)
            if event.code == "ABS_HAT0Y" and event.state == -1:
                keyboard.press(config_linux.up)
            if event.code == "ABS_HAT0Y" and event.state == 0:
                keyboard.release(config_linux.up)
            if event.code == "ABS_HAT0Y" and event.state == 1:
                keyboard.press(config_linux.down)
            if event.code == "ABS_HAT0Y" and event.state == 0:
                keyboard.release(config_linux.down)
            """
            Changing modes
            """
            if event.code == "BTN_SELECT" and event.state == 1:
                casual()
            if event.code == "BTN_START" and event.state == 1:
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


"""
