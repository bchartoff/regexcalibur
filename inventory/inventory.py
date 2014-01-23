import globals
import sys, os
import terminaloutput
modify_text_file = terminaloutput.modify_text_file


class Inventory:
	val = 0
	art = ""
	def __init__(self,val):
		self.val = val
		self.art = modify_text_file("inventory/art/inv%d_art.txt"%val)
		self.desc = modify_text_file("inventory/descriptions/inv%d_description.txt"%val)