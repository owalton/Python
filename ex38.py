#!/usr/bin/python

#Author: Octavius Walton
#Date: 
#Purpose Exercise 38

ten_things = "Apple Oranges Crews Telephone Light Sugar"

print "Wait there's not 10 things in that list, lets fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Fresbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print ' '.join(stuff) # whoa! Cool!
print '#'.join(stuff[3:5]) # super stellar!