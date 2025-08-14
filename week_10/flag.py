flag = False
for number in range(1, 5):
	if number == 2:
		flag = True
		break
if flag:
	print(number)
else:
	print("not found")
