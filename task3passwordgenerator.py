#password generator
import string
import random
n = int(input("enter the length(you want) of password : "))
character = string.ascii_letters + string.digits + string.punctuation
password = " "
for i in range(n):
    password+=(random.choice(character))
print("Genreted password : " ,password )