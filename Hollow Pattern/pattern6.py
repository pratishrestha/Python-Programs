# Hollow increasing triangle

'''

*       
* *     
*   *   
*     * 
* * * * *

'''

n=int(input("Enter number of rows: "))
for i in range(n):
    for j in range(i+1):
        if(j==0 or j==i or i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()