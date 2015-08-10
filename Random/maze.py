# A short adventure game where you try to escape the maze 

# starts the program

room1Exit = {"north":"room2", "east":"room3"}
room1 = ["The room is dark even to your light-starved eyes. A faint drip of water sounds from the east, and a fetid sent assults your nose from the north.", room1Exit]
room2Exit = {"south":"room1", "east":"room4"}
room2 = ["Utter blackness assults you, with only your hands showing your way along the narrowing tunnel. Your feet squalch in something unpleasently organic. You can follow the tunnel east as water rises around your feet, or retreat to the south.", room2Exit]
room3Exit = {"north":"room4", "west":"room1"}
room3 = ["Light peaks the cavern walls where roots has started breakng apart the rock. The reason for this growth is obvious, a stream runs though the cavern, flowing north. Stillness beckons from the west.", room3Exit]
room4Exit = {"south":"room3", "west":"room2", "north":"room5"}
room4 = ["Soon your swiming through feezing water. Abrasions you never realized you had start to burn, then numb in the chill waters. The waters shallow into a dark tunnel to the west, light shines from the south, and a faint breeze comes from the north.", room4Exit]
room5Exit = {"north":"exit", "south":"room4"}
room5 = ["You stride out of the water in a small champer, light and the smells of growing things comes from a mouth to the north. Dark waters lap to the south.", room5Exit]
mazeExit = 1;


rooms = {"room1":room1, "room2":room2, "room3":room3, "room4":room4, "room5":room5, "exit":mazeExit}


def start():
	print("Stired from your slumber, you wake to a dark room. You have one Urge... Escape!!")
	movement()

def movement():
	place = "room1"
	while place != "exit":
		location = rooms[place]
		exits = location[1]
		print(location[0])
		path = input("Where do you travel: ")
		if path.lower() in exits:
			place = exits[path.lower()]
		else:
			print("That isn't a path to escape!")
	print("congradulations on escaping!")
