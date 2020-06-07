


'''

A python calculator

'''


while True:

	print("Welcome To Calculator")

	print("Type 'Add' to start add two number together")

	print("Type 'Minus' to start add minus two number together")

	print("Type 'Divide' to start add divide two number together")

	print("Type 'Mulitply' to start add mulitply two number together")

	user_input  = input(":")

	if user_input == "Add":

		num1 = float(input("Enter the first number"))
		num2 = float(input("Enter the second number"))
		result = num1 + num2

		print (f'The sum of {num1} and {num2} is {result}')

	elif user_input == "Minus":

		num1 = float(input("Enter the first number"))
		num2 = float(input("Enter the second number"))
		result = num1 - num2

		print (f'The subtraction of {num1} and {num2} is {result}')

	elif user_input == "Divide":

		num1 = float(input("Enter the first number"))
		num2 = float(input("Enter the second number"))
		result = num1 / num2

		print (f'The Division of {num1} and {num2} is {result}')

	elif user_input == "Multiply":

		num1 = float(input("Enter the first number"))
		num2 = float(input("Enter the second number"))
		result = num1 * num2

		print (f'The multiplication of {num1} and {num2} is {result}')


	elif user_input == "end":

		print("Thank you, run python calc.py to restart the calculator")

		break

	else:

		print("Make sure you use caps when entering a")

		break

