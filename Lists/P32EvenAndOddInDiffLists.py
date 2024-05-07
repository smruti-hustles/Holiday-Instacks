n=int(input("Enter no of ele : "))
l=[]
for i in range(n):
    a=int(input("Enter element"))
    l.append(a)
l1=[]
l2=[]
for j in l:
    if j%2==0:
        l1.append(j)
    else:
        l2.append(j)    
print(l1)
print(l2)        