smallest = None
print("Before:", smallest)
for itervar in [9, 41, 12, 3, 74, 15,-1]:
    if smallest is None or itervar < smallest :
        smallest = itervar
       # break <-- no debe estar por que rompe el ciclo
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)


Zork = 0
print("Before:", Zork)
for thing in [9, 41, 12, 3, 74, 15]:
        Zork = Zork +1
        print("Loop:", Zork, thing)
print("After:", Zork)

Avg = 0
Num = 0
print("Before:", Num)
for thing in [9, 41, 12, 3, 74, 15]:
        Num = Num +1
        Avg = thing + Avg
        print("Loop:", Num, thing,Avg)
Pavg=Avg/Num        
print("After *:",Num,Avg,Pavg)