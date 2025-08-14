vip = ["Jon", "James", "Peter"]
check = input("Name\n").capitalize()
for name in vip:
	if name == check:
		print("VIP")
		break
	else:
		print("regular")
		continue

