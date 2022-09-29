"""Task
The provided code stub reads two integers from STDIN, a and b . Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers."""

from math import prod


if __name__ == '__main__':
    a = int(input())
    b = int(input())
ra=range(1,10**10)
rb=range(1,10**10)

if (a in ra and b in rb):
    sum = a+b
    dif=a-b
    pr=a*b
    print(sum)
    print(dif)
    print(pr)
else:
    print("out of range")