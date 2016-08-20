#!/usr/bin/python

import BaseHTTPServer
import json
import SocketServer

import SimpleHTTPServer

import platform
import subprocess
import os
import sys

DEVNULL = open(os.devnull, 'wb')

exploitCmds = {'runpoc', 'dump', 'getmodules', 'getpid'}
exploitCmd 	= ''

def runExploitCommand():
	print "A command requiring code execution has been called. To continue the console, please refresh the page on your PS4 system..."
	pass

def runConsoleInterpretter():
	while True:
		print ">",

		command = raw_input()

		if command in exploitCmds:
			exploitCmd = command
			break

		if command == "authors":
			print("\r")
			print("[ PS4Console Version 1.1 - Authors ]")
			print("\r")
			print("Specter")
			print("Fire30")
			print("Maxton")
			print("Xerpi")
			print("\r\r")

		if command == "clear":
			if platform.system() == 'Windows':
				os.system('cls')
			else:
				os.system('clear')

		if command == "help":
			print("\r")
			print("[ PS4Console Version 1.1 - Help Center ]")
			print("\r")
			print("List of available commands:")
			print("-")
			print("authors")
			print("clear")
			print("dump [module ID] [file name]")
			print("getaddress {vtable/webkit/[module ID]}")
			print("getmodules")
			print("getpid")
			print("getsysinfo")
			print("getversion {webkit/firmware}")
			print("help")
			print("runpoc")
			print("shutdown (server, not system)")
			print("\r\r")

		if command == "shutdown":
			print("Goodbye . . .")
			os._exit(0)

	if exploitCmd != '':
		runExploitCommand()

	return

class PS4Console(SimpleHTTPServer.SimpleHTTPRequestHandler):

	def do_GET(self):
		if '/scripts/' in self.path:
			self.send_response(200);
			self.send_header("Content-type", "text/html")
			self.end_headers()
			path = self.path[1:]
		else:
			self.send_response(200);
			self.send_header("Content-type", "text/html")
			self.end_headers()
			runConsoleInterpretter()
		pass

	def do_POST(self):
		pass

	def log_message(self, format, *args):
		return

if __name__ == '__main__':
	server_class = BaseHTTPServer.HTTPServer
	httpd = server_class(('0.0.0.0', 80), PS4Console)

	print("[ Welcome to PS4Console ]")
	print("Starting fakedns.py. . .")

	subprocess.Popen(["python", "fakedns.py", "-c", "dns.conf"], stdout=DEVNULL, stderr=DEVNULL)

	if platform.system() == 'Windows':
		os.system("cls")
	else:
		os.system("clear")

	print("Go to the web browser on the PS4/User Guide and go to the landing page to issue commands. To continue issuing commands, hit OK when WebKit crashes...\r\n");

	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass

	httpd.server_close()
