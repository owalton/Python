#!/usr/bin/python

#Author: Octavius Walton
#Date: 
#Purpose Exercise 42

# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## ??
class Dog(Animal):

	def __init__(self, name):
		## ??
		self.nam = name

class Cat(Animal):

	def __init__(self, name):
		## ??
		self.name = name

## ??
class Person(object):

	def __init__(self, name):
		## ??
		self.name = name

		## Person has-s pet of some kind
		self.pet = None

## ??
class Employee(Person):

	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee,self).__init__(name)
		## ??
		self.salary = salary

## ??
class Fish(object):
	pass

## ??
class Salmon(Fish):
	pass

## ??
class Halibut(Fish):
	pass


## rover is-a Dog
rover = Dog("Rover")

## is-a cat
satan = Cat("Satan")

## is-a person
mary = Person("Mary")

## has-a
mary.pet = satan

## ?? 
frank = Employee("Frank", 120000)

## has-a
frank.pet = rover

## is-a 
flipper = Fish()

## is-a
crouse = Salmon()

## is-a
harry = Halibut()