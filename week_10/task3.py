students = []
for record in range(3):
	name = input("Name\n")
	gender = input("Gender\n")
	if gender == "f":
		pass
	elif gender == "m":
		pass
	else:
		print("Invalid input for gender")
	score = float(input("score\n"))

	student = {
		"name": name,
		"Gender": gender,
		"score": score
	}
	students.append(student)
print(students)
