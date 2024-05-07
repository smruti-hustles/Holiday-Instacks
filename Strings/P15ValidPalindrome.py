#A man, A plan, A Canal: Panama  ----> valid
#race a car ----> not valid palindrome

n=input()
s=n.upper()
t=''
for i in s:
    if i.isalnum():
        t+=i
r1=t
r2=r1[::-1]
if r1==r2:
    print("Valid Palindrome")
else:
    print("Not valid palindrome")              