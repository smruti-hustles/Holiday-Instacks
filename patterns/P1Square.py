n=5
for  i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()   


'''
* * * * * 
* * * * *
* * * * *
* * * * *
* * * * *
'''     


n=5
k=1
for  i in range(n):
    for j in range(n):
        print(k,end=" ")
    print()   

'''
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
  '''    

n=5
k=1
for  i in range(n):
    for j in range(n):
        print(k,end=" ")
        k+=1
    print() 

'''
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
'''    


n=5
for  i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print() 

'''
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''    

n=5
for  i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
    print() 
'''
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
'''   

n=5
for  i in range(1,n+1):
    for j in range(1,n+1):
        print(i*i,end=" ")
    print() 

'''
1 1 1 1 1
4 4 4 4 4
9 9 9 9 9
16 16 16 16 16
25 25 25 25 25
'''    

n=5
for  i in range(1,n+1):
    for j in range(1,n+1):
        print(j*j,end=" ")
    print() 
