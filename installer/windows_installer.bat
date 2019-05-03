
@echo "---------------------------------------------------"
@echo "Install python first if you already don't have it"
@echo "you can download it from official page:"
@echo "https://www.python.org/downloads/release/python-368/"
@echo "To check if you already have it installed"
@echo "in cmd type: 'python --version' (works for 3.6+)"
@echo "Then run this installer"
@echo "This script will install required packages"
@echo "---------------------------------------------------"
pause
pip install -r ./../requirements.txt
@echo "---------------------------------------------------"
@echo "Installation completed"
@echo "---------------------------------------------------"
@echo "If you want to run controller:"
@echo "open cmd in project root directory"
@echo "run script by command: 'python [controller_name].py'"
@echo "Make sure you comment proper settings in config.py"
@echo "And connect your controller :)"
@echo "If you want to stop controller just do ctrl+c"
@echo "---------------------------------------------------"
pause
