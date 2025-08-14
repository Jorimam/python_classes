students = {
	"John": 60,
	"Mimi": 50,
	"Sarah": 30
	}

names = list(students.keys())
scores = list(students.values())
name_len = len(names)
counter = 0
while counter < name_len :
	print(names[counter])
	counter += 1
#print(f"Name: {names}" )
