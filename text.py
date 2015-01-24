#!/bin/python
import copy

verbs = ["look", "walk", "take", "bag", "map"]
nouns = ["north", "east", "south", "west", "n", "s", "e", "w"]

bag = []

player_x = 1
player_y = 1

maze = [
	[1,1,1,1,1,1,1,1,1,1],
	[1,0,2,0,0,0,0,0,0,1],
	[1,1,1,1,0,0,0,0,0,1],
	[1,0,0,1,1,1,0,0,0,1],
	[1,0,0,0,0,1,0,0,0,1],
	[1,0,0,0,0,1,1,0,0,1],
	[1,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,1,0,1,0,0,1],
	[1,4,0,0,1,0,1,0,0,1],
	[1,1,1,1,1,1,1,3,1,1],
	[1,1,1,1,1,1,1,1,1,1],
]
height = len(maze)
width = len(maze[0])

def parse_input(input):
	words = input.split()

	verb = None
	noun = None
	for word in words:
		if word in verbs:
			verb = word
			continue
		elif word in nouns:
			noun = word
	return (verb, noun)

def read_input():
	user_input = raw_input("What do you want to do? ")
	out = parse_input(user_input.lower())
	if out[0] == "walk":
		walk(out[1])
		get_exits()
		look()
	if out[0] == "look":
		get_exits()
		look()
	if out[0] == "take":
		take()
	if out[0] == "bag":
		look_bag()
	if out[0] == "map":
		showmap()
	if out[1] in nouns:
		walk(out[1])
		get_exits()
		look()
	return out

def get_exits():
	exits = []
	if maze[player_y+1][player_x] == 0:
		exits.append("south")
	if maze[player_y-1][player_x] == 0:
		exits.append("north")
	if maze[player_y][player_x+1] == 0:
		exits.append("east")
	if maze[player_y][player_x-1] == 0:
		exits.append("west")
	print "There are exits in the following directions: %s" % exits

def look():
	if maze[player_y][player_x] == 2:
		print "You see an apple"
	if maze[player_y][player_x] == 3:
		print "You see a pizza"
	if maze[player_y][player_x] == 4:
		print "You see a beer"

def take():
	if maze[player_y][player_x]>1:
		bag.append(maze[player_y][player_x])
		print "You picked up a %s" % maze[player_y][player_x]
		maze[player_y][player_x] = 0

def showmap():
	thismap = copy.deepcopy(maze)
	thismap[player_y][player_x] = "@"
	import pprint
	pprint.pprint(thismap)

def look_bag():
	print "Your bag contains: %s" % bag
	if len(bag) > 2:
		print "You have found everything! WINNER!"
		import sys
		sys.exit()

def walk(direction):
	x_mod = 0
	y_mod = 0

	global player_x
	global player_y
	print "walking %s" % direction
	if direction in ("north", "n"):
		y_mod -= 1
	elif direction in ("south", "s"):
		y_mod += 1
	elif direction in ("west", "w"):
		x_mod -= 1
	elif direction in ("east", "e"):
		x_mod += 1
	else:
		print "Wasn't a compass direction"
		return

	try:
		value = maze[player_y + y_mod][player_x + x_mod]

	except Exception as e:
		print "Could not walk out of bounds"
		return
	
	if value != 1:
		player_y = player_y+y_mod
		player_x = player_x+x_mod
	else:
		print "You hit the wall"
	print "Player x: %s Player y: %s" % (player_x, player_y)
	print "Current cell is: %s" % maze[player_y][player_x]
	return

while True:
	read_input()
