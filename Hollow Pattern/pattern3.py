# Plus Pattern -2


n= int(input("Enter the place of rows: "))

for i in range(1,n*2):
    for j in range(1,n*2):  
        if (i==n or j==n):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 