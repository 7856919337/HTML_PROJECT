from time import time


x=int(input("total no of class:"))
y=int(input("no of class attained:"))
z=(y/x)*100
if z>=70:
    print("you are eligible")
else:
    print('better luck next time')