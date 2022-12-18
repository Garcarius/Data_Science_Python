#Regular Expressions
import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) #true or false
# ^ <--start with   . match any character
# $ <-- end with
if x:
  print("YES! We have a match!")
else:
  print("No match")
