from inputs import get_gamepad
import pyautogui


def resolution():
    print('Checking resolution')
    while True:
        events = get_gamepad()
        for event in events:
            if event.code == "BTN_SOUTH" and event.state == 1:
                print(pyautogui.position())


if __name__ == "__main__":
    resolution()
