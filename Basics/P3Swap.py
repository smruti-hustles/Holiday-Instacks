a=int(input())
b=int(input())
print(f" before : a is {a} and b is {b}")
c=a
a=b
b=c
print(f"after : a is {a} and b is {b}")


'''
without using 3rd variable
a=a+b
b=a-b
a=a-b
'''