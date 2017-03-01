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
version = 'V1.0'
credits = '©2017 Synthx\n' + color['TWITTER_BLUE'] + 'Twitter: @_Synthx' + color['DEFAULT']
printHelp = color['PURPLE'] + '''
+-------+----------------------------+
| help  | Prints this dialog         |
+-------+----------------------------+
| SSH   | Will begin ssh selection   |
+-------+----------------------------+
| clear | Clears the screen          |
+-------+----------------------------+
| exit  | Exits Easy SSH :/          |
+-------+----------------------------+
| info  | Shows credits for Easy SSH |
+-------+----------------------------+
'''
header = color['PURPLE'] + '''
 _____                  _____ _____ _   _ 
|  ___|                /  ___/  ___| | | |
| |__  __ _ ___ _   _  \ `--.\ `--.| |_| |
|  __|/ _` / __| | | |  `--. \`--. \  _  |
| |__| (_| \__ \ |_| | /\__/ /\__/ / | | |
\____/\__,_|___/\__, | \____/\____/\_| |_/
                 __/ |                    
                |___/                     
''' + color['DEFAULT'] + '''\n                        -=-=-=-=-=-=-=-=-=-=-=-=-\n                          xTools ''' + version + '''\n                          Created by ''' + color['TWITTER_BLUE'] + '''@_Synthx''' + color['DEFAULT'] + '''\n                        -=-=-=-=-=-=-=-=-=-=-=-=-
'''
os.system('clear')
print(header)
print('Type "help" to begin!')
def Main():
	global exit
	mainInput = input(color['RED'] + 'Easy SSH> ' + color['DEFAULT'])
	if mainInput.lower() == 'help':
		os.system('clear')
		print(printHelp)
		Main()
	elif mainInput == '':
		Main()
	elif mainInput == '':
while exit == False:
    Main()





