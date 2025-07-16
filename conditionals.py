

first_number=input("Enter first number \n")
second_number=input("Enter second number \n")


if first_number > second_number :
	print(f"{first_number} is greater than  {second_number}" )
elif first_number < second_number :
	print( "{} is less than {} ".format(first_number, second_number))

else:
	print(first_number, " is equal to ", second_number)
print(f"{first_number} {second_number}" )
