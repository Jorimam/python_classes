print("""
+-----------------------+
|	Dail *555#	|
|	for options	|
+-----------------------+
""")
balance = 1000
command = input("Enter command\n")
if command == "*555#":
	print("""
1. Buy Airtime
2. Buy Data
3. Borrow
4. Check balance
5. Exit
		"""
	)
	option = input("Choose an option\n")
	if option == "1":
#handling airtime purchase
		phone_number = int(input("Enter beneficiary phone number\n"))
		amount = float(input("Enter amount you want to recharge\n"))
		if amount > balance:
			print("Insufficient funds.")
			print(f"Your balance is {balance}")
		else:
			balance -= amount
			print(f"{phone_number} has been recharged {amount}")
			print(f"Your current balance is {balance}")
#Handling data purchase
	elif option == "2":
		print("""
1. 1GB for 300
2. 2GB for 800
3. 3GB for 1000
		""")
		

		data_option = input("Select your data option\n")
		
		if data_option == "1":
			balance -= 300
			phone_number = int(input("Enter beneficiary phone number\n"))
			print(f" A sum of 300 has been deducted from your balance.Current balance is {balance}")
			print(f"{phone_number} has been subscribed with 1GB worth of data")
		elif data_option == "2":
			balance -= 800
			phone_number = int(input("Enter beneficiary phone number\n"))
			print(f" A sum of 800 has been deducted from your balance. Current balance is {balance}")
			print(f"{phone_number} has been subscribed with 2GB worth of data")
		elif data_option == "3":
			balance -= 1000
			phone_number = int(input("Enter beneficiary phone number\n"))
			print(f" A sum of 1000 has been deducted from your balance. Current balance is {balance}")
			print(f"{phone_number} has been subscribed with 3GB worth of data")
		else:
			print("Invalid input")
#Handling borrow option
	elif option == "3":
		print("""
1. Borrow Airtime
2. Borrow Data
		""")
		borrow_option = input("Enter borrow option\n")
		if borrow_option == "1":
			borrow_amount = float(input("Enter amount you want to borrow\n"))
			if borrow_amount > 2000:
				print("You cant borrow more than 2000")
			elif borrow_amount <= 2000:
				phone_number = int(input("Enter phone number\n"))
				print(f"{phone_number} has been recharged with {borrow_amount}")
		elif borrow_option == "2":
			print("""
1. 1GB for 300
2. 2GB for 800
3. 3GB for 1000
		""")
			data_option = int(input("Select data option\n"))
			if data_option == "1":
				phone_number = int(input("Enter phone number\n"))
				print(f"{phone_number} subscribed with 1gb worth of data")
			elif data_option == "2":

				phone_number = int(input("Enter phone number\n"))
				print(f"{phone_number} subscribed with 2gb worth of data")

			elif data_option == "3":
				phone_number = int(input("Enter phone number\n"))
				print(f"{phone_number} subscribed with 3gb worth of data")

			else:
				print("Error")

#Handling balance check
	elif option == "4":
		print(f"Your balance is {balance}")

#Handling stop option
	elif option == "5":
		print("Goodbye")
else:
	print("Invalid input")
	
'''
This is quite optional if bowwowing is dependent on the user's balance
		
		amount_to_borrow = float(input("Enter the amount you wish to borrow\n"))
		if amount_to_borrow <= balance:
			print(f"You have a balnce of {balance}, you do not need to borrow")
		elif amount_to_borrow > balance:
			balance -= amount_to_borrow
			phone_number = int(input("Enter phone number\n"))
			print(f"{phone_number} recharged with {amount_to_borrow}. Your current balance is {balance}")
		else:
			print("Invalid input")

'''
