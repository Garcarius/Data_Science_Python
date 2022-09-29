""" The included code stub will read an integer, , from STDIN.
Without using any string methods, try to print the following:
123...n
Note that "..." represents the consecutive values in between.
Example
n=5
Print the string 12345
Input Format
The first line contains an integer n
Constraints
1 <= n <150
Print the list of integers from  through  as a string, without spaces. """

if __name__ == '__main__':
    n = int(input())

i=''
co=1
r=range(1,151)
if n in r:
    while co <= n:
       i=i+str(co)
       co=co+1
    print(i)
else:
    print('number out of range')