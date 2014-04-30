#! /usr/bin/env python
def side_input(sentence):
	a = raw_input(sentence)
	if a != "head" and a != "tail":
		print "I cannot understand because the program is stupid. Please just enter 'head' or 'tail'"
		a = side_input(sentence)
	else:
		return a

def int_input(sentence):
	number = raw_input(sentence)
	try:
		number = int(number)
		return number	
	except:
		print "Not an int, try again."
		number = int_input(sentence)

def float_input(sentence):
	number = raw_input(sentence)
	try:
		number = float(number)
		return number
	except:
		print "Not a float, try again."
		number = float_input(sentence)