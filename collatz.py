def main():
	number = int(raw_input('Starting number? >> '))
	counter(number)


def counter(number):
	count = 0

	while number != 1:
		if number <= 1:
			print 'Starting number must be > 1!'
			main()
		elif number % 2 == 0:
			number = number / 2
			count += 1
		else:
			number = number * 3 + 1
			count += 1
	print 'Number of steps to 1 is:', count

main()