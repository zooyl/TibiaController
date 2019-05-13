#!/usr/bin/env bash

echo "---------------------------------------------------"
echo "This script will install:"
echo "Python, scrot (for PyAutoGUI) and virtual environment."
echo "Activate it and download required packages"
echo "---------------------------------------------------"
read -n1 -r -p "Press any key to continue"
echo
echo "Installing Python..."
sudo apt-get install python3
echo
echo "Installing virtual environment..."
sudo apt install virtualenv
echo
echo "---------------------------------------------------"
echo "Creating virtual environment in current directory"
echo "---------------------------------------------------"
echo
virtualenv -p python3 venv
source ./venv/bin/activate
# pip install -r requirements.txt
sudo apt-get install scrot
venv/bin/pip install -r ./../requirements.txt
echo "---------------------------------------------------"
echo "Installation completed"
echo "---------------------------------------------------"
echo "In root directory"
echo "activate venv: ""source installer/venv/bin/activate"""
echo "run script: ""python [controller_name].py"""
echo "---------------------------------------------------"
echo "Make sure you comment proper settings in config.py"
echo "They are set by default for windows"
echo "And connect your controller :)"
echo "---------------------------------------------------"
echo "If you want to exit just do ctrl+c or click exit"
echo "---------------------------------------------------"