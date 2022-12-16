import pytest
def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)

num=int(input("enter the value of n"))
# num = 5;
s=int(input("enter the factorial value"))
# s=120

assert factorial(num)==s

