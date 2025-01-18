import os
import subprocess
import sys

def check_virtualenv():
    if not hasattr(sys, 'real_prefix') and (not hasattr(sys, 'base_prefix') or sys.base_prefix == sys.prefix):
        print("Creating a virtual environment...")
        subprocess.check_call([sys.executable, "-m", "venv", "venv"])

def install_dependencies():
    print("Installing dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

if __name__ == "__main__":
    check_virtualenv()
    install_dependencies()
    print("Environment setup complete. You can now run the application!")
