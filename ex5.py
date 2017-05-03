#!/usr/bin/python

#Author: Octavius Walton
#Date: 
#Purpose Exercise 5 More Variables and Printing

my_name = 'Octavius Walton'
my_age = 40 # not a lie
my_height  = 72 # inches
my_weight = 273 # lbs
my_eyes = 'brown'
my_teeth = 'white'
my_hair = 'black'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "DAAMMMMNNNNN!!!"
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right 
print "if I add %d, %d, and %d I get %d." %(my_age, my_height, my_weight, my_age + my_height + my_weight)