
#decimal to binary
a=int(input())
result1=bin(a)
print(result1)
result2=bin(a)[2:]
print(result2)


#binary to decimal
b=input()  #take binary numbers
r=int(b,2)#returns decimal value
print(r)

#octal to decimal
c=input()
r2=int(c,8)
print(r2)

#decimal to octal
d=int(input())
r3=oct(d)[2:]
print(r3)

#hexadecimal to decimal
c=input()
r2=int(c,16)
print(r2)

#decimal to hexadecimal
d=int(input())
r4=hex(d)[2:]
print(r4)