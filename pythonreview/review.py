aNumber=10
anotherNumber=20

def isThisOdd(n):
    return n % 2 == 1

def multiplicationTable(n):
    for x in range(11):
        r = x * n 
        print(f"{x} x {n} = {r}")

print('Hello there')
if(isThisOdd(anotherNumber)):
    print(f"{anotherNumber} is odd")
else:
    print(f"{anotherNumber} is even")

multiplicationTable(7)