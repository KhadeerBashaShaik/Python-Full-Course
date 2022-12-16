import pytest
def print_factors(x):
    print("The factors of",x,"are:")
    s=[]
    for i in range(1, x + 1):
        if x % i == 0:
            s.append(i)
    return s
           

num = int(input("enter the value of n"))
n=int(input("enter the no.of factors"))
l=[]
print("enter the factors")
for i in range (n):
    x=int(input())
    l.append(x)
assert print_factors(num)==l
