#!/usr/bin/python

#Author: Octavius Walton
#Date: 
#Purpose Exercise 15 Reading Files

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()