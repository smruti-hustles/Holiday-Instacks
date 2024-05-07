n=5
for  i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print() 

'''
* 
* *
* * *
* * * *
* * * * *
'''

n=5
k=1
for  i in range(1,n+1):
    for j in range(i):
        print(k,end=" ")
    print()   
'''
1
1 1
1 1 1
1 1 1 1
1 1 1 1 1
'''      
n=5
for  i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print() 

'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
n=5
for  i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print() 
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''    
n=5
for  i in range(1,n+1):
    for j in range(1,i+1):
        print(i*i,end=" ")
    print() 

n=5
for  i in range(1,n+1):
    for j in range(1,i+1):
        print(j*j,end=" ")
    print()     
