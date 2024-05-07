#sum of factors=that num  1,2,3 are factors of 6 ....  so 1+2+3=6
#eg,,6,28,496,8128
n=int(input())
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
if s==n:
    print("Perfect number")
else:
    print("Not perfect number")            