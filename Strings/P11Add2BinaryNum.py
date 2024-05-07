#a="11"  b="1"  ans=100
a = input()
b = input()

# Convert binary strings to decimal and add them
result = int(a, 2) + int(b, 2)

# Convert the sum back to binary
binary_result = bin(result)[2:]  # [2:] to remove the '0b' prefix

print(binary_result)




'''

a=input()
b=input()

def binary(n):
    n1=n[::-1]
    res=0
    for i in range(len(n1)):
        res+=((2**i)*(int(n1[i])))
    return res   
 
result=binary(a)+binary(b)      #it gives ans in decimal but we want in binary


num=result
sum=''
while(num>0):
    r=num%2
    sum=str(r)+sum
    num//=2
print(sum)    #it gives the answer in binary
'''