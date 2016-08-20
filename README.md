# PS4Console
PS4Console is a project that is meant to be a successor of the PS4 Playground for 3.55. It is a python-based program that can be run on any Linux/Windows/Mac system and allows you to interface with the PlayStation 4 with the 3.55 exploit. The program simulates a terminal-like environment that allows you to send commands to the exploit being ran on the PS4, almost as if you were in the terminal. The program automatically runs fakedns.py when it is initiated, so using the User Guide would be the quickest and easiest way to use PS4Console.

# Usage
You can run PS4Console in your command-prompt or terminal via the following command (Python 2.7):

```
python ps4console.py
```

Ensure you're not running any processes on port 80 such as Apache, as PS4Console uses this port to operate. You must also setup your dns.conf file for fakedns.py and point your PS4's DNS setting to your computer's IP address (can be found via ipconfig on windows or ifconfig on linux/mac).

# Latest Version
The latest version is 0.1. More of the project will be implemented in future commits.

# Notes
The exploit will not run correctly all of the time. If it doesn't work, just keep trying until it does, it shouldn't take long.

If you're on a linux system, you may need root permissions to run PS4Console on port 80, so you may need to run it via:
```
sudo python ps4console.py
```

# Documentation
Documentation is currently not existant for PS4Console, however it will be implemented in a future commit.

# Special Thanks To
Fire30 - The porting of the WebKit Exploit to PS4, as well as assistance

Xerpi - Functions in his POC edit that I ported over (these functions made things way easier and more efficient)

XYZ - The original exploit for PSVita 3.60

CTurt - Research done with 1.76

XorLoser - File sizes and headers for dumping modules

Maxton - Assistance in development

Red-EyeX32 - Assistance in development


