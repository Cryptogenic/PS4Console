# PS4Console
PS4Console is a project that is meant to be a successor of the PS4 Playground for 3.55. It is a python-based program that can be run on any Linux/Windows/Mac system and allows you to interface with the PlayStation 4 with the 3.55 exploit. The program simulates a terminal-like environment that allows you to send commands to the exploit being ran on the PS4, almost as if you were in the terminal. The program automatically runs fakedns.py when it is initiated, so using the User Guide would be the quickest and easiest way to use PS4Console.

# PS4Console vs PS4-Playground 3.55
Many may wonder what the difference is and why I'd start this new project. The reason is, PS4 Playground is a fun project to use through your web browser if you wish not to use the computer other than hosting the server, but it was very unstable and not much could be done with it as the exploit would destabalize WebKit, which PS4 Playground needs to operate.

PS4Console is an idea that allows you to interact with the PS4 in a terminal-like design and send commands to it. The WebKit process will always crash, but information is printed/modules are dumped in the terminal, so WebKit being unstable isn't a big issue. This should allow us to do more in the future, such as have a much more stable file browser and such.

# Usage
You can run PS4Console in your command-prompt or terminal via the following command (Python 2.7):

```
python ps4console.py
```

Ensure you're not running any processes on port 80 such as Apache, as PS4Console uses this port to operate. You must also setup your dns.conf file for fakedns.py and point your PS4's DNS setting to your computer's IP address (can be found via ipconfig on windows or ifconfig on linux/mac).

# Latest Version
The latest version is 1.0. Module dumping has been partially implemented, as well as module information and PID fetching. More commands will be implemented in the near future, as well as completed module dumping capability.

# Notes
The exploit will not run correctly all of the time. If it doesn't work, just keep trying until it does, it shouldn't take long.

---

Many are seeing a blank screen on their PS4 and they're thinking something is wrong. This is completely fine and expected, as long as the '>' appears in the terminal/command prompt on ps4console.py, you are good to run commands. The pages ps4console serves does not have any markup for styling. If you cannot get the '>' to appear, just refresh the page on the PS4 or press "OK" if you have a segmentation fault (not enough memory prompt).

---

Module dumping is still not completely supported. Only most of the modules loaded by WebKit are currently supported, WebKit has not been included in v1.0 as I want to clean up how it works a bit more before that (it's a little inefficient at the moment).

---

If you're on a linux system, you may need root permissions to run PS4Console on port 80, so you may need to run it via:
```
sudo python ps4console.py
```

Even after shutting down the program via shutdown command (this actually won't seem to occur if you use ctrl + c), the service will still run on port 53/port 80. To fix this, you can use the following command for Linux:
```
sudo kill `sudo lsof -t -i:80`
sudo kill `sudo lsof -t -i:53`
```

Similarily, if you run into this problem on Windows, you can use the following commands:
```
netstat -o -n -a | findstr 0.0:3000
```

This will return something like TCP    0.0.0.0:3000      0.0.0.0:0              LISTENING       [PID], using the PID given, run:
```
taskkill /F /PID [PID FROM ABOVE COMMAND]
```

I will soon implement a fix for this.

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



