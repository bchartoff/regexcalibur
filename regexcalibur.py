import globals
globals.init()

import terminaloutput
from mobs import *
from inventory import *
from screens import *

import os
modify_text_file = terminaloutput.modify_text_file



globals.active_screen = screens.startscreen

while True:
	if globals.lives == 0:
		break
	if globals.active_message:
		globals.active_message.print_output()
		raw_input(globals.active_message.prompt)
		globals.active_message = None
		continue
	else:
		screen = globals.active_screen
		screen.print_output()
		if globals.gameover:
			break
		globals.active_input = raw_input(screen.prompt)
		globals.active_screen = screen.next()
if globals.lives == 0:
 	screens.losescreen.print_output()