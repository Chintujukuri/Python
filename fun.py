
import sys
def add(a,b):
    return (a+b)

def sub(a,b):
    return (a-b)

def mul(a,b):
    return (a*b)

a=float(sys.argv[1])
operation=sys.argv[2]
b=float(sys.argv[3])

if operation=="add":
    output=add(a,b)
    print(output)

if operation=="sub":
    output=sub(a,b)
    print(output)

if operation=="mul":
    output=mul(a,b)
    print(output)
