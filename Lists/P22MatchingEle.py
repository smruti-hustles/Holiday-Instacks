l1=list(eval((input())))
l2=list(eval((input())))
res=False
for i in l1:
    for j in l2:
        if i==j:
            res=True
            break
print(res)
