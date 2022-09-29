Zork = 0
print("Before:", Zork)
for thing in [9, 41, 12, 3, 74, 15]:
        Zork = Zork +1
        print("Loop:", Zork, thing)
print("13 After:", Zork)

Avg = 0
Num = 0
print("Before:", Num)
for thing in [9, 41, 12, 3, 74, 15]:
        Num = Num +1
        Avg = thing + Avg
        print("Loop:", Num, thing,Avg)
Pavg=Avg/Num
print("After:",Num,Avg,Pavg)