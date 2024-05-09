n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()    
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print("*",end=" ")
    print()

'''
* 
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''    

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()    
for i in range(0,n+1):
    for j in range(0,n-i):
        print("*",end=" ")
    print()

'''
*
* *
* * *
* * * *
* * * * *
* * * * *
* * * *
* * *
* *
*
'''    





n=5
for i in range(0,n+1):
    for j in range(0,n-i):
        print("*",end=" ")
    print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()    


'''
*
* *
* * *
* * * *
* * * * *
* * * * *
* * * *
* * *
* *
*
'''    



n=5
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ", end=" ")   
    for k in range(1,i+1):
        print("*",end=" ")    
    print()
for i in range(0,n):
    for k in range(0,i):
        print(" ",end=" ")   
    for j in range(0,n-i):
        print("*", end=" ")      
    print()

'''
        *
      * *
    * * *
  * * * *
* * * * *
* * * * *
  * * * *
    * * *
      * *
        *
''' 



n=5
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ", end=" ")   
    for k in range(1,i+1):
        print("*",end=" ")    
    print()
for i in range(1,n+1):
    for k in range(1,i+1):
        print(" ",end=" ")   
    for j in range(1,n+1-i):
        print("*", end=" ")      
    print()

'''
        *
      * *
    * * *
  * * * *
* * * * *
* * * * *
  * * * *
    * * *
      * *
        *
''' 