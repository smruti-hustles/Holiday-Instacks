n=int(input())
l=[]
for i in range(n):
    a=input()
    l.append(a)
large=max(l)   
l.remove(large)
second_large=max(l)
print(f"second largest ele is {second_large}")