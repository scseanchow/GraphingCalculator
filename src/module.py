def printMenu():
	choice = '0'
	q = 'q'
	while (choice != 'q'):

		choice = input("Enter choice: ")


		if (choice == 1):
			addition()
		if (choice == 2):
			subtraction()
		if (choice == 3):
			multiplication()
		if (choice == 4):
			division()
		if (choice == 5):
			squareRoot()
		if (choice == 6):
			power()
		if (choice == 7):
			power()
		if (choice == 8):
			graphFunction()
		if (choice == 9):
			graphFunction()
		if (choice == 10):
			leastCommonMultiple()
		if (choice == 11):
			randomNumberGenerator()
		if (choice == 12):



def addition():
	print ("Enter two numbers to perform addition.")
	number1 = raw_input("Number one:")
	number2 = raw_input("Number two:")
	return number1 + number2;

def subtraction():
	print ("Enter two numbers to perform subtraction")
	number1 = raw_input("Number one:")
	number2 = raw_input("Number two:")
	return number1 - number2;

def multiplication():
	print ("Enter two numbers to perform subtraction")
	number1 = raw_input("Number one:")
	number2 = raw_input("Number two:")
	return number1 * number2;

def division():
	print ("Enter two numbers to perform division")
	number1 = raw_input("Number one:")
	number2 = raw_input("Number two:")
	return number1 / number2;

def squareRoot():
	print ("Enter numbers to perform square root")

def power():
	print ("Enter x^y")
	number1 = input("X:")
	number2 = input("Y:")
	return pow(x,y)

def graphFunction():

	print ("Enter function variables: a,b,c,d")
	print ("For example: f(x) = ax^b + cx + d")
	a = input("A:")
	b = input("B:")
	c = input("C:")
	d = input("D:")

	print ("Enter the domain. Two x values seperated by a comma. (ex 1,100)")
	domain = raw_input ("Domain:")

	print ("Enter the step (delta x)")
	step = input("Step:")
	step = float(step)
	numbers = domain.split(',')
	minNum = float(numbers[0])
	maxNum = float(numbers[1])


	while (minNum <= maxNum):
		y = (a * pow(minNum,b)) + (c * minNum) + d
		print 'f(',minNum,') = ',y,' '
		minNum += step

def leastCommonMultiple():
	print ("Enter two numbers to calculate LCM")
	number1 = input("Number One:")
	number2 = input("Number Two:")
	print lcm(number1,number2)
