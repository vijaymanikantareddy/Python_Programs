def p(n):
     for i in range(0, n):
             for j in range(0,n):
                     if i==j or j==n-1-i:
                             print("*", end=" ")
                     else:
                             print(" " , end=" ")
             print()
             
             
p(int(input('enter a number: ')))
