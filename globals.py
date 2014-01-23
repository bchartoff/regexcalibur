import os
from mobs import *
from inventory import *
import terminaloutput
modify_text_file = terminaloutput.modify_text_file

def init():
	global gameover, lives, active_input, active_screen, active_message, start_inventory, active_inventory, inventory, active_hit_strings, active_miss_strings, num_mobs, hit_strings, miss_strings, active_hit_mob, active_miss_mob, hit_mobs, miss_mobs

	gameover = False
	lives = 5
	active_input = ""
	active_screen = None
	active_message = None

	inventory_path = "inventory/descriptions/"
	num_inventory = len([name for name in os.listdir(inventory_path) if os.path.splitext(inventory_path+name)[-1].lower() == ".txt"])
	start_inventory = [Inventory(i) for i in range(0,1)]
	active_inventory = start_inventory
	inventory = [Inventory(i) for i in range(0,num_inventory)]

	hit_path = "mobs/hit_mobs/hit_strings/"
	miss_path = "mobs/miss_mobs/miss_strings/"
	hit_strings = [modify_text_file(hit_path+fn) for fn in os.listdir(hit_path) if os.path.splitext(hit_path+fn)[-1].lower() == ".txt"]
	miss_strings = [modify_text_file(miss_path+fn) for fn in os.listdir(miss_path) if os.path.splitext(miss_path+fn)[-1].lower() == ".txt"]
	active_hit_strings = []
	active_miss_strings = []

	num_mobs = len([name for name in os.listdir(hit_path) if os.path.splitext(hit_path+name)[-1].lower() == ".txt"])
	active_hit_mob = Mob("hit",0)
	active_miss_mob = Mob("miss",0)
	hit_mobs = [Mob("hit",i) for i in range(0,num_mobs)]
	miss_mobs = [Mob("miss",i) for i in range(0,num_mobs)]
