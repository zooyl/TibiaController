"""
Here you can find some snippets for customizing your experience
All you have to do is configure, copy and paste it in [controller_name].py file
in which preset best suits your needs.
Feel free to implement your own in [controller_name].py
"""
"""
Right analog - beta
"""
if event.code == config.right_stick_x_axis and 25000 < event.state:
    pyautogui.hotkey('shift', 'f1')
if event.code == config.right_stick_x_axis and event.state < -25000:
    pyautogui.hotkey('shift', 'f2')
if event.code == config.right_stick_y_axis and 20000 < event.state:
    pyautogui.hotkey('shift', 'f3')
if event.code == config.right_stick_y_axis and event.state < -25000:
    pyautogui.hotkey('shift', 'f4')
"""
Left analog - beta
"""
if event.code == config.left_stick_x_axis and 25000 < event.state:
    pyautogui.hotkey('shift', 'f5')
if event.code == config.left_stick_x_axis and event.state < -25000:
    pyautogui.hotkey('shift', 'f6')
if event.code == config.left_stick_y_axis and 20000 < event.state:
    pyautogui.hotkey('shift', 'f7')
if event.code == config.left_stick_y_axis and event.state < -25000:
    pyautogui.hotkey('shift', 'f8')
"""
holding lb with buttons to do 'ctrl+shift+f*' hotkey
you have to change existing button in [controller_name].py in desired preset
(state 1 is for pressed and 0 for release)
"""
if event.code == config.lb and event.state == 1:
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
if event.code == config.lb and event.state == 0:
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')
