c=[]
n=int(input("enter no.of students: "))
a=int(input("enter the no.of subjects: "))
for i in range(1,a+1):
        c.append(int(input(f"enter subject number-{i} subject credits: ")))
t=sum(c)
f=[]
print(f"the total credits are={t}")
for x in range(1,n+1):
    g=[]
    ans=0
    print(f"enter the details for studnet-{x}")
    for i in range(1,a+1):
        g.append(int(input(f"enter subject number-{i} grades: ")))
    
    for i in range(0,a):
        ans=ans+g[i]*c[i]

    fans=ans/t
    print(f"the average cpga of this student-{x} is: {fans}")
    f.append(fans)
print(f"the highest grade in the class is={max(f)}")