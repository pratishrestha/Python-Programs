# Hollow Decreasing Triangle

'''

* * * * * 
*     *
*   *
* *
*

'''

n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(i,n):
        if(i==0 or j==i or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()