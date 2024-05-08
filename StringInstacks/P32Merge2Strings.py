a=input()
b=input()
l1=len(a)
l2=len(b)
r1=''
if l1<l2:
    for i in range(l1):
        r1+=a[i]+b[i]
    print(r1+b[l1:l2])   
else:
    for i in range(l2):
        r1+=a[i]+b[i]
    print(r1+a[l2:l1])  

