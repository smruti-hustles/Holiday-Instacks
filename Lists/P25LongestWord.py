n=int(input())
l=[]
for i in range(n):
    a=input()
    l.append(a)
length=0
res=l[0]
for j in l:
    if len(j)>length:
        length=len(j)
        res=j
print(res)               