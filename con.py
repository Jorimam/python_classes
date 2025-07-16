#string formatting can use the comma style
#And two different types of formatting, .format and f:w


first_name =input("Enter Name \n") 
surname=input("Enter surname \n")
print("My name is {} {} ".format(first_name, surname) )

print(f"{first_name} you are a son of {surname}")
