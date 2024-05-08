n=input()
l=len(n)
if l%4==0:
    res=n[::-1]
    print(res)
else:
    print(-1)    