"""
Here you can find some snippets for customizing your experience
All you have to do is configure, copy and paste it in [controller_name].py file
in which preset best suits your needs.
Feel free to implement your own in [controller_name].py
"""

"""
Collect Loot around character, you have to specify your own display resolution here
Loot setting - Shift + right mouse click
"RB" button is holding shift while "A" button is right clicking around character position
"""
if event.code == config.rb and event.state == 1:
    pyautogui.keyDown('shift')
if event.code == config.rb and event.state == 0:
    pyautogui.keyUp('shift')
"""
Mouse clicking down below
"""
if event.code == config.a and event.state == 1:
    # collect right loot (North-East, East)
    pyautogui.click(x=939, y=415, button='right')
    pyautogui.click(x=936, y=475, button='right')
    # collect left loot (South-West, West)
    pyautogui.click(x=805, y=479, button='right')
    pyautogui.click(x=804, y=545, button='right')
    # collect top loot (North-West, North)
    pyautogui.click(x=812, y=415, button='right')
    pyautogui.click(x=879, y=417, button='right')
    # collect bottom loot (South-East, South)
    pyautogui.click(x=871, y=539, button='right')
    pyautogui.click(x=940, y=543, button='right')

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
