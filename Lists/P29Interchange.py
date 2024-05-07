l=list(eval(input())) 
first=l[-1]
last=l[0]
l[0]=first
l[-1]=last
print(l)