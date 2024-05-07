#here we are going to reverse the words.....eg. hello world -----> world hello
import re
n=input()
print(n)
r=re.split(" ",n)
print(r)
r1=r[::-1]
print(r1)
s=""
for i in r1:
    s=s+i+" "
print(s)    