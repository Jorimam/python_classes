#Taking user input
print("Enter First Name \n")
first_name= str(input(""))

print("Enter Surname \n")
surname= str(input(""))

print("Enter your Age \n")
age= int(input(""))

print("Enter your Height \n")
height= float(input(""))

print("Enter you hobie \n ")
hobie= str(input(""))

print("Is married \n")
marital_status= bool(input(""))


print("Name:  {} {} ".format(first_name, surname) )




print("Age: {} ".format( age))
print(f"Height: {height}")
print(f"Hobbie: {hobie} ")

print(f"Is married: {marital_status} ")


print(type(first_name))
print(type(age))
print(type(height))
print(type(hobie))
print(type(marital_status))

