import random

secret_number = random.randint(1, 10)
while True:
	user_guess = int(input("Enter lucky number\n"))
	if user_guess == secret_number:
		print("Correct")
		break
	else:
		print("try again")

