class Calculate:
    def  Rectangle(a,b):
        print(f"the primeter is: {2*a+2*b}\nThe area is: {a*b}")  # type: ignore

    def circle(x):
        print(f"The perimeter of circle is: {2*3.14*x}\nThe area of circle is: {3.14*x*x}")  # type: ignore

    def triangle(l,m,n):
        print(f"The perimeter of trinagle is: {l+m+n}\nThe area of triangle is: {0.5*m*n}")

        
def main():
    ch='yes'
    while(True):
        if ch=='yes':
            print("enter your choice\n1.circle\n2.Rectangle\n3.triangle")
            n=int(input())
            l=[]
            for i in range(n):
                c=int(input())
                l.append(c)
            if n==1:
                Calculate.circle(l[0])  
            elif n==2:
                Calculate.Rectangle(l[0],l[1])  
            else:
                Calculate.triangle(l[0],l[1],l[2])  
            print("Do you want to continue(yes/no)")
            ch=input()
        else:
            return

main()