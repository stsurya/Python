'''
*  
**
***  
**
*    
'''

N = 4
space = 2 * (N-1)
for i in range(N):
    for j in range(i+1):
        print(j+1,end="")
    for j in range(space+1):
        print(" ",end="")
    for j in range(i,-1,-1):
        print(j+1,end="")
    space -= 2
    print()