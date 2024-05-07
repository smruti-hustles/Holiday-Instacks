l1=list(eval(input()))
l2=list(eval(input()))
l=[]
for i in l1:
    if i%2!=0:
        l.append(i)
for j in l2:
    if j%2==0:
        l.append(j)
print(l)        