# TibiaController

Boring of grinding hunting grounds without smile on your face?  
Maybe its time to try it out with controller instead, comfortably sitting on your couch.  
Fear no more, here it is:  
Python script with only two libraries, working on linux and windows.  
It's open source, everyone can see how it's made and contribute, it's not trying to hide itself or do something suspicious.  
At this moment there is no graphical user interface.  

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
```CF1-CF2``` for bumpers
```CF3-CF4``` for triggers  
```CF5-CF8``` for ```Y, X, A, B```


### Config.py
Comment one that you are **not** using ```Linux settings``` or ```Windows settings``` in a file.  
It's customizable if you want to make it feel a little bit personal.  
All you have to do is change ```System configuration``` (f1-f9 or cf1-cf8) in ```config.py```  
  
Note:  
Right now only xbox one controller is done.

### Linux installation

Open terminal in ```TibiaController/installer```.  
Run: ```chmod +x ./linux_installer.sh``` to give executable permission  
After that you can install script by ```./linux_installer.sh``` command in terminal.  

### Linux manual installation

If you want to install packages without installer.  
Create virtual environment on your machine, then install requirements using:
```pip install -r requirements.txt```  

### Windows installation  
work in progress

### Running on Linux
If you want to run script on linux you have to be logged in as sudo in terminal  
TO DO so:  
open terminal in project root directory  
switch to sudo by: "sudo su"  
activate venv: "source installer/venv/bin/activate"  
run script: "python [controller_name].py"  
Make sure you comment proper settings in config.py  
They are set by default for windows  
And connect your controller :)  

### Advanced customization

Additionally you can change buttons in ```[controller].py``` if you feel comfortable doing so,  
for example: change ```config.[button]``` variable with existing or created one in ```config.py```  
```if event.code == config.lb and event.state == 1:```  
     ```keyboard.send(config.numpad_7)```  

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
* [Keyboard](https://github.com/boppreh/keyboard)
