'''
  *  
 ***
***** 
*****  
 ***
  *    
'''

N = 3
for i in range(N):
    for j in range(N-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    for j in range(i):
        print(" ",end="")
    print()

for i in range(N):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(2*N-(2*i+1)):
        print("*",end=" ")
    for j in range(i):
        print(" ",end=" ")
    print()