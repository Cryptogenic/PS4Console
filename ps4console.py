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

exploitCmds = {'runpoc', 'dump', 'getmodules', 'getpid', 'getsysinfo'}
exploitCmd  = ''
exploitPage = ''

def runConsoleInterpretter():
	while True:
		print ">",

		command = raw_input()

		if command in exploitCmds:
			exploitCmd = command
			print "A command requiring code execution has been called. To continue the console, please refresh the page on your PS4 system..."
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
			print("Commands marked with a '!!!' are currently not functional.")
			print("\r\r")
			print("List of commands:")
			print("-")
			print("authors")
			print("clear")
			print("dump")
			print("!!! getaddress {vtable/webkit/[module ID]}")
			print("getmodules")
			print("getpid")
			print("!!! getsysinfo")
			print("!!! getversion {webkit/firmware}")
			print("help")
			print("runpoc")
			print("shutdown (server, not system)")
			print("\r\r")

		if command == "shutdown":
			print("Goodbye . . .")
			os._exit(0)

	if exploitCmd != '':
		return exploitCmd

	return

class PS4Console(SimpleHTTPServer.SimpleHTTPRequestHandler):

	def do_GET(self):
		if '/scripts/' in self.path:
			self.send_response(200);
			self.send_header("Content-type", "text/html")
			self.end_headers()
			path = self.path[1:]
			self.wfile.write(open(path).read())
		elif 'moduleToDump.txt' in self.path:
			self.send_response(200)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write(open("moduleToDump.txt").read())
		else:
			self.send_response(200);
			self.send_header("Content-type", "text/html")
			self.end_headers()

			cmdToRun = runConsoleInterpretter()

			if cmdToRun == 'runpoc':
				print("\r")
				print("[ PS4Console Version 1.1 - POC Test ]")
				print("\r")
				self.wfile.write(open('pages/runpoc.html').read())

			if cmdToRun == 'getmodules':
				print("\r")
				print("[ PS4Console Version 1.1 - Module Information ]")
				print("\r")
				self.wfile.write(open('pages/sysinfo.html').read())

			if cmdToRun == 'getpid':
				print("\r")
				print "One of the two WebKit PID's is:",
				self.wfile.write(open('pages/getpid.html').read())

			# Here we will have sub-input for parameters
			if cmdToRun == 'dump':
				print("\r")
				print("[ PS4Console Version 1.1 - Module Dumper ]")
				print("\r")

				print "Enter the name or ID (including 0x prefix) of the module you wish to dump: ",

				nameModule = raw_input()

				if nameModule == 'libSceSysmodule' or nameModule == '0xc':
					self.wfile.write(open('pages/dumping/dump-sysmodule.html').read())
				elif nameModule == 'libSceNetCtl' or nameModule == '0x1b':
					self.wfile.write(open('pages/dumping/dump-netctl.html').read())
				elif nameModule == 'libSceRegMgr' or nameModule == '0x1f':
					self.wfile.write(open('pages/dumping/dump-regmgr.html').read())
				elif nameModule == 'libSceRtc' or nameModule == '0x20':
					self.wfile.write(open('pages/dumping/dump-scertc.html').read())
				elif nameModule == 'libScePad' or nameModule == '0x21':
					self.wfile.write(open('pages/dumping/dump-scepad.html').read())
				elif nameModule == 'libSceOrbisCompat' or nameModule == '0x23':
					self.wfile.write(open('pages/dumping/dump-orbis.html').read())
				elif nameModule == 'libSceSysCore' or nameModule == '0x25':
					self.wfile.write(open('pages/dumping/dump-syscore.html').read())
				elif nameModule == 'libSceSystemService' or nameModule == '0x26':
					self.wfile.write(open('pages/dumping/dump-sysserv.html').read())
				elif nameModule == 'libSceSsl' or nameModule == '0x35':
					self.wfile.write(open('pages/dumping/dump-scessl.html').read())
				else:
					print "You are attempting to dump an unknown or unsupported module..."

	def do_POST(self):
		if '/debug/log' in self.path:
			data_string = self.rfile.read(int(self.headers['Content-Length']))
			self.send_response(200)
			self.end_headers()
			print data_string

		if '/debug/bin' in self.path:
			filename = self.path.split("/")[-1]

			dataString = self.rfile.read(int(self.headers['Content-length']))
			self.send_response(200)
			self.end_headers()
			f = open('Dumps/Modules/' + filename, mode='wb')
			f.write(dataString)
			f.close()

			print 'Module has been dumped to %s' % filename

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
