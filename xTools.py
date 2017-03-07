##################################################################################
#  ©2017 Synthx                                                                  #
#  You may not redistribute as yours unless you have written consent from Synthx #
#  Twitter: @_synthx                                                             #
#  Email: synthx@protonmail.com or synthx01@gmail.com                            #
##################################################################################

import readline # arrow keys
import os # This imports your OS.
exit = False
color = {
    'RED'             : '\033[1;91m',
    'UNDERLINE_PURPLE' : '\033[4;34m',
    'GREEN'           : '\033[1;92m',
    'YELLOW'          : '\033[1;33m',
    'CYAN'            : '\033[0;36m',
    'PURPLE'            : '\033[0;34m',
    'MAGENTA'         : '\033[0;35m',
    'DEFAULT'         : '\033[0m',
    'TWITTER_BLUE'            : '\033[38;5;33m',
}
pythonVersions = '\n[1]python2\n[2]python3.5.2'
toolList = '\n[1]Folder Locker\n[2]Easy SSH'
listTools = '''
+----------------+
| Folder Locker  |
+----------------+
| Easy SSH       |
+----------------+
'''  + color['RED'] + '[MORE COMING SOON!]' + color['DEFAULT']
exitSentence = color['RED'] + '[Now Exiting!] ' + color['DEFAULT'] + 'xTools\n'
credits = '©2017 Synthx\n' + color['TWITTER_BLUE'] + 'Twitter: @_Synthx' + color['DEFAULT'] + '\n@danbatiste\n@NyteLife26'
printHelp = color['MAGENTA'] + '''
+------------+---------------------------------------+
| clear      |  Clears the screen!                   |
+------------+---------------------------------------+
| exit       |  Exits xTools :/                      |
+------------+---------------------------------------+
| help       |  Shows this dialog                    |
+------------+---------------------------------------+
| open tool  |  Lets you choose what tool too open   |
+------------+---------------------------------------+
| tools      |  Shows the list of tools              |
+------------+---------------------------------------+
| info       |  Shows credits for xTools             |
+------------+---------------------------------------+
| bash       |  Opens a bash session to run commands |
+------------+---------------------------------------+
''' + color['DEFAULT']
header = color['YELLOW'] + '''
                        ___________            __          
                 ___  __\__    ___/___   ____ |  |   ______
                 \  \/  / |    | /  _ \ /  _ \|  |  /  ___/
                  >    <  |    |(  <_> |  <_> )  |__\___ \ 
                 /__/\_ \ |____| \____/ \____/|____/____  >
                       \/                               \/                            ''' + color['DEFAULT'] + '''\n                            +-----------------------+\n                            |  Created by ''' + color['TWITTER_BLUE'] + '''@_Synthx''' + color['DEFAULT'] + '''  |\n                            +-----------------------+
'''
os.system('clear')
print(header + 'Type "help" to begin!\n')
def Main():
	global exit
	mainInput = input(color['PURPLE'] + 'xTools> ' + color['DEFAULT'])
	if mainInput.lower() == 'help':
		os.system('clear')
		print(printHelp)
		Main()
	elif mainInput == '':
		Main()
	elif mainInput.lower() == 'open tool':
		os.system('clear')
		print(header + 'Which tool would you like to open?' + toolList)
		toolOpen()
	elif mainInput.lower() == 'exit':
		os.system('clear')
		print(exitSentence)
		exit = True
	elif mainInput.lower() == 'info':
		os.system('clear')
		print(header + '\n' + credits)
		Main()
	elif mainInput.lower() == 'clear':
		os.system('clear')
		print(header)
		Main()
	elif mainInput.lower() == 'tools':
		os.system('clear')
		print(listTools)
		Main()
	elif mainInput.lower() == 'bash':
		os.system('clear')
		print(header + 'Type "' + color['MAGENTA'] + 'exit' + color['DEFAULT'] + '" to end the bash session!')
		bashSession()
	elif mainInput.lower() == 'python':
		os.system('clear')
		print(header + 'Which version of python?\n' + pythonVersions)
		pythonSession()
	else:
		os.system('clear')
		print(header + color['RED'] + '[ERROR] COMMAND "' + mainInput + '" NOT FOUND\n' + color['DEFAULT'] + 'PLEASE USE A PROPER COMMAND!\n')
		Main()
def toolOpen():
	mainInput = input(color['PURPLE'] + '> ' + color['DEFAULT'])
	if mainInput == '':
		toolOpen()
	elif mainInput == '1':
		os.system('clear')
		os.system('python3 ./tools/folder-locker.py')
		print(header)
		Main()
	elif mainInput == '2':
		os.system('clear')
		print(color['RED'] + 'Easy SSH is not ready yet!!!' + color['DEFAULT'])
		os.system('python3 ./tools/easy_ssh.py')
		print(header)
		Main()
	elif mainInput.lower() == 'cancel':
		os.system('clear')
		print(header)
		Main()
	else:
		os.system('clear')
		print(header + color['RED'] + '\n[ERROR]' + color['DEFAULT'] + 'That is not an option. If you would like to cancel please type "cancel".\nOtherwise, please select a number from the list!\n' + toolList)
		toolOpen()
def bashSession():
	os.system('bash;clear')
	print(header)
	Main()
def pythonSession():
	mainInput = input(color['PURPLE'] + '> ' + color['DEFAULT'])
	if mainInput == '':
		pythonSession()
	elif mainInput == '1':
		os.system('clear;python;clear')
		print(header)
		Main()
	elif mainInput == '2':
		os.system('clear;python3;clear')
		print(header)
		Main()
	elif mainInput.lower() == 'cancel':
		os.system('clear')
		print(header)
		Main()
	else:
		os.system('clear')
		print(header + color['RED'] + '[ERROR]' + color['DEFAULT'] + 'That is not an option. If you would like to cancel please type "cancel".\nOtherwise, please select a number from the list!\n' + pythonVersions)
		pythonSession()
while exit == False:
    Main()