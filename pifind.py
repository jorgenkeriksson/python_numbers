from math import pi

decimals = int(raw_input("Enter the number of decimals you wish to display pi with (max. 15). >> "))

if decimals > 15:
	print "That is not a valid input. The number of decimals is restricted to between 0 and 15"
elif decimals < 0:
	print "That is not a valid input. The number of decimals is restricted to between 0 and 15"
elif decimals == 0:
	print int(pi)
else:
	print round(pi, decimals)