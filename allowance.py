#Initial value of allowance
allowance = 2000

#After buying books
allowance -= 400
print(f"Balance after I bought books N{allowance}")

#Found some extra bucks
allowance += 100
print(f"I found some money in my pocket, now my balance is N{allowance}")

#Bought snacks
allowance -= 250
print(f"balance after I bought snacks N{allowance} ")

#Took out 25%
allowance -= (0.25 * allowance)
print(f"Balance after I gave my sibblings 25% of my money N{allowance}")

#Data subscription
allowance -= ((1/3) * allowance)
print(f"Balance after I bought data N{allowance}") 

#Gave tithe
allowance =  allowance // 2
print(f"After tithing N{allowance}")

#Modulos
allowance %= 100
print(f"My last balance N{allowance}")

