#!/usr/bin/python

#Author: Octavius Walton
#Date: 
#Purpose Exercise 30


people = 30
cars = 40
buses = 15

if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "we can't decide."

if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "We still can't decide."

if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let just take the buses."

	