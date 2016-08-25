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

exploitCmds = {'runpoc', 'dump', 'getmodules', 'getpid', 'getsysinfo', 'ls'}
exploitCmd  = ''
browserPage = '/'

def runConsoleInterpretter():
	while True:
		print ">",

		command = raw_input()

		if command in exploitCmds:
			exploitCmd = command
			print "A command requiring code execution has been called. To continue the console, please refresh the page on your PS4 system..."
			break
		elif " " in command:
			if command[0:command.index(" ")] in exploitCmds:
				exploitCmd = command
				print "A command requiring code execution has been called. To continue the console, please refresh the page on your PS4 system..."
				break

		if command[0:2] == "cd":
                                global browserPage

				if command[3] == '/':
					browserPage = command[3:]
				elif command[3:5] == '..':
					pass
				elif command[3:5] == './':
					browserPage += command[4:]
				else: # Must be relative
					if browserPage[-1:] == '/':
						browserPage += command[3:]
					else:
						browserPage += '/' + command[3:]
						

                                print("Directory changed to: [" + browserPage + "]")

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
			print("cd [new dir]")
			print("clear")
			print("dump {file/module} [file name/module name/module id]")
			print("getmodules")
			print("getpid")
			print("help")
			print("ls")
			print("runpoc")
			print("\r\r")

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
		else:
			self.send_response(200);
			self.send_header("Content-type", "text/html")
			self.end_headers()

			cmdToRun = runConsoleInterpretter()

			if cmdToRun == 'ls':
				print("\r")
				print("[ PS4Console Version 1.1 - List Directory ]")
				print("\r")
				self.wfile.write("<script>var currentDir = \"" + browserPage + "\";</script>" + open('pages/ls.html').read())

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

			if cmdToRun == 'getsysinfo':
				print("\r")
				print("[ PS4Console Version 1.1 - System Information ]")
				self.wfile.write(open('pages/getsysinfo.html').read())

			if cmdToRun[0:4] == 'dump':
				print("\r")
				print("[ PS4Console Version 1.1 - Module/File Dumper ]")
				print("\r")

				if 'module' in cmdToRun:
					# List of valid modules for dumping
					validModuleNames = ["libSceSysmodule", "libSceNetCtl", "libSceRegMgr", "libSceRtc", "libScePad", "libSceOrbisCompat", "libSceSysCore", "libSceSystemService", "libSceSsl"]
					validModuleIDs	 = ["0xC", "0x1B", "0x1F", "0x20", "0x21", "0x23", "0x25", "0x26", "0x35"]

					moduleToDump = ""

					if cmdToRun[12:] in validModuleNames:
						# Loop through the array to get the index, then get the module ID from this index
						moduleIndex = -1;

						for x in range(0, len(validModuleNames)):
							if validModuleNames[x] == cmdToRun[12:]:
								moduleIndex = x
								break

						if moduleIndex != -1:
							moduleToDump = validModuleIDs[x]
						else:
							print "Module name does not have a corresponding module ID"

					elif cmdToRun[12:] in validModuleIDs:
						moduleToDump = cmdToRun[12:]

					else:
						print "You are attempting to dump an unknown or unsupported module..."

					if moduleToDump != "":
						print "Preparing to dump module with ID [" + moduleToDump + "]..."
						self.wfile.write("<script>var moduleToDump = \"" + moduleToDump + "\";</script>" + open('pages/dump-module.html').read())

				elif 'file' in cmdToRun:
					# We must open the file via syscall open, then read via syscall read
					fileToDump = browserPage + "/" + cmdToRun[10:]
					print "Preparing to dump file of name [" + fileToDump + "]..."
					self.wfile.write("<script>var fileToDump = \"" + fileToDump + "\";</script>" + open('pages/dump-file.html').read())

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

		if '/debug/file' in self.path:
			filename = self.path.split("/")[-1]

			dataString = self.rfile.read(int(self.headers['Content-length']))
			self.send_response(200)
			self.end_headers()
			f = open('Dumps/Files/' + filename, mode='wb')
			f.write(dataString)
			f.close()

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
