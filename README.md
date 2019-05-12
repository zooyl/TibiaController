# TibiaController

Bored of grinding hunting grounds without smile on your face?  
Maybe its time to try it out with controller instead, comfortably sitting on your couch.  
Fear no more, here it is:  
Python script made with inputs, pyautogui. Working on linux and windows.  
It's open source, everyone can see how it's made and contribute, it's not trying to hide itself or do something suspicious.  
At this moment there is no graphical user interface.  

Note:  
Right now only xbox one controller is done.

### Requirements
[Python 3](https://www.python.org/downloads/release/python-368/)  
Installed libraries from ```requirements.txt```, scripts in ```installer``` folder does it for you.  
On Linux system you also have to install ```sudo apt-get install scrot``` (required for [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/install.html))

### Basic hotkeys
```start``` - main preset  
```select``` - custom preset  

Main preset:  
Contains moving, rotating character (holding Y) and walking diagonally (bumpers and triggers)  
On ```B``` button is switch for ```combat``` preset  
```X``` is ```F1```  
```A``` is ```F2```  

Combat preset:
```B``` is switching back to main preset (by default you can only go to combat mode from main preset)  
Every button and trigger is customizable here:  
```F3-F4``` for bumpers  
```F5-F6``` for triggers  
```F7-F9``` for ```Y, X, A```  

Custom preset:  
```CF1``` for lb  
holding ```shift``` + "A" button is looting area around character (shift + right click to loot) but you have to specify your own x and y axis based on display resolution.  
There is script provided to check it in ```checking_inputs``` directory. Open terminal there and type ```python display_resolution.py```, next move mouse around and click "A" button to see current position.  
```CF3-CF4``` for triggers  
```CF5-CF6``` for ```Y, X```

```CF*``` means ```ctrl+F*```

### Config.py
Comment one that you are **not** using ```Linux settings``` or ```Windows settings``` in a file.  

 ### Windows installation  
Open ```installer``` directory and run ```windows_installer.bat```

### Running on Windows
open ```cmd``` in root directory (nice trick to run it is to type cmd in address bar and hit enter)  
and run ```python [controller_name].py```

### Linux installation

Open terminal in ```TibiaController/installer```.  
Run: ```chmod +x ./linux_installer.sh``` to give executable permission  
After that you can install script by ```./linux_installer.sh``` command in terminal.  

### Linux manual installation

If you want to install packages without installer.  
Create virtual environment on your machine, then install requirements using:
```pip install -r requirements.txt```  


### Running on Linux
In root directory  
activate venv: "source installer/venv/bin/activate"  
run script: "python [controller_name].py"  
Make sure you comment proper settings in config.py  
They are set by default for windows  
And connect your controller :)  

### Advanced customization

Additionally you can change buttons in ```[controller].py``` if you feel comfortable doing so,  
for example: change ```config.[button]``` or pyautogui [action](https://pyautogui.readthedocs.io/en/latest/keyboard.html).  
```if event.code == config.lb and event.state == 1:```  
     ```pyautogui.hotkey('ctrl', 'f4')```  

```event.state``` explanation:  
for buttons ```event.state == 1``` is clicked, while ```0``` would be released  
for x axies ```event.state == 1``` is right, while ```-1``` is left and ```0``` for release  
for y axies ```event.state == 1``` is down, while ```-1``` is up and ```0``` for release  
for triggers ```event.state > config.trigger_power``` means how far trigger has to be pushed to perform action  
 

## Additional info  
[Tibia](https://www.tibia.com/news/?subtopic=latestnews) is made by [Cipsoft](https://www.cipsoft.com/index.php/en/), all Tibia content belongs to Cipsoft.  
I do not take any responsibility and I'm not liable for any damage caused through use of this script  

## Contributing
Feel free to fork project and make pull requests

## Built With

* [Python](https://www.python.org/)
* [Inputs](https://github.com/zeth/inputs)
* [PyAutoGUI](https://github.com/asweigart/pyautogui)