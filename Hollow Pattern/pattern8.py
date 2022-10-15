# Hollow Hill Patttern
'''

          *
        *   *
      *       *
    *           *
  * * * * * * * * *

'''
n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        if (j==0 or i==n-1):    # j==0 i.e 0 is the starting condition in nested loop
            print("*",end=" ")
        else:
            print(" ",end=' ')
    for j in range(i+1):
        if (j==i or i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()