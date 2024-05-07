n=int(input("Enter no of ele of 1st list : "))
m=int(input("Enter no of ele of 2nd list : "))


l1=[]
for i in range(n):
    a=int(input("Enter element : "))
    l1.append(a)


l2=[]
for j in range(m):
    a=int(input("Enter element : "))
    l2.append(a)    
s1=set(l1)
s2=set(l2)
res=s1.intersection(s2)
r=list(res)
print(sorted(r))    