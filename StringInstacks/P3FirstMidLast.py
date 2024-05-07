n=input()
m=input()
l1=len(n)
ll1=l1//2
l2=len(m)
ll2=l2//2
'''
if l1%2==0 and l2%2==0:
    res=n[0]+m[0]+n[ll2]+m[ll2]+n[-1]+m[-1]
elif l1%2!=0 and l2%2==0:
    res=n[0]+m[0]+n[ll2+1]+m[ll2]+n[-1]+m[-1]
elif l1%2==0 and l2%2!=0:
    res=n[0]+m[0]+n[ll2]+m[ll2+1]+n[-1]+m[-1]
else:'''
res=n[0]+m[0]+n[ll1]+m[ll2]+n[-1]+m[-1]
print(res)