sallary=int(input("enter your sallary :"))
a=int(input("enter your year of service :"))
if a>10:
    print(sallary+sallary*0.1)
elif a>6 and 10>a:
    print(sallary+(sallary*0.08))
elif a<6:
    print(sallary+(sallary*0.05))