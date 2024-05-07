n=input()
m=input()
l=len(n)
mid=l//2
if l%2==0:
    res=n[0:mid]+m+n[mid:]
else:
     res=n[0:mid+1]+m+n[mid+1:]    
print(res)