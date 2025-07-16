#Variable for names of students
#Student record
first_name= "Jon"
last_name= "Pip"
'''Taking student age
and NAtionality
'''
age=12
country="Nigeria"


'''
employee_name,employee_id,address = "Jo", "001","Rayfield"
date_of_birth,department,position ="12/02/25", "ICT","Manager"
print(employee_name, address, date_of_birth, position)
'''

print("Enter first name \n")
first_name=input("")

print("Enter surname \n")
surname=input("")

print("Enter last_name \n")
last_name=input("")

#first_name,surname, last_name="Jo", "Rimam", "Chika"
#print(first_name,surname,last_name)
#print(first_name + surname + last_name)
print("{} {} {}" .format (first_name, surname, last_name))
print(f"{first_name} {surname} { last_name}" )
