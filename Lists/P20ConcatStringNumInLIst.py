l=list(eval(input()))
n=int(input())
res=[i+str(j) for i in l for j in range(1,n+1)]
print(res)


output=[]
for a in range(1,n+1):
    for b in l:
        output.append(b+str(a))
print(output)        
