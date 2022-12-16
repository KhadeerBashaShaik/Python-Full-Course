import pytest
def sum(n):
    s=0
    for i in range (1,n+1):
        s+=i
    return s

def main():
    # n=int(input("enter the value of n"))
    n=8
    # t=int(input("enter the sum you think"))
    t=3
    assert sum(n)==t

main()