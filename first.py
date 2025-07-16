import time
print("**********************************")
print("Cohort III Microwave")


print("**********************************")
print("1. Open the micorwave")
print("2. Put the rice")
print("3. Set Time")
customer={}



username=input("Enter your name \n")
customer["name"]=username
time_to_microwave= float(input("Duration: \n"))
print("4. I will let you know when it is ready")
customer["Duration"]= time_to_microwave
price= time_to_microwave * 1000
customer["Amount"]=price
print("You are charged: ", price, "only") 
print(customer)

print("Your rice will be ready in {} min(s) {}".format(time_to_microwave, username, ))
time.sleep(time_to_microwave * 60)
print("5. Your food is ready")

