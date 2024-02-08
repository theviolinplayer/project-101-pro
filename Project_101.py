import random
response=input("Press y to roll dice: ")
while(response == "y"):
    random_num=random.randint(1,6)
    print(random_num)
    response=input("Press y to roll dice again: ")