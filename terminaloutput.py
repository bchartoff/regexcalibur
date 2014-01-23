class Colors:
	RED   = '\033[91;40m'
	REDB  = '\033[31;1m'
	GREENB  = '\033[32;1m'
	GREEN = '\033[92;40m'
	WHITE = '\033[97;40m'
	BLACK = '\033[97;100m'
	ENDC  = '\033[0m'

def modify_text(string, R1 = ""):
	string = string.replace("\n","")
	string = string.replace("#R1",R1)
	string = string.replace("#R",Colors.RED).replace("R#",Colors.ENDC)
	string = string.replace("#G",Colors.GREEN).replace("G#",Colors.ENDC)
	string = string.replace("#W",Colors.WHITE).replace("W#",Colors.ENDC)
	string = string.replace("#B",Colors.BLACK).replace("B#",Colors.ENDC)
	string = string.replace("#X",Colors.REDB).replace("X#",Colors.ENDC)
	string = string.replace("#Y",Colors.GREENB).replace("Y#",Colors.ENDC)
	return string

def modify_text_file(filename, R1 = ""):
	textfile = open(filename,"r")
	lines = textfile.readlines()
	output = []
	for line in lines:
		line = modify_text(line, R1)
		output.append(line)
	return output