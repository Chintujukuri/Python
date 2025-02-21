import sys

input=sys.argv[1]
if input=="t2.micro":
    print("it will be $2 dollor")
elif input=="t1.medium":
    print("it will be $1 dollor")
else:
    print("we dont have ",input,"service")