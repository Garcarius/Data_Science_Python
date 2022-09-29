""" Task
The provided code stub reads and integer,n , from STDIN. For all non-negative integers i<n , print i**2.

Example

The list of non-negative integers that are less than  is . Print the square of each number on a separate line. """

if __name__ == '__main__':
    n = int(input())

rn=range(0,21)

if n not in rn:
    print("number is out of range")
else:
    for i in range(0,n):
        print(i**2)
