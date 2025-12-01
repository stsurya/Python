'''
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
'''

N = 5
sp = (2*N) - 2
for i in range(N):
    print("*" * (i+1),end="")
    print(" "*sp,end="")
    print("*"*(i+1))
    sp-=2

sp+=4
for j in range(N-1):
    print("*"*(N-(j+1)),end="")
    print(" "*sp,end="")
    print("*"*(N-(j+1)))
    sp+=2