n=int(input("Enter no of ele of 1st list : "))
l1=[]
for i in range(n):
    a=int(input("Enter element : "))
    l1.append(a)

m=int(input("Enter no of ele of 2nd list : "))
l2=[]
for j in range(n):
    a=int(input("Enter element : "))
    l2.append(a)    

l=l1+l2
s=set(l)
res=sorted(s)
print(res)
