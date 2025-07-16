#Question number one
#Variables
my_age=28
pi=3.14159

magic_number= ((my_age * 3) + pi) % 7


print(magic_number)
print(type(magic_number))

#Question number two

secret_word= "PythonIsAmazing"

part1=(secret_word[:6])
print(part1)

end_part=(secret_word[-7:])
print(end_part)

mid_word=(secret_word[6:8])
print(mid_word)

#string reverse

print(end_part[::2])

print(secret_word[len(secret_word)-1 ] )
'''
print(end_part[6])
print(end_part[5])
print(end_part[4])
print(end_part[3])
print(end_part[2])
print(end_part[1])
print(end_part[0])
'''
#Every seond character
print(end_part[::-2])

#Question number three

print(part1.upper())

mid_to_end=(secret_word[6:])
print(mid_to_end.lower())

#combination
combine=(part1.upper() + mid_to_end.lower())
print(combine)
