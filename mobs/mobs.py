import terminaloutput
modify_text_file = terminaloutput.modify_text_file

class Mob:
	val = 0
	mobtype = ""
	def __init__(self,mobtype,val):
		self.val = val
		self.mobtype = mobtype
		self.art = modify_text_file("mobs/%s_mobs/%s_art/mob%d_%s_art.txt"%(mobtype,mobtype,val,mobtype))
		self.strings = modify_text_file("mobs/%s_mobs/%s_strings/mob%d_%s_strings.txt"%(mobtype,mobtype,val,mobtype))
		self.clean_strings = []
		for s in self.strings:
			self.clean_strings.append(s.replace("#G","").replace("G#","").replace("#R","").replace("R#",""))