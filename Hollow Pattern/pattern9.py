# Hollow Diamond Pattern
'''

          * 
        *   * 
      *       * 
    *           * 
  *               *
    *           *
      *       *
        *   *
          *

'''
n=int(input("Enter the number of upper-half rows: "))
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        if(i==n-1 or j==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(i+1):
        if(i==n-1 or j==i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        if(i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(i,n):
        if(j==n-2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()