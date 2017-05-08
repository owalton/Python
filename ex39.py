#!/usr/bin/python

#Author: Octavius Walton
#Date: 
#Purpose Exercise 39Dictionaries, Oh lovely Dictionaries


# create a mapping of state to abbreviation

states = [
	'Oregon:' 'OR',
	'Florida:' 'FL',
	'California:' 'CA',
	'New York:' 'NY',
	'Michigan:' 'MI'
]

# create a basick set of states and some cities in them 
cities = [
	'CA:' 'San Francisco',
	'MI:' 'Detroit',
	'FL:' 'Jacksonville'
]

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states 
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using state then cities dict
print '-' * 10
for state, abbrev in cities.items():
	print "%s is abbreviated %s" % (abbrev, city)

# now do both at the same time 
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
	print "Sorry, No Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the stat 'TX' is %s" % city

