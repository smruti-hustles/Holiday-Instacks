#automorphic number last digits of square of number==number eg..76==5776
#0,1,5,6,25,76,376,625....
n=int(input())  #76
sq=n**2   #5776
s=str(sq)  #5776
s1=s[::-1]  #6775
t=str(n)  #76
t1=t[::-1]  #67
l=len(t1)
sub=s1[0:l]#67
if sub==t1:
    print("Automorphic")
else:
    print("Not Automorphic")    
