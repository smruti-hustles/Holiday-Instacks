n=int(input("Enter no of elements :  "))
l=[]
for i in range(n): 
    a=int(input("Enter the element : "))
    l.append(a)
print(l)
res=[j*j for j in l]
print(res)    
