#More Conditional Structures

temp = "5"
cel = 0
try:
 fahr = float(temp)
 cel = (fahr - 32.0) * 5.0 / 9.0
except:
     print(" ")
print(cel)


astr=input('type your age ')
try:
     stra=int(astr)
     print('tyour age is ',stra)
except:
     print('-1 string not a number')