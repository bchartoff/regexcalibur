import re
import globals
import terminaloutput
from mobs import *
from inventory import *
modify_text = terminaloutput.modify_text
modify_text_file = terminaloutput.modify_text_file




def on_load(load_message):
	load_message = load_message[0]
	ismob = re.match('mob(\d*)',load_message)
	isinv = re.match('inv(\d*)',load_message)
	if ismob:
		globals.active_hit_strings = (globals.hit_strings[int(ismob.group(1))])
		globals.active_miss_strings = (globals.miss_strings[int(ismob.group(1))])
		globals.active_hit_mob = Mob("hit",int(ismob.group(1)))
		globals.active_miss_mob = Mob("miss",int(ismob.group(1)))
	elif isinv:
		globals.active_inventory.append(globals.inventory[int(isinv.group(1))])
		try:
			globals.active_screen = mobscreens[int(isinv.group(1))]
		except IndexError:
			globals.active_screen = winscreen
			globals.gameover = True


def eval_input(inp):
	kind = globals.active_screen.kind
	if inp == "i":
		out = []
		for inv in globals.active_inventory:
			for i in inv.art:
				out.append(i)
			for i in inv.desc:
				out.append(i)
		return out
	elif inp == "it":
		out = []
		for invt in globals.active_inventory:
			for i in invt.desc:
				out.append(i)
			out.append('\r')
		return out
	elif inp == "l":
		return ["\n\t"+modify_text("#R<3R# ")*globals.lives+"\n"]
	elif inp == "h":
		return modify_text_file("screens/help.txt")
	elif miss(inp) and kind == "mob":
		globals.lives -= 1
		#print ["miss"] + globals.active_miss_strings
		#print ["miss strings: "]+globals.hit_strings
		return miss(inp)
	elif kind == "mob":
		globals.active_screen = invscreens[len(globals.active_inventory)]
		globals.active_screen.print_output()
		return [""]
	elif kind == "inv":
		globals.active_screen = mobscreens[globals.active_hit_mob.val]
	elif kind == "start1":
		globals.active_screen = startscreen2
		return None
	elif kind == "start2":
		globals.active_screen = mobscreens[0]
		return None
	else:
		return ["Yargh, I don't know how to %s"%inp]

def miss(inp):
	inp = re.compile(inp)
	for s in globals.active_miss_strings:
		if re.match(inp,s):
			return ["\n\tTragedy! Your regex hit a woodland creature by matching "+s,"","\t"+modify_text("#R<3R# ")*globals.lives+"\n"]
	for s in globals.active_hit_strings:
		if re.match(inp,s):
			continue
		else:
			return ["\n\tEek! Your regex failed to hit "+s+ " and he ate you up.","","\t"+modify_text("#R<3R# ")*globals.lives+"\n"]
	return False

class Screen:
	output = []
	load_function = None
	load_function_args = []
	prompt = "\t"
	def __init__(self,kind,prompt,output,load_function,*load_function_args):
		self.load_function = load_function
		self.load_function_args = load_function_args
		self.output = output
		self.kind = kind
		self.first = True
		self.prompt += prompt
	def next(self):
		output = eval_input(globals.active_input)
		if output == None:
			globals.active_message = None
			return globals.active_screen
		else:
			if globals.active_input != "h":
				globals.active_message = Message(output,modify_text("\t\t\t\t----#BPress Any Key to ContinueB#----"))
			else:
				globals.active_message = Message(output,"\t")
			return globals.active_screen
	def print_output(self):
		if self.first:
			self.load_function(self.load_function_args)
			self.first = False
		for line in self.output:
			print "\t" + line

class Message:
	prompt = ""
	def __init__(self,output,prompt):
		self.output = output
		self.prompt = prompt
	def print_output(self):
		for line in self.output:
			print "\t" + line

def dummy(val):
	pass


startscreen = Screen("start1","",modify_text_file("screens/help.txt"),dummy,"")
startscreen2 = Screen("start2","",["\tYOU FOUND YOUR FIRST TREASURE!"]+["The lady of the L4k3 gave you this sweet sword\n"] +modify_text_file("inventory/art/inv0_art.txt")+modify_text_file("inventory/descriptions/inv0_description.txt")+[""]+[modify_text("\t\t\t----#BPress Any Key to ContinueB#----")],dummy,"")
winscreen = Screen("end","",modify_text_file("screens/winscreen.txt"),dummy,"")
losescreen = Screen("end","",modify_text_file("screens/losescreen.txt"),dummy,"")
mobscreens = [Screen("mob","regex: ",globals.hit_mobs[i].art+globals.hit_mobs[i].strings+[""]+globals.miss_mobs[i].art+globals.miss_mobs[i].strings+["","Type a single regex to hit the monsters but avoid hitting the woodland creatures"],on_load,"mob%d"%i) for i in range(0,globals.num_mobs)]
invscreens = [Screen("inv","",[modify_text("\t\t\t----#GYOU FOUND A TREASURE!G#----"),""]+globals.inventory[i].art+[""]+globals.inventory[i].desc,on_load,"inv%d"%i) for i in range(0,len(globals.inventory))]

###########list of files to create
#mob regexes


#ascii text art powered by https://github.com/patorjk/figlet.js

