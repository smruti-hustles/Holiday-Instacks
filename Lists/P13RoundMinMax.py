l=list(eval(input()))
p=[]
res=[round(i) for i in l]
print(res)
print(min(res))
print(max(res))
s=set(res)
t=sorted(s)
for i in t:
    print(i*5 ,end=" ")