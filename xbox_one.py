# Dependencies
from inputs import get_gamepad
import pyautogui

# Config settings
import config


def main():
    print('Running main mode')
    while True:
        events = get_gamepad()
        for event in events:
            """
            Function allows character to move
            """
            if event.code == config.d_pad_x_axis and event.state == 1:
                pyautogui.keyDown('right')
            if event.code == config.d_pad_x_axis and event.state == 0:
                pyautogui.keyUp('right')
            if event.code == config.d_pad_x_axis and event.state == -1:
                pyautogui.keyDown('left')
            if event.code == config.d_pad_x_axis and event.state == 0:
                pyautogui.keyUp('left')
            if event.code == config.d_pad_y_axis and event.state == -1:
                pyautogui.keyDown('up')
            if event.code == config.d_pad_y_axis and event.state == 0:
                pyautogui.keyUp('up')
            if event.code == config.d_pad_y_axis and event.state == 1:
                pyautogui.keyDown('down')
            if event.code == config.d_pad_y_axis and event.state == 0:
                pyautogui.keyUp('down')
            """
            Rotating character by holding left ctrl ("Y" in this case) -
            you can change for your own preferences
            """
            if event.code == config.y and event.state == 1:
                pyautogui.keyDown('ctrl')
            if event.code == config.y and event.state == 0:
                pyautogui.keyUp('ctrl')
            """
            triggers and bumpers - numpad walking - you can change for your own preferences
            """
            if event.code == config.lb and event.state == 1:
                pyautogui.press('num7')
            if event.code == config.rb and event.state == 1:
                pyautogui.press('num9')
            if event.code == config.rt and event.state > config.trigger_power:
                pyautogui.press('num3')
            if event.code == config.lt and event.state > config.trigger_power:
                pyautogui.press('num1')
            """
            buttons - you can change for your own preferences 
            ("Y" does rotating and "B" change mode)
            """
            if event.code == config.x and event.state == 1:
                pyautogui.press('f1')
            if event.code == config.a and event.state == 1:
                pyautogui.press('f2')
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
            """
            if event.code == config.d_pad_x_axis and event.state == 1:
                pyautogui.keyDown('right')
            if event.code == config.d_pad_x_axis and event.state == 0:
                pyautogui.keyUp('right')
            if event.code == config.d_pad_x_axis and event.state == -1:
                pyautogui.keyDown('left')
            if event.code == config.d_pad_x_axis and event.state == 0:
                pyautogui.keyUp('left')
            if event.code == config.d_pad_y_axis and event.state == -1:
                pyautogui.keyDown('up')
            if event.code == config.d_pad_y_axis and event.state == 0:
                pyautogui.keyUp('up')
            if event.code == config.d_pad_y_axis and event.state == 1:
                pyautogui.keyDown('down')
            if event.code == config.d_pad_y_axis and event.state == 0:
                pyautogui.keyUp('down')
            """
            triggers and bumpers - you can change for your own preferences
            """
            if event.code == config.lb and event.state == 1:
                pyautogui.press('f3')
            if event.code == config.rb and event.state == 1:
                pyautogui.press('f4')
            if event.code == config.rt and event.state > config.trigger_power:
                pyautogui.press('f5')
            if event.code == config.lt and event.state > config.trigger_power:
                pyautogui.press('f6')
            """
            buttons - you can change for your own preferences
            """
            if event.code == config.y and event.state == 1:
                pyautogui.press('f7')
            if event.code == config.x and event.state == 1:
                pyautogui.press('f8')
            if event.code == config.a and event.state == 1:
                pyautogui.press('f9')
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
            """
            if event.code == config.d_pad_x_axis and event.state == 1:
                pyautogui.keyDown('right')
            if event.code == config.d_pad_x_axis and event.state == 0:
                pyautogui.keyUp('right')
            if event.code == config.d_pad_x_axis and event.state == -1:
                pyautogui.keyDown('left')
            if event.code == config.d_pad_x_axis and event.state == 0:
                pyautogui.keyUp('left')
            if event.code == config.d_pad_y_axis and event.state == -1:
                pyautogui.keyDown('up')
            if event.code == config.d_pad_y_axis and event.state == 0:
                pyautogui.keyUp('up')
            if event.code == config.d_pad_y_axis and event.state == 1:
                pyautogui.keyDown('down')
            if event.code == config.d_pad_y_axis and event.state == 0:
                pyautogui.keyUp('down')
            """
            triggers and bumpers - you can change hotkey
            for your own preferences
            """
            if event.code == config.lb and event.state == 1:
                pyautogui.hotkey('ctrl', 'f1')
            if event.code == config.rb and event.state == 1:
                pyautogui.keyDown('shift')
            if event.code == config.rb and event.state == 0:
                pyautogui.keyUp('shift')
            if event.code == config.rt and event.state > config.trigger_power:
                pyautogui.hotkey('ctrl', 'f3')
            if event.code == config.lt and event.state > config.trigger_power:
                pyautogui.hotkey('ctrl', 'f4')
            """
            buttons - you can change hotkey for your own preferences
            "B" is for changing mode
            """
            if event.code == config.y and event.state == 1:
                pyautogui.hotkey('ctrl', 'f5')
            if event.code == config.x and event.state == 1:
                pyautogui.hotkey('ctrl', 'f6')
            if event.code == config.a and event.state == 1:
                pyautogui.hotkey('ctrl', 'f7')
            if event.code == config.b and event.state == 1:
                pyautogui.hotkey('ctrl', 'f8')
            """
            Changing modes
            """
            if event.code == config.select and event.state == 1:
                custom()
            if event.code == config.start and event.state == 1:
                main()
            if event.code == config.b and event.state == 1:
                battle()


if __name__ == "__main__":
    main()
