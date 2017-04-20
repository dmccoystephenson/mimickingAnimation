import time

def printSpace():
	for i in range(10):
		print " "

space = ""

def printGuy():
	print "%s  O" % space
	print "%s /|\\" % space
	print "%s / \\" % space
	
def printGuy2():
	print "%s \O/" % space
	print "%s  |_" % space
	print "%s  \\" % space

for i in range(35):
	printSpace()
	printGuy()
	printSpace()
	space = space + " "
	time.sleep(.2)
	
	printSpace()
	printGuy2()
	printSpace()
	space = space + " "
	time.sleep(.2)
