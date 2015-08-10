## A program to bring the end to a small universe
#
THE_FIRST_TOWER = []
THE_SECOND_TOWER = []
THE_THIRD_TOWER = []
TOWER_HIGHT = 0

def the_tower_of_hanoi(disks = 3):
	global TOWER_HIGHT
	TOWER_HIGHT = disks
	load_tower(disks)
	print_towers(disks)
	solve(disks, THE_FIRST_TOWER, THE_SECOND_TOWER, THE_THIRD_TOWER)

def solve(disks, source, storage, roost):
	if disks > 0:
		solve(disks - 1, source, roost, storage)
		if source[-1]:
			lift = source.pop()
			roost.append(lift)
			print("\n\n")
			print_towers(TOWER_HIGHT)
		solve(disks - 1, storage, source, roost)

def load_tower(disks):
	print("\n\n\n\n")
	for inits in range(disks, 0, -1):
		THE_FIRST_TOWER.append(inits)

def print_towers(hight):
	for floor in reversed(range(0, TOWER_HIGHT)):
		try:
			if THE_FIRST_TOWER[floor]:
				print("{0}|{0}".format(THE_FIRST_TOWER[floor]), end="")
		except IndexError:
			print(" | ", end="")
		print("		", end="")
		try:
			if THE_SECOND_TOWER[floor]:
				print("{0}|{0}".format(THE_SECOND_TOWER[floor]), end="")
		except IndexError:
			print(" | ", end="")
		print("		", end="")
		try:
			if THE_THIRD_TOWER[floor]:
				print("{0}|{0}".format(THE_THIRD_TOWER[floor]))
		except IndexError:
			print(" | ")
	print("***		***		***")