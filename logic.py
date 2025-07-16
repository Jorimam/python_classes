#Simple calculator app
print('''----------------------
1. Addition
2. Subtraction
3. Multiplication 
4. Division
------------------------------
'''
)
#Addition
print("Enter two numbers to add")

print("First number")
first_number = input("")

print("Second number")
second_number = input("")

add =float(first_number) + float(second_number)

print(f"The sum of {first_number} and {second_number} is {add:,.2f}")
print("----------------------------------")
#Subtraction
print("Enter two numbers to subtract")

print("First number")
first_number = input("")

print("Second number")
second_number = input("")

sub =float(first_number) - float(second_number)

print(f"The difference of {first_number} and {second_number} is {sub:,.2f}")
print("----------------------------------")
