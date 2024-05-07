a=input()
b=input()
c=b[::-1]
l1=len(a)
l2=len(c)
s=''
if l1<l2:
    for i in range(l1):
        s+=a[i]+c[i]
    s+=c[l1:l2]
    print(s)  
else:
    for i in range(l2):
        s+=a[i]+c[i]
    s+=a[l2:l1]
    print(s)        

