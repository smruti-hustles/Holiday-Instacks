#hello ----> helo
n=input()
res=""
for i in n:
    if i not in res:
        res+=i
print(res)        