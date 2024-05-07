l=eval(input())
res=[]
for i in range(len(l)):
    if i%2!=0:
        res.append(l[i-1])
    else:
        res.append(l[i+1])    
print(res)        

