
names = ["Tom", "Jerry", "Jo"]
user = input("Enter name\n").capitalize()
'''
flag = False
for name in names:
	if user == name:
		flag = True
		break
if flag:
	print("VIP")
else:
	print("regular")
'''

for name in names:
	if user in name:
		print("VIP")
		break
else:
	print("regular")
