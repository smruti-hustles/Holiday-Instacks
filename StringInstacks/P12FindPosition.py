import re
n=input("Enter String : ")
ch=input("enter substring : ")

#to find the last position
last_position=n.rfind(ch)
if last_position!=-1:
    print(f"last position is {last_position}")
else:
    print(-1)


#finding first position
res=re.search(ch,n)
print(f"first position is {res.start()}")