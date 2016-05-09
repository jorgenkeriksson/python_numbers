import sys

def main():
	print "Enter a number to have this program generate the Fibonacci sequence to that number."
	number = int(raw_input(">> "))
	seq(number)

def seq(number):
	fib1 = 0
	fib2 = 1
	fib = 1
	print fib1
	while fib <= number:
		print fib
		fib = fib1 + fib2
		fib1 = fib2
		fib2 = fib
	q = raw_input("Want to go again? (y/n) >> ")
	if q == "y":
		main()
	else:
		sys.exit()

main()