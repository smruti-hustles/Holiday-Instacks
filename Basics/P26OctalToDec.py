n=input() #1000
s=n[::-1]
sum=0
for i in range(len(s)):
    sum+=((8**i)*(int(s[i])))
print(sum)    

